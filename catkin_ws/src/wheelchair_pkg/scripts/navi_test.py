#!/usr/bin/env python3
import time
import rospy
import tf
from geometry_msgs.msg import Twist, PoseStamped, Quaternion
from std_msgs.msg import Empty, String, Bool
from actionlib_msgs.msg import GoalID                     # ★ 추가: goal cancel
from tf.transformations import euler_from_quaternion, quaternion_from_euler

class CmdVelMux:
    def __init__(self):
        # ---- 기존 입력 버퍼 ----
        self.teleop = Twist(); self.t_teleop = 0.0
        self.joy    = Twist(); self.t_joy    = 0.0
        self.nav    = Twist(); self.t_nav    = 0.0

        # 파라미터
        self.timeout  = rospy.get_param("~timeout", 0.5)   # s
        self.rate_hz  = rospy.get_param("~rate", 50)
        self.eps_lin  = rospy.get_param("~eps_lin", 1e-3)
        self.eps_ang  = rospy.get_param("~eps_ang", 1e-3)
        self.priority = rospy.get_param("~priority", ["teleop","joy"])  # 수동일 때 우선순위

        # 네비 프레임/토픽
        self.map_frame  = rospy.get_param("~map_frame",  "map")
        self.base_frame = rospy.get_param("~base_frame", "base_link")
        self.goal_topic = rospy.get_param("~goal_topic", "/move_base_simple/goal")

        # 모드 게이트: true=수동 허용, false=자동(네비) 전용
        self.manual_enable = False

        # 구독
        rospy.Subscriber("cmd_vel_teleop", Twist, self.cb_teleop, queue_size=5)
        rospy.Subscriber("cmd_vel_joy",    Twist, self.cb_joy,    queue_size=5)
        rospy.Subscriber("cmd_vel_nav",    Twist, self.cb_nav,    queue_size=10)

        rospy.Subscriber("manual_enable",  Bool,  self.cb_manual,     queue_size=5)   # ★ 게이트
        rospy.Subscriber("nav/save_pose",  Empty, self.cb_save_pose,  queue_size=1)
        rospy.Subscriber("nav/goto_saved", Empty, self.cb_goto_pose,  queue_size=1)
        rospy.Subscriber("nav/cmd",        String,self.cb_nav_cmd,    queue_size=1)   # "save"/"goto"

        # 퍼블리셔
        self.pub_out        = rospy.Publisher("cmd_vel", Twist, queue_size=10)        # 최종 속도
        self.pub_goal       = rospy.Publisher(self.goal_topic, PoseStamped, queue_size=1)  # 2D Nav Goal
        self.pub_goal_cancel= rospy.Publisher("/move_base/cancel", GoalID, queue_size=1)   # ★ 네비 취소

        # TF
        self.tf_listener = tf.TransformListener()
        rospy.sleep(0.5)

        # 저장 포즈
        self.saved_pose = None  # (x,y,yaw)

    # ---------- 콜백 ----------
    def cb_manual(self, msg:Bool):
        prev = self.manual_enable
        self.manual_enable = bool(msg.data)
        rospy.loginfo("[mux] manual_enable=%s", self.manual_enable)

        # False -> True (자동→수동)로 전환 시, 진행 중인 네비 goal 취소
        if self.manual_enable and not prev:
            self.cancel_nav_goal()

    def cb_teleop(self, msg:Twist):
        self.teleop = msg; self.t_teleop = time.time()

    def cb_joy(self, msg:Twist):
        self.joy = msg; self.t_joy = time.time()

    def cb_nav(self, msg:Twist):
        self.nav = msg; self.t_nav = time.time()

    # ---------- 유틸 ----------
    def valid(self, msg, tstamp):
        if (time.time() - tstamp) > self.timeout:
            return False
        # 완전 정지 명령은 유효 취급 안 함(원하면 아래 3줄 주석)
        if abs(msg.linear.x) < self.eps_lin and abs(msg.angular.z) < self.eps_ang:
            return False
        return True

    def cancel_nav_goal(self):
        """현재 실행 중인 모든 move_base goal 취소"""
        self.pub_goal_cancel.publish(GoalID())               # 빈 ID → 전체 취소
        rospy.logwarn("[mux] Sent /move_base/cancel (manual mode)")

        # 선택: 바로 정지 명령 1회 발행(관성으로 밀리는 것 최소화)
        stop = Twist()
        self.pub_out.publish(stop)

    def get_current_pose_map(self):
        try:
            self.tf_listener.waitForTransform(self.map_frame, self.base_frame,
                                              rospy.Time(0), rospy.Duration(1.0))
            (trans, rot) = self.tf_listener.lookupTransform(self.map_frame, self.base_frame, rospy.Time(0))
            x, y = trans[0], trans[1]
            roll, pitch, yaw = euler_from_quaternion(rot)
            return (x, y, yaw)
        except (tf.Exception, tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException) as e:
            rospy.logwarn_throttle(2.0, "[mux] TF lookup failed: %s", str(e))
            return None

    def publish_nav_goal(self, x, y, yaw):
        q = quaternion_from_euler(0.0, 0.0, yaw)
        goal = PoseStamped()
        goal.header.stamp = rospy.Time.now()
        goal.header.frame_id = self.map_frame
        goal.pose.position.x = x
        goal.pose.position.y = y
        goal.pose.position.z = 0.0
        goal.pose.orientation = Quaternion(*q)
        self.pub_goal.publish(goal)
        rospy.loginfo("[mux] 2D Nav Goal → (%.3f, %.3f, %.1f°)", x, y, yaw*180.0/3.1415926535)

    # ---------- 저장/이동 ----------
    def cb_save_pose(self, _):
        pose = self.get_current_pose_map()
        if pose is None:
            rospy.logwarn("[mux] Cannot save pose: TF(map→%s) unavailable.", self.base_frame)
            return
        self.saved_pose = pose
        x,y,yaw = pose
        rospy.loginfo("[mux] Saved pose: x=%.3f y=%.3f yaw=%.1f°", x, y, yaw*180.0/3.1415926535)

    def cb_goto_pose(self, _):
        if self.saved_pose is None:
            rospy.logwarn("[mux] No saved pose yet. Publish nav/save_pose first.")
            return
        x,y,yaw = self.saved_pose
        self.publish_nav_goal(x, y, yaw)

    def cb_nav_cmd(self, msg:String):
        cmd = msg.data.strip().lower()
        if   cmd == "save": self.cb_save_pose(None)
        elif cmd == "goto": self.cb_goto_pose(None)
        else: rospy.logwarn("[mux] Unknown nav/cmd: '%s' (use 'save' or 'goto')", cmd)

    # ---------- 루프 ----------
    def spin(self):
        r = rospy.Rate(self.rate_hz)
        while not rospy.is_shutdown():
            out = None

            if self.manual_enable:
                # 수동 허용: priority 순서대로 유효 입력 선택(teleop -> joy)
                for src in self.priority:
                    if   src == "teleop" and self.valid(self.teleop, self.t_teleop): out = self.teleop; break
                    elif src == "joy"    and self.valid(self.joy,    self.t_joy):    out = self.joy;    break
            else:
                # 자동 전용: 네비게이션 입력만 사용 (nav -> /cmd_vel_nav를 릴레이하여 입력 받는 구조 가정)
                if self.valid(self.nav, self.t_nav): out = self.nav

            # 선택된 게 없으면 퍼블리시 생략
            if out is not None:
                self.pub_out.publish(out)

            r.sleep()

if __name__ == "__main__":
    rospy.init_node("cmd_vel_mux")
    CmdVelMux().spin()
