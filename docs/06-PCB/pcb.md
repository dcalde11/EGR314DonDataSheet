---
title: Module's PCB
---


### Hall Effect Sensor Control PCB

This PCB interfaces multiple Hall effect sensors with an ESP32 
microcontroller for magnetic field detection and system control. The board 
includes a regulated power system that converts a +12 V input into stable 
+5 V and +3.3 V rails using switching regulators and filtering components. 
The +3.3 V rail powers the ESP32 module and Hall effect sensor ICs, while 
the +5 V rail supports servo outputs and auxiliary circuitry.

Two I²C buses are implemented using digital Hall effect sensors with pull-
up resistors and decoupling capacitors to ensure reliable communication. 
User interface elements such as push buttons, status LEDs, and debugging 
connectors are included for monitoring and testing. Additional connectors 
provide outputs for servo control and other external peripherals.

Test points are distributed across the board for key signals and power 
rails, simplifying debugging and validation during development.

## PCB Resources

The Hall Effect Sensor Control PCB interfaces multiple Hall effect sensors 
with the ESP32 microcontroller, provides regulated power rails, and 
supports servo control and debugging.

### 3D and Board Images
- **3D View of PCB:**  
  ![3D PCB View](https://github.com/dcalde11/EGR314DonDataSheet/raw/8916ebebba7e6873621c8a66df29b36d032fd23d/docs/06-PCB/3DView.png)  
- **Whole PCB Layout:**  
  ![Whole PCB](https://github.com/dcalde11/EGR314DonDataSheet/raw/8916ebebba7e6873621c8a66df29b36d032fd23d/docs/06-PCB/WHOLEPCB.png)  
- **Front Side Power Section:**  
  ![Front Power PCB](https://github.com/dcalde11/EGR314DonDataSheet/raw/8916ebebba7e6873621c8a66df29b36d032fd23d/docs/06-PCB/Front_Power_PCB.png)  
- **Back Ground Layer:**  
  ![Back PCB](https://github.com/dcalde11/EGR314DonDataSheet/raw/0cc5e27c3bc17a7d2334c2a681f571045fff1c7e/docs/06-PCB/Back_Ground_PCB.png)  

### Downloads
- **Gerber Files (for fabrication):** [Download 314_HallEffectGerberV2.zip](https://github.com/dcalde11/EGR314DonDataSheet/raw/8916ebebba7e6873621c8a66df29b36d032fd23d/docs/06-PCB/314_HallEffectGerberV2.zip)  
- **DFM Analysis Report (JLCPCB):** [Download PDF](https://github.com/dcalde11/EGR314DonDataSheet/raw/8916ebebba7e6873621c8a66df29b36d032fd23d/docs/06-PCB/DFM%20analysis%20report_JLCDFM_314_HallEffectGerberV2.zip.pdf)
