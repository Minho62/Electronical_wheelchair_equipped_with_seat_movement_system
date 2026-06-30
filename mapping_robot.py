#!/usr/bin/env python3
import subprocess
import time
import os

def run(cmd):
    print(f"[RUN] {cmd}")
    return subprocess.Popen(cmd, shell=True)

home = os.path.expanduser("~")

# 1) roscore
roscore = run("roscore")
time.sleep(5)   # roscore 완전히 뜰 때까지 기다림

# 2) turtlebot bringup
bringup = run("roslaunch turtlebot3_bringup turtlebot3_robot.launch")

time.sleep(3)

# 3) slam
slam = run(f"roslaunch turtlebot3_slam turtlebot3_slam.launch")

time.sleep(3)

# 4) rosserial
serial = run("rosrun rosserial_python serial_node.py _port:=/dev/ttyARDUINO _baud:=57600")

time.sleep(2)

# 5) wheelchair main control
wheel = run("rosrun wheelchair_pkg wheelchair.py")

# 프로세스가 종료되지 않도록 유지
roscore.wait()

# 6) kill the terminal itself
parent_pid = os.getppid()
os.system(f"kill -9 {parent_pid}")
