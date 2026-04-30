# Hall Effect Sensor Control PCB

This PCB interfaces multiple Hall effect sensors with an ESP32 
microcontroller for magnetic field detection and system control. The board 
includes a regulated power
system that converts a +12 V input into stable +5 V and +3.3 V rails using 
switching regulators and filtering components. The +3.3 V rail powers the 
ESP32 module and 
Hall effect sensor ICs, while the +5 V rail supports servo outputs and 
auxiliary circuitry.

Two I²C buses are implemented using digital Hall effect sensors with pull-up 
resistors and decoupling capacitors to ensure reliable communication. User 
interface 
elements such as push buttons, status LEDs, and debugging connectors are 
included for monitoring and testing. Additional connectors provide outputs 
for servo control 
and other external peripherals.

Test points are distributed across the board for key signals and power rails, 
simplifying debugging and validation during development.

## PCB Resources
The Hall Effect Sensor Control PCB interfaces multiple Hall effect sensors
with the ESP32 microcontroller, provides regulated power rails, and supports 
servo control 
and debugging.

# PCB Resources

---

## 3D View
![3D PCB](https://github.com/dcalde11/EGR314DonDataSheet/raw/504a73d7ccef2306419345308a4a0fa6d56c8b2d/docs/06-PCB/3DPCB.png)

---

## Whole View
![Whole PCB](https://github.com/dcalde11/EGR314DonDataSheet/raw/504a73d7ccef2306419345308a4a0fa6d56c8b2d/docs/06-PCB/WholePCB.png)

---

## Front View
![Front PCB](https://github.com/dcalde11/EGR314DonDataSheet/raw/504a73d7ccef2306419345308a4a0fa6d56c8b2d/docs/06-PCB/FrontPCB.png)

---

## Back View
![Back PCB](https://github.com/dcalde11/EGR314DonDataSheet/raw/504a73d7ccef2306419345308a4a0fa6d56c8b2d/docs/06-PCB/BackPCB.png)

---

### DFM Analysis Report
[View DFM Report](https://github.com/dcalde11/EGR314DonDataSheet/raw/504a73d7ccef2306419345308a4a0fa6d56c8b2d/docs/06-PCB/DFM%20analysis%20report_JLCDFM_GerberFiles314.zip.pdf)



### Gerber Files
[Download Gerber Files](https://github.com/dcalde11/EGR314DonDataSheet/raw/504a73d7ccef2306419345308a4a0fa6d56c8b2d/docs/06-PCB/GerberFiles314.zip)



### Final Project Package
[Download Final314HallEffect.zip](https://github.com/dcalde11/EGR314DonDataSheet/raw/504a73d7ccef2306419345308a4a0fa6d56c8b2d/docs/06-PCB/FInal314HallEffect.zip)
