---
title: Module's Block Diagram
tags:
- tag1
- tag2
---

## Block Diagram Overview

This block diagram illustrates a simplified overall system architecture centered around the ESP32 microcontroller. It shows the major components with their mainstream connections, how power is supplied and regulated, the flow of information, 
and how the subsystem interfaces with other team components and programming hardware through input and output connections.

---

## System Breakdown

### Power Source
- A 12V 6A wall adapter provides the primary power input.
- The wall adapter powers two buck voltage regulators and the microcontroller subsystem.

### Power Levels
- Two parallel buck voltage regulators convert the input voltage down to 5V and 3.3V.
- The 3.3V rail powers the ESP32 microcontroller, Hall effect sensors, and LED indicators.
- The 5V rail powers the servos directly.

### Sensors
- Two Hall effect sensors monitor rotational movement.
- Two additional Hall effect sensors act as a remote to control servo movement, functioning as fins.
- All sensors communicate with the microcontroller using two digital I²C serial communication buses.
- Sensor data is read and processed by the ESP32.

### Actuators
- Green LEDs serve as visual indicators.
- LEDs are driven by digital GPIO output pins.
- LED states indicate when Hall effect sensor readings have been detected and processed.
- Two servos control fins for vehicle maneuverability.
- Two buttons are used for debugging and switching operational modes.

### Team Connections
- Upstream and downstream headers provide interfaces to other team subsystems.
- These connections allow system integration while avoiding duplicated functionality across team members.
![Individual Block Diagram](https://github.com/dcalde11/EGR314DonDataSheet/raw/79f4ddfb4dbc87574f77d2af221d91c7b53191c4/docs/02-Block-Diagram/FinalBD314V2.png)
