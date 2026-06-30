#!/usr/bin/env python3
import subprocess
import os
import time

def run(cmd):
    print(f"[RUN] {cmd}")
    return subprocess.call(cmd, shell=True)

home = os.path.expanduser("~")
map_name = "map1"   # 필요하면 나중에 바꿔도 됨

# 1) 맵 저장
run(f"rosrun map_server map_saver -f {home}/{map_name}")

time.sleep(3)

# 2) ROS 노드 전부 종료
run("rosnode kill -a")
time.sleep(2)

# 3) roslaunch / roscore 프로세스도 정리
run("pkill -f roslaunch")
run("pkill -f roscore")
run("pkill -f mapping_robot.py")
time.sleep(2)

run("pkill -f mapping_robot.py")
print("[INFO] Map saved and ROS/SLAM stack stopped.]")

# 4) kill parent terminal
parent_pid = os.getppid()   # 상위 프로세스 PID (gnome-terminal)
os.system(f"kill -9 {parent_pid}")