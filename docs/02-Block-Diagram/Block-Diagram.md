---
title: Module's Block Diagram
tags:
- tag1
- tag2
---

## Block Diagram Overview

This block diagram illustrates the overall system architecture centered around the PIC18F47Q42 microcontroller. It shows how power is supplied and regulated, how Hall effect sensors provide input data, how LEDs are used as visual indicators, and how the subsystem interfaces with other team components and programming hardware.

---

## System Breakdown

### Power Source
- 9V alkaline battery provides the primary power input.
- Battery connects to the system through a snap-style battery connector.

### Power Levels
- A buck voltage regulator converts the 9V battery voltage down to **3.3V**.
- The 3.3V rail powers the microcontroller, Hall effect sensors, and LED indicators.

### Sensors
- Two Hall effect sensors are used to detect magnetic fields.
- Sensors communicate with the microcontroller using **digital I²C serial communication**.
- Sensor data is read and processed by the PIC18F47Q42.

### Actuators
- RGBW LEDs are used as visual indicators.
- LEDs are driven by **digital GPIO output pins**.
- LED states indicate when Hall effect sensor readings have been detected and processed.

### Team Connections
- Upstream and downstream headers provide interfaces to other team subsystems.
- These connections allow system integration while avoiding duplicated functionality across team members.


## Example Block Diagram 
Showing an example of how to import a screenshot of the block diagram created outside of git and brought into a page.

![Individual Block Diagram](https://github.com/dcalde11/EGR314DonDataSheet/raw/a509418d56f460ab2f5f93befa5f674fc9e85620/docs/02-Block-Diagram/314BD3.drawio.png)
