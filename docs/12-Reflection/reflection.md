---
title: Reflection
---

## Review of Module's Success

Reviewing the module requirements, several objectives were successfully achieved while others remained in progress or partially implemented.

### Successfully Accomplished Requirements

- Implementation of a working UART communication system using framed messages (AZ/YB protocol).
- Integration of Hall effect sensor data acquisition via I²C (SoftI2C interface).
- Conversion of raw sensor values into a usable 0–360° angular measurement.
- Development of a non-blocking firmware loop structure for continuous system operation.
- Implementation of LED-based status indicators for TX, RX, sensor status, and error detection.
- Reliable message parsing with start/end frame validation and buffer handling.
- Basic relay-based communication between nodes in a daisy-chain architecture.

### Requirements Not Fully Met or Missed

- Full dual I²C bus implementation for separated subsystems (only a single I²C bus is currently active).
- Servo motor PWM control system for fin actuation is not yet implemented.
- Dead-reckoning position estimation (x, y, z integration using speed and orientation) is not implemented in the current firmware build.
- Debug GPIO trigger system (external hardware-based debug toggles) is not fully integrated into firmware.
- Complete alignment with the original Team 307 structured message specification was simplified in the current implementation.

---

## Microcontroller/Module Startup Tip

Several challenges were encountered during system startup, particularly around communication reliability amoung team members, sensor initialization, and system synchronization. The following tips summarize key lessons learned:

- Always verify GPIO assignments early, as mismatched pin mappings between schematic design and firmware caused significant debugging delays.
- Ensure I²C devices are detected before entering the main loop; adding a startup sensor check prevents system failure.
- UART framing issues (missing or incorrect start/end bytes) can cause communication failures, so validation is important.
- Implement LED indicators early in development to provide real-time feedback.
- Maintain a consistent message protocol format across all nodes to avoid parsing mismatches in the daisy-chain network.

---

## Lessons Learned

1. I learned that modular system design is essential in embedded systems because separating sensor reading, communication, and control logic makes debugging significantly easier and reduces system complexity.

2. I learned that strict communication protocols are critical because even small inconsistencies in message framing or data formatting can cause complete system failure in multi-system UART networks.

3. I learned that non-blocking code structure is necessary for real-time embedded systems because blocking delays interfere with sensor updates, UART communication, and overall system timing.

4. I learned that hardware and firmware must always be kept the same because mismatches between schematic IO pin configuration and firmware implementation can cause difficult debugging sessions.

5. I learned that early validation of individual subsystems is more effective than full system integration attempts, since testing sensors, UART, and outputs separately reduces the number of unknown failure points.

6. I learned that debugging tools such as LED indicators are extremely valuable because they provide immediate hardware-level feedback.

7. I learned that sensor noise and instability must be handled through filtering such as exponential smoothing, especially when converting raw sensor readings into usable control signals.

8. I learned that system reliability depends heavily on robust error handling, because unhandled sensor failures or communication errors can cause the entire system to freeze or behave unpredictably.

9. I learned that documentation consistency is just as important as code implementation, because unclear or outdated system descriptions can lead to incorrect assumptions during development and testing.

10. I learned that choosing the adequate team members are important as well.



---

## Recommendations for Future Students

1. Begin development by validating hardware connections and GPIO assignments before writing full firmware logic, as early mismatches can lead to difficult debugging later.

2. Build and test each subsystem independently (sensor reading, UART communication, actuator control) before integrating them into a complete system.

3. Use strict and consistent communication protocols from the beginning, including defined start/end frames and fixed message structures.

4. Avoid blocking delays in embedded firmware and instead design systems using non-blocking loops or timed polling methods.

5. Implement basic debugging tools such as LED indicators in the project to simplify troubleshooting and system validation.
