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

During startup the firmware waits for a UART handshake signal before beginning normal operation. If no signal is received within five seconds, the system performs a short automatic debug cycle before continuing with normal operation. If uart is recieved within that timeframe the intial debug cycle is skipped and operates as normal.

This startup process ensures the system can synchronize with external subsystems while still operating independently if communication is unavailable.
