Hall Effect Sensor Control PCB

This PCB is designed to interface multiple Hall effect sensors with an ESP32 microcontroller for magnetic field detection and system control. 
The board includes a regulated power system that converts a +12 V input into stable +5 V and +3.3 V rails using switching regulators and 
filtering components. The +3.3 V rail powers the ESP32 module and Hall effect sensor ICs, while the +5 V rail supports servo outputs and 
auxiliary circuitry.

Two I²C buses are implemented using digital Hall sensors with pull-up resistors and decoupling capacitors to ensure reliable communication. 
The board also includes user interface elements such as push buttons, status LEDs, and debugging connectors for monitoring and testing. 
Additional connectors provide outputs for servo control and external peripherals.

Test points are distributed across the board for key signals and power rails to simplify debugging and validation during development.
