---
title: Module's Requirements
---

## Module Requirements
The table below outlines the key requirements designated to me, compiled from the team’s [Project Requirements](https://egr-314-team-307-spring-2026.github.io/Team307.github.io/03-Project-Requirements/Project-requirements/) . My primary responsibility focuses on the 
predicted 3D positioning and speed integration calculations for the vehicle. This subsystem is responsible for determining the 
vehicle’s motion state (also known as the zero state) and estimating movement using rotational data around the Z-axis combined with 
speed data received from another subsystem.

The speed information is received through UART communication and is used as the magnitude component in forming a motion vector. By 
combining rotational orientation data with the incoming speed values, the subsystem is able to estimate the vehicle’s predicted 
movement and directional state.

This module operates independently using a surface-mounted 3.3V switching power regulator and an ESP32 microcontroller as its primary 
processing unit. The system utilizes Hall effect sensors to detect rotational changes and determine the angular movement around the Z-
axis. Additional Hall effect sensors are used to control two servo motors that function as control fins for the vehicle.

A dedicated debug function allows the system to reset when needed, ensuring reliable operation during testing and deployment. 
Throughout operation, motion data is transmitted wirelessly to the main system interface for monitoring and analysis.

| **Requirement** | **Description** | **Measure of Threshold (Minimum to Pass)** | **Target Measure** | **Stretch Requirement (Y/N)** |
|--------------|---------------|-----------------|-----------------|:-----:|
| Surface-mounted 3.3V switching power regulator | Provides regulated power to the module, allowing the subsystem to operate independently from other systems. | ≥ 3.2 V output | 3.3 V regulated output | No |
| Surface-mounted microcontroller (ESP) | Serves as the primary processing unit responsible for data handling, sensor integration, and subsystem control. | ESP-based microcontroller | ESP32 microcontroller | No |
| Wireless Communication | Enables the module to transmit and receive operational data through a wireless network connection. | Ability to send and receive basic signal data | Efficiently transmit and receive Wi-Fi data using MQTT protocol | Yes |
| Speed Measurement Sensor (Hall Effect Sensor) | Measures or estimates the vehicle’s speed in 3D space based on rotational motion data. | ±10% measurement accuracy | ±5% measurement accuracy | No |
| Motion Detection (2 Hall Effect Sensors) | Determines whether the vehicle is moving, stopped, or changing direction by detecting motion states. | Correct identification of motion/zero state | Accurate and continuous motion state updates | No |
| Reaction Time | Time required for the subsystem to detect motion changes and report updated motion data. | < 2 ms response time | < 1 ms response time | No |
| Additional Hall Effect Sensors | Provides additional rotational feedback used for control fin positioning and extended motion monitoring. | Detect rotational change | Accurate rotational feedback for fin control | Yes |
| Servo Motors (Control Fins) | Controls fin movement to assist with vehicle maneuverability and directional adjustments. | Basic fin actuation | Responsive fin control based on sensor input | Yes |
