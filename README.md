# **Development of a Mobile Robot for Autonomous & Manual Inspection of Confined Spaces Using Multi-Sensor Detection Systems**  

This repository contains the code, simulations, and documentation for my final-year internship project. The project focuses on designing and developing an autonomous mobile robot equipped with a **modular multi-sensor detection system** for navigating and inspecting confined spaces. The system supports both **autonomous** and **manual navigation**, making it adaptable to various inspection scenarios.  

## **Project Overview**  
🚀 **Autonomous & Manual Navigation**: Supports **autonomous path planning** and **manual control via remote interface**.  
🔍 **Multi-Sensor Fusion**: Integrated **LiDAR, stereo cameras, IMU, motor encoders, gas sensors, and temperature & humidity sensors** for comprehensive environmental monitoring.  
🛠 **Modular Sensor Hub**: Designed to adapt to multiple **sensor communication protocols (I2C, SPI, UART, CAN, etc.)**.  
🎮 **Manual Control Mode**: Operators can remotely control the robot for real-time inspections in complex environments.  
🎯 **Embedded Systems Development**: Developed firmware for **Jetson (high-level AI processing) and STM32 (real-time low-level control)**.  
📊 **Structural & Thermal Analysis**: Conducted **FEA for vibration and load assessment** and **CFD for electronics cooling optimization** using **ANSYS**.  

## **Features**  
- **Autonomous Navigation**: ROS-based path planning and obstacle avoidance.  
- **Manual Navigation**: Remote control via a user interface or joystick for real-time intervention.  
- **Multi-Sensor Fusion**:  
  - **LiDAR & Stereo Cameras** → Mapping & Obstacle Detection  
  - **IMU & Encoders** → Precise Localization  
  - **Gas, Temperature & Humidity Sensors** → Environmental Monitoring  
- **Gazebo-Based Simulation**: Virtual environment for testing and validation.  
- **ROS Integration**: Efficient robot control, mapping, and localization.  
- **Modular Sensor Hub**: Compatible with different sensor protocols for flexibility.  
- **Embedded Control**: Jetson for AI processing & STM32 for sensor acquisition and motor control.  
- **Structural & Thermal Optimization**:  
  - **ANSYS FEA** → Vibration & Load Analysis  
  - **ANSYS CFD** → Thermal Management for Electronics  

## **Contents**  
📂 **Code**: Navigation algorithms, sensor fusion logic, embedded firmware, and ROS nodes.  
📄 **Documentation**: System architecture, hardware design, sensor integration, and experimental results.  
🏗 **Simulations**: Gazebo environments for real-world scenario validation.  

## **Technologies Used**  
- **Programming Languages**: Python (mainly), C++ (for embedded systems)  
- **Frameworks & Tools**: ROS, OpenCV, TensorFlow (if applicable)  
- **Simulation & Analysis**: Gazebo (for robot simulations), ANSYS (for FEA & CFD analysis)  
- **Hardware**: **LiDAR, stereo cameras, IMU, motor encoders, gas sensors, temperature & humidity sensors, Jetson, STM32**  

## **Contributing**  
Contributions are welcome! Feel free to submit issues, feature requests, or pull requests.  

## **Contact**  
For inquiries or collaboration, reach out via moataz.seghyar@usmba.ac.ma or connect on my linkedin page at Moataz Seghyar.  
