---
title: Module's Power Budget
tags:
- tag1
- tag2
---

## Power Budget ##

The power budget for the 3D positioning system was developed to estimate the total current and power requirements of all major components in the design. The system is powered 
by a 12 V, 6 A external wall supply, which feeds voltage regulators that generate the required 3.3 V and 5 V power rails.

The 3.3 V rail powers the low-voltage logic components, such as the ESP32-S3-WROOM-1-N4 microcontroller, two AS5600 sensors, two AS5600L sensors, and the system status/Debug 
LEDs. The 5 V rail powers the two high-torque RC servo motors used for the positioning mechanism, which require higher current
during operation.

A 25% safety margin was included in the power calculations to account for startup currents andfor any regulator inefficiencies. Based on the requirements, the selected 12 V, 
6 A wall supply provides sufficient power to reliably operate all subsystems in the 3D positioning system. The use of fixed and
adjustable voltage regulators ensures that each power rail maintains a stable output voltage even during load changes caused by servo movement. Proper decoupling capacitors 
and filtering components are also included in the design to reduce noise and improve overall power stability. This helps ensure
reliable operation of components of the system. Below is an image as well as a pdf.

## Power Budget Files

 ![Power Budget](https://raw.githubusercontent.com/dcalde11/EGR314DonDataSheet/f8b59d818f780010123a9663db23587123048be9/docs/07-Power%20Budget/POWERB.png)

[Download PDF](https://github.com/dcalde11/EGR314DonDataSheet/blob/f8b59d818f780010123a9663db23587123048be9/docs/07-Power%20Budget/BPOWER%20(1).pdf)
