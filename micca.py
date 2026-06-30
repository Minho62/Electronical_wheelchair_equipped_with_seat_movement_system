#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
import time

class CmdVelMux:
    def __init__(self):
        self.teleop = Twist(); self.t_stamp_teleop = 0.0
        self.joy    = Twist(); self.t_stamp_joy    = 0.0

        self.timeout = rospy.get_param("~timeout", 0.5)   # s
        self.eps_lin = rospy.get_param("~eps_lin", 1e-3)
        self.eps_ang = rospy.get_param("~eps_ang", 1e-3)

        self.sub_teleop = rospy.Subscriber("cmd_vel_teleop", Twist, self.cb_teleop, queue_size=5)
        self.sub_joy    = rospy.Subscriber("cmd_vel_joy",    Twist, self.cb_joy,    queue_size=5)

        self.pub_out    = rospy.Publisher("cmd_vel", Twist, queue_size=5)
        self.rate_hz    = rospy.get_param("~rate", 50)
        self.prio       = rospy.get_param("~priority", ["teleop", "joy"])  # 순서대로 우선

    def cb_teleop(self, msg):
        self.teleop = msg
        self.t_stamp_teleop = time.time()

    def cb_joy(self, msg):
        self.joy = msg
        self.t_stamp_joy = time.time()

    def is_valid(self, msg, tstamp):
        if (time.time() - tstamp) > self.timeout:
            return False
        if abs(msg.linear.x) < self.eps_lin and abs(msg.angular.z) < self.eps_ang:
            # 완전 정지 명령도 ‘유효’로 쓰고 싶다면 이 조건을 제거하세요.
            return False
        return True

    def spin(self):
        r = rospy.Rate(self.rate_hz)
        while not rospy.is_shutdown():
            out = Twist()
            # 우선순위대로 선택
            for src in self.prio:
                if src == "teleop" and self.is_valid(self.teleop, self.t_stamp_teleop):
                    out = self.teleop
                    break
                if src == "joy" and self.is_valid(self.joy, self.t_stamp_joy):
                    out = self.joy
                    break
            self.pub_out.publish(out)
            r.sleep()

if __name__ == "__main__":
    rospy.init_node("cmd_vel_mux")
    CmdVelMux().spin()

