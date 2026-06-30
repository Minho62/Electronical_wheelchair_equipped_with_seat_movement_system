# Electronical Wheelchair Equipped with Seat Movement System
## 목표
거동이 불편한 자(者)의 이동권 보장을 위한 전자식 휠체어를 개발한다.

하나, 휠체어 승 차 하차 간 사람의 힘을 필요로 하지 않는 자동 시트를 제작한다.
둘, Lidar센서를 기반한 공간정보 Mapping으로 예기치 못한 충돌 위험을 방지함과 동시에 자율 주행계(系)를 포함 시킨다. 또한 본 시스템은 단순한 이동 장치를 넘어, 사용자 중심적 조작 환경을 제공하는 것을 목표로 한다. 

이를 위해 블루투스 모듈, 조이스틱, 소형 터치 모니터 등 다양한 입력 방식을  통합하여  사용자의  조작  편의성을  대폭  향상시켰다.  Lidar  기반  SLAM  및 Navigation 기능을 도입함으로써, 사용자가 직접 조작하지 않아도 목적지까지 스스로 이동 할 수 있는 완전 자동화를 구현하고자 한다. 더불어 시트 이동 보조 기능은 승하차 과정에 서의 피로를 최소화하도록 설계하여, 사용자의 안전성과 독립성을 강화하는 데 목적을 둔다.

## 프로젝트 추진 배경 및 필요성
1)  노약자 장애인 등 거동이 불편한 사람에 대한 이동권 개선이 오랜 기간 사회적 화두(話頭)로서 거론되었다. 보조적, 제도적 방식으로 다양한 시도가 있었지만, 휠체어의 탑승 및 하차 과정에서 생기는 근본적인 불편함이 해소되지 않았다. 이에 본 캡스톤디자인으로 이것을 기술론적으로 해결하고자 하는 바이다.
2)	실제 대상자와의 인터뷰를 통해 철저히 대상에 시각을 고정한 UX(User experience)를 고려한 설계를 주안(主眼)점으로 설정한다. 이를 통해, 팔 힘 혹은 보조자에 의지하지 않는 전자식 휠체어 설계를 한다. 이는 첫째, 휠체어 승차 하차 과정에서의 자동화와 둘째, 충돌 방지 장치와 자율 주행 기능을 포함하는 계(系)를 포함한다.
3)	승차 하차 과정의 편의를 위해, 높낮이를 조절하는 Linear actuator와 시트의 움직임을 조절하는 Servo motor의 유기적인 동작을 통해 간단한 사용자의 조작으로 쉽게 승차 하차를 가능하게 하는 전자식 제어 시스템 구축을 한다. 
4)	충돌 방지 장치와 자율 주행은 모두 Lidar센서에 기반한 공간 좌표를 Mapping하고, ROS제어를 통해 구축한다. 고도화된 제어방식을 도입함으로써, 사람의 힘에 의존함과 동시에 즉각적인 충돌 반응이 힘든 기존의 휠체어에서 더욱 안정성 높은 기술 가치를 제공할 수 있다. 
5)	본 시스템은 기존 전동 휠체어가 해결하지 못한 승, 하차의 난이도, 자기 위치 인식의 부재, 충돌 방지 기능 미비와 같은 문제를 기술적으로 해소하고자 한다. 특히, 좌석 높낮이 조절과 시트 벌림 동작을 자동화함으로써, 기존에는 보호자의 힘이 필요했던 구간을 사용자 단독으로 수행할 수 있게 한다.
6)	Lidar, IMU를 기반으로 한 자율주행 시스템을 통합하여, 사용자가 특정 좌석 또는 저장된 위치로 휠체어를 자동 호출하거나 자동 주차할 수 있는 고도화된 환경을 제공한다. 이는 단순 편의성을 넘어, 실내 이동 중 돌발 장애물을 실시간으로 감지하고 회피할 수 있는 안전성 높은 이동 보조 기술을 가능케 한다.
7)	Jetson Nano 기반의 ROS 제어 플랫폼을 구축하여, 로봇이 주행 상태, 배터리 정보, 센서 데이터를 실시간으로 파악하고 반영하도록 하였다. 이러한 고성능 프로세서 기반의 제어 아키텍처는 향후 의료, 재활 환경에서도 확장 가능하도록 설계된 것으로, 산업적, 학술적 가치가 크다.


## 기대효과 및 활용방안
1)  거동이 불편한 모든 계층 군(群)을 대상으로 이동권 신장과 안정성에 있어 새로운 형태의 기술 표준을 제공할 수 있다. 특히, 대상자의 자율성과 전자식 장치에 기반한 보조 기능으로서 높은 사용자 만족도를 기대한다.
2)	본 제품을 통해 사용자 본인의 편의뿐만 아닌, 보호자의 편의까지 신장 가능한 제품이다. 나아가 사용자, 보호자, 의료기관의 선순환적인 연결성에 대해 가치를 가질 수 있다.
3)	종래의 수동적 의료기기에 첨단화를 통해 일련의 정보를 데이터화할 수 있다. 대상자의 정보를 수집하는 것뿐만 아닌, 제품 이용의 경험을 통해 Real time 개선이 가능하다. 이를 통해 사용자 경험(UX)을 고려한 기술로서, 새로운 이동 보조장치로서 유사 의료 산업 발전에 도움이 될 수 있다.
4)	승하차의 자동화, 사용자 위치 기반 자율주행, UI 기반 제어 등 고도화된 기능을 포함하고 있어 기존 휠체어 대비 높은 자율성을 제공한다. 사용자는 조작 장치에 능숙하지 않더라도, 단 한 번의 터치로 맵핑, 맵 저장, 자율주행 실행, 주차 기능을 수행할 수 있어, 사용자 경험(UX)의 질을 크게 향상시킨다.
5)	구축된 ROS 기반 플랫폼은 센서, 모터, MCU 간 통신 구조가 명확히 정립되어 있어, 향후 다양한 재활 보조 장치나 특수 목적 로봇에도 확장 적용이 가능하다. 특히, 저장된 위치로의 자동 귀환 기능, 장애물 실시간 회피 기능 등은 실내 이동 안전성 향상에 직접적으로 기여할 수 있다.
6)	본 연구를 통해 확보한 시트 이동 보조 알고리즘, 자율주행 인터페이스(UI), 로봇 제어 구조는 후속 연구, 산업 현장에서 응용될 것이며, 고령화 사회에서 증가하는 이동 보조 장치 수요에 대응하는 실질적 해결책으로 활용될 수 있다.
 
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
