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

---

## Actual Firmware Implementation (MicroPython)

The implemented firmware runs on the ESP32-S3-WROOM-N4 and provides real-time communication between sensors, external devices, and actuators. The system is built around UART messaging, I²C sensor acquisition, and LED-based status indication for debugging and system monitoring.

---

### Core Communication System

The firmware uses a structured UART packet format with start and end delimiters (`AZ` and `YB`) to ensure reliable data transmission. Each message contains:
- A sender ID  
- A receiver ID  
- A payload containing command or sensor data  

Incoming UART data is buffered and only processed when a complete valid frame is detected. This prevents partial or corrupted messages from being interpreted.

When a message is received and addressed to the device, it is decoded and processed based on the sender type. If the message originates from a designated transmitter node, the system appends the current sensor angle and relays the updated packet to another module.

---

### Sensor Acquisition (I²C System)

The system uses a SoftI2C interface to communicate with a Hall effect rotary sensor. The firmware periodically reads raw sensor data from a fixed register address, then converts the 12-bit value into an angle ranging from 0° to 360°.

To ensure stable operation:
- Sensor polling is limited to 10 Hz  
- Read failures are handled using exception handling  
- The latest valid angle is stored globally for use in communication logic  

If the sensor is not detected on the I²C bus, the system halts normal processing and enters an error state.

---

### LED Status Indication

Four onboard LEDs provide real-time system feedback:
- **TX LED:** flashes during UART transmission  
- **RX LED:** flashes when a valid message is received  
- **Sensor OK LED:** indicates successful I²C sensor detection  
- **Error LED:** indicates sensor or communication faults  

This enables hardware-level debugging without requiring serial monitoring tools.

---

### Message Processing Logic

When a valid UART frame is received:
1. The frame is validated using start/end markers  
2. Sender and receiver IDs are extracted  
3. Payload data is parsed  
4. If the message is intended for this device, it is processed  

If the sender is a recognized upstream node, the system:
- Combines the received payload with the latest sensor reading  
- Formats a new response message  
- Transmits it to the next module in the chain  

This creates a chained communication system between nodes.

---

### System Timing and Control

The firmware operates using a non-blocking loop structure:
- UART is continuously polled for incoming data  
- Sensor readings are updated at 10 Hz  
- LED indicators respond immediately to system events  

This ensures consistent timing without blocking execution during communication or sensor reads.

---

### Error Handling Behavior

The system includes built-in fault detection:
- If the I²C sensor is not detected, normal operation is paused  
- Communication errors reset the UART buffer to prevent desynchronization  
- Sensor read exceptions are caught to prevent system crashes  

In error states, LEDs provide immediate visual feedback while maintaining system stability.

---

## Microcontroller Pin Usage (Actual Implementation)

The firmware uses a simplified subset of the ESP32-S3 pin configuration compared to the full system design. Only essential communication, sensor, and indicator pins are active.

---

### Active Pin Assignments

| GPIO | Function | Description |
|------|----------|-------------|
| GPIO4  | TX LED Indicator | Blinks during UART transmission |
| GPIO5  | RX LED Indicator | Blinks when UART message is received |
| GPIO6  | Sensor OK LED | Indicates valid I²C sensor detection |
| GPIO7  | Error LED | Indicates sensor or communication faults |
| GPIO35 | I²C SCL | Clock line for SoftI2C sensor communication |
| GPIO36 | I²C SDA | Data line for SoftI2C sensor communication |
| GPIO38 | UART TX | Transmits processed system data |
| GPIO10 | UART RX | Receives incoming messages and commands |

---

### Pin Usage Summary

- **I²C Interface (GPIO35, GPIO36):** Used for reading angular position data from the Hall effect sensor.  
- **UART Communication (GPIO10, GPIO38):** Handles all system messaging and data exchange.  
- **LED Indicators (GPIO4–GPIO7):** Provide real-time system status feedback.

---

### Design Notes

Compared to the full hardware architecture, this firmware version does not implement:
- Dual I²C buses  
- PWM servo control outputs  
- External debug GPIO triggers  

This simplified configuration focuses on core functionality: sensor acquisition, UART communication, and system status monitoring.
