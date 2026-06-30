roscore

roslaunch turtlebot3_bringup turtlebot3_robot.launch
roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=$HOME/map.yaml


roslaunch turtlebot3_slam turtlebot3_slam.launch
roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch

rosrun rosserial_python serial_node.py _port:=/dev/ttyUSB1 _baud:=57600
rosrun wheelchair_pkg wheelchair.py 
rosrun wheelchair_pkg navi_test.py
rostopic pub -1 /nav/save_pose std_msgs/Empty "{}"
rostopic pub -1 /nav/goto_saved std_msgs/Empty "{}"
rostopic pub -1 /manual_enable std_msgs/Bool "data: true" 
rostopic pub -1 /manual_enable std_msgs/Bool "data: false" 
rostopic pub /cmd_vel_joy geometry_msgs/Twist "linear:                                               
  x: 0.5
  y: 0.5
  z: 0.0
angular:
  x: 0.0
  y: 0.0
  z: 0.0"

startup setting
gnome-terminal -- /bin/bash -c 'source /opt/ros/noetic/setup.bash; source /home/jetson/catkin_ws/devel/setup.bash; cd /usr/bin/python /home/jetson/start_robot.py'

bash -lc "/home/jetson/start_robot.py"
