## Microcontroller Firmware Overview

The system firmware is written in MicroPython and runs on the ESP32-S3-WROOM-N4 microcontroller. The program runs two I²C 
sensor buses, servo control, UART communication, and a debug system. Its primary purpose is to collect orientation data from 
Hall effect sensors, estimate vehicle motion, and control servo-driven fins based on sensor feedback.

### Main System Functions

The firmware performs two main operational tasks:

**Bus 0 – Dead-Reckoning System**
- Reads yaw and pitch from AS5600 and As5600L magnetic rotary sensors using one I²C bus.
- Receives speed input from UART communication.
- Calculates estimated position (x, y, z) using orientation and speed data.
- Transmits position and speed information back over UART for monitoring.

**Bus 1 – Servo Control System**
- Reads orientation data from sensors on a second I²C bus.
- Converts the sensor readings into logical servo angles.
- Generates PWM signals to control two servo motors used to adjust vehicle fins.

### Peripheral Interfaces

The ESP32-S3 utilizes several integrated peripherals to support the system:

| Peripheral | Function |
|-----------|----------|
| I²C Bus 0 | Sensor communication for dead-reckoning calculations |
| I²C Bus 1 | Sensor communication for servo control |
| UART2 | Speed input and telemetry communication |
| PWM | Servo motor control |
| GPIO | Status LEDs, debug inputs, and user interface buttons |

### Debug and Monitoring System

A debug mode allows system monitoring during testing and development.

Debug mode can be triggered by:
- **GPIO5 button** (falling edge trigger)
- **GPIO23 external signal** (rising edge trigger)

When enabled:
- System LEDs blink to indicate debug status.
- Normal sensor processing and servo control operations pause.
- The system can be toggled in and out of debug mode during operation.

### Sensor Data Processing

Sensor readings are filtered using exponential smoothing to reduce noise and improve stability:

```
filtered = α(new reading) + (1 − α)(previous value)
```

A smoothing constant of α = 0.3 is used to stabilize the yaw and pitch measurements before they are used in motion calculations or servo control.

This filtering is necessary because the Hall effect sensors measure rotational position over a 0–360° range, while the servo motors operate within a 0–180° range. To properly translate sensor data into usable servo commands, the sensor readings are first stabilized and then mapped using a piecewise conversion function. This function constrains the values within defined limits and converts the full rotational measurement into a logical servo range.

### System Startup Behavior

During startup the firmware waits for a UART handshake signal before beginning normal operation. If no signal is received within five seconds, the system performs a short 
automatic debug cycle before continuing with normal operation. If uart is recieved within that timeframe the intial debug cycle is skipped and operates as normal.

This startup process ensures the system can synchronize with external subsystems while still operating independently if communication is unavailable.

## Microcontroller Pin Connections

The ESP32-S3-WROOM-N4 microcontroller interfaces with sensors, actuators, communication peripherals, and debugging hardware.  
The table below summarizes the GPIO assignments used by the firmware and PCB design.

| GPIO | Peripheral / Function | Description |
|-----|----------------------|-------------|
| GPIO41 | I²C Bus 0 SDA | Software I²C data line for Bus 0 sensors |
| GPIO42 | I²C Bus 0 SCL | Software I²C clock line for Bus 0 sensors |
| GPIO40 | I²C Bus 1 SDA | Hardware I²C data line for Bus 1 sensors |
| GPIO39 | I²C Bus 1 SCL | Hardware I²C clock line for Bus 1 sensors |
| GPIO10 | UART2 RX | Receives speed and handshake data |
| GPIO12 | UART2 TX | Transmits telemetry and system data |
| GPIO8 | Servo Motor A | PWM output controlling fin servo A |
| GPIO18 | Servo Motor B | PWM output controlling fin servo B |
| GPIO4 | LED 1 (Bus 0 – Sensor 0x36) | Activity indicator for Bus 0 sensor |
| GPIO5 | LED 2 (Bus 0 – Sensor 0x40) | Activity indicator for Bus 0 sensor |
| GPIO6 | LED 3 (Bus 1 – Sensor 0x36) | Activity indicator for Bus 1 sensor |
| GPIO7 | LED 4 (Bus 1 – Sensor 0x40) | Activity indicator for Bus 1 sensor |
| GPIO15 | Bus Select Button | Toggles between Bus 0 and Bus 1 operation |
| GPIO16 | Debug Button | Manually toggles debug mode |
| GPIO9 | Debug Signal Input | External signal trigger for debug mode |
| GPIO19 | USB D− | USB communication line |
| GPIO20 | USB D+ | USB communication line |

### Pin Usage Summary

- **Two I²C buses** are used to isolate sensor communication for different subsystems.
- **UART2** provides speed input and telemetry communication between modules.
- **PWM outputs** control two servo motors responsible for adjusting the vehicle fins.
- **GPIO LEDs** provide visual indicators for sensor activity and debugging.
- **Debug and bus selection buttons** allow runtime system control during testing and development.
