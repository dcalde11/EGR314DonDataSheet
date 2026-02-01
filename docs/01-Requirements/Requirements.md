---
title: Module's Requirements
---

## Module Requirements
The table below outlines the key requirements designated to me, compiled from the team’s [Project Requirements](https://egr-314-team-307-spring-2026.github.io/Team307.github.io/03-Project-Requirements/Project-requirements/). My
responsibility lies in the Motion and Speed Sensing Module of the vehicle. The module itself is responsible for 
detecting the vehicle’s motion state (also known as the zero state), measuring speed, and identifying obstacles to 
ensure safe and accurate operation. The table details each requirement along with its description, outlining the 
minimum threshold necessary for the module to function correctly. Each component is surface-mounted, aside from
minor components such as resistors and capacitors. This module will operate independently using a surface-mounted
3.3V switching power regulator and an ESP32 microcontroller as its processing unit. It will utilize sensors such as 
Hall Effect sensors for speed measurement and distance sensors for obstacle detection, while communicating motion 
data wirelessly to the system or user interface. The module’s fast reaction time ensures that motion changes are 
detected and reported promptly, supporting the overall safe operation and control of the vehicle.

| **Requirement** | **Description** | **Measure of<br> Threshold <br> (Minimum to Pass)** | **Target<br>Measure** |**Stretch<br>Requirement<br>(Y-N)**|
|--------------|---------------| ----------------- | ----------------- | :-----: |
| Surface mounted, 3.3V switching power regulator | Will be used to supply power to the module as it has to work independently as well. | 3.2 Volts | 3.3 Volts | No |
| Surface mounted microcontroller (ESP) | Will Serve as the "Brain" of the module, | ESP | ESP32 | No |
| Wireless Communication | Able to send or receive a Wi-Fi data |Being able to send and get some sort of signal  | Efficiently Send and receive Wi-Fi Data to MQTT | Yes |
|Speed Measurement Sensor (Hall Effect Sensor)  |Measures/estimates the speed of the vehicle in 3D Space | +/- 10% accuracy | +/- 5% accuracy |No|
|Motion Detection|Detects whether the vehicle is moving, stopped, or changing direction | Correct State/ Zero State | Is able to update motion accurately | No |
|Reaction Time|Time required for motion changes to be detected and reported| Less than 2 milliseconds | Less than 1 millisecond | No |
|Distance Sensing| Detects nearby obstacles to inform motion state| Detects objects within 1 ft |Detects objects within 2ft with adjustable range | No |
