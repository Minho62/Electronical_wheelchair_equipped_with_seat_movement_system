# Electronical Wheelchair Equipped with Seat Movement System

시트 이동 보조 기능을 탑재한 자율주행 휠체어 프로젝트입니다.  
본 프로젝트는 거동이 불편한 사용자의 승하차 부담을 줄이고, LiDAR 기반 자율주행 기능을 통해 실내 이동 편의성과 안전성을 높이는 것을 목표로 개발되었습니다.

## 1. Project 
https://github.com/user-attachments/assets/6ae830d9-bad3-4cb6-a0cc-cf844929c53a

<img width="607" height="610" alt="image" src="https://github.com/user-attachments/assets/2c46a123-254f-4f7f-9cbd-ad26499d85a8" />


본 시스템은 단순한 이동 보조 장치를 넘어, 사용자의 좌석 이동과 실내 주행을 보조하는 전자식 휠체어 플랫폼입니다.

주요 목표는 다음과 같습니다.

- 리니어 액추에이터 기반 시트 높이 조절
- 서보모터 기반 시트 벌림 동작 구현
- LiDAR 기반 SLAM 및 Navigation 기능 구현
- 블루투스, 조이스틱, 터치 모니터 기반 다중 조작 방식 제공
- ROS Noetic 기반 자율주행 시스템 구축
- OpenCR, ATmega328P, Jetson Nano 간 통합 제어 구조 구현


<img width="794" height="851" alt="image" src="https://github.com/user-attachments/assets/00b0aa47-20fb-40bb-ae7f-bf7abde5e6e2" />
<img width="800" height="641" alt="image" src="https://github.com/user-attachments/assets/54bfaa27-be79-4f84-80dc-94da780a97bf" />

## 2. Main Features

### 2.1 Seat Movement Assist System

사용자가 휠체어에서 다른 좌석으로 이동할 때 필요한 신체적 부담을 줄이기 위해 시트 이동 보조 기능을 구현했습니다.

동작 순서는 다음과 같습니다.

1. 휠체어가 목표 좌석 근처로 이동
2. 리니어 액추에이터를 이용해 시트 높이 조절
3. 목표 좌석과 높이 정렬
4. 서보모터를 이용해 시트 양쪽을 벌림
5. 사용자가 자연스럽게 좌석으로 이동
6. 시트 구조를 원위치로 복귀

### 2.2 Autonomous Navigation

YDLiDAR G2와 ROS Noetic 기반 SLAM/Navigation 시스템을 활용하여 실내 자율주행 기능을 구현했습니다.

- GMapping 기반 실내 지도 생성
- AMCL 기반 위치 추정
- Move Base 기반 목표 지점 이동
- LiDAR 기반 장애물 감지 및 회피
- RViz 및 터치 모니터 기반 목표 지점 설정

### 2.3 Multi Control Interface

사용자의 접근성을 높이기 위해 다양한 제어 방식을 지원합니다.

- Joystick Control
- Bluetooth Control
- Touch Monitor UI
- Autonomous Navigation Mode

## 3. Hardware

본 프로젝트에 사용된 주요 하드웨어는 다음과 같습니다.

- Jetson Nano
- OpenCR
- ATmega328P
- YDLiDAR G2
- DYNAMIXEL XM430-W210T
- Linear Actuator
- MG996R Servo Motor
- Bluetooth Module HC-06
- Joystick Module
- 7-inch HDMI Touch Monitor
- 12V Lithium Battery
- DC-DC Converter
- Custom Soldered Control Board

## 4. Software Environment

- Ubuntu 20.04
- ROS Noetic
- Python3
- C/C++
- Arduino Framework
- Rosserial
- TurtleBot3 Packages
- GMapping
- AMCL
- Move Base
- RViz
- RQT
- URDF / Xacro
- VS Code
- OpenCR Firmware Loader

## 5. System Architecture

본 시스템은 Jetson Nano를 중심으로 OpenCR과 ATmega328P가 분산 제어를 수행하는 구조입니다.

<img width="1119" height="391" alt="image" src="https://github.com/user-attachments/assets/37780eef-6b4a-4733-a91a-5e571b3e9734" />

- Jetson Nano
  - ROS Master
  - SLAM
  - Navigation
  - LiDAR 데이터 처리
  - UI 실행
  - cmd_vel 통합 제어

- OpenCR
  - 주행 모터 제어
  - 오도메트리 데이터 송신
  - IMU 데이터 처리

- ATmega328P
  - 리니어 액추에이터 제어
  - 서보모터 제어
  - 조이스틱 입력 처리
  - 블루투스 명령 처리
  - Rosserial 통신

## 6. System Block Diagram
<img width="1239" height="688" alt="image" src="https://github.com/user-attachments/assets/8460b541-7aa9-49f1-a81a-b462be0d7391" />


## 7. Electrical Schematic
<img width="1410" height="978" alt="image" src="https://github.com/user-attachments/assets/f2537051-7794-465d-807c-5a61a789c877" />

## 9. Robot Modeling

기구부는 CATIA와 Fusion 360을 활용하여 설계했습니다.
<img width="795" height="818" alt="image" src="https://github.com/user-attachments/assets/feae39c1-74e0-44d3-90e7-e8bd079e0cad" />

<img width="790" height="785" alt="image" src="https://github.com/user-attachments/assets/6bb5a8b3-7cbb-4ded-ae1f-648073d37e9f" />



## 10. Autonomous Driving UI

터치 모니터에서 한 번의 터치로 주요 기능을 실행할 수 있도록 UI 아이콘을 제작했습니다.

주요 기능은 다음과 같습니다.

<img width="800" height="479" alt="image" src="https://github.com/user-attachments/assets/cd66cf0f-96ff-4691-bdf1-0a7430783e60" />
<img width="388" height="387" alt="image" src="https://github.com/user-attachments/assets/bc353384-84b2-41af-8f17-53c6b5322e45" />
<img width="395" height="405" alt="image" src="https://github.com/user-attachments/assets/dbcfa87c-158d-423e-8c30-fe7ed99bc4b7" />
<img width="412" height="450" alt="image" src="https://github.com/user-attachments/assets/1c57e233-32cf-4bf3-ae62-c93212f68b6a" />

- Mapping Robot System
- Save Mapping
- Start Robot System

<img width="1145" height="566" alt="image" src="https://github.com/user-attachments/assets/13000736-56b7-4bd5-a37a-1fb6c27dc9f2" />

## Repository Structure

```text
Electronical_wheelchair_equipped_with_seat_movement_system/
├── catkin_ws/
│   └── src/
│       ├── turtlebot3/
│       ├── turtlebot3_description/
│       ├── turtlebot3_navigation/
│       └── wheelchair_control/
├── firmware/
│   ├── opencr/
│   └── atmega328p/
├── hardware/
│   ├── schematic/
│   └── modeling/
├── images/
│   ├── system_block_diagram.png
│   ├── electrical_schematic.png
│   ├── soldering_board.png
│   ├── robot_modeling.png
│   └── autonomous_ui.png
└── README.md
