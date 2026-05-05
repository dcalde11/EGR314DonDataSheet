# Reflection

This document is formatted for GitHub and intended to be included as a standalone markdown page in the project repository.

---

## Review of Module's Success

Reviewing the module requirements, several core objectives were successfully achieved while others remain in progress or partially implemented.

### Successfully Accomplished Requirements

- Implementation of a working UART communication system using framed messages (AZ/YB protocol).
- Integration of Hall effect sensor data acquisition via I²C (SoftI2C interface).
- Conversion of raw sensor values into a usable 0–360° angular measurement.
- Development of a non-blocking firmware loop structure for continuous system operation.
- Implementation of LED-based status indicators for TX, RX, sensor status, and error detection.
- Reliable message parsing with start/end frame validation and buffer handling.
- Basic relay-based communication between nodes in a daisy-chain architecture.

### Requirements Not Fully Met or Missed

- Full dual I²C bus implementation for separated subsystems (only a single I²C bus is currently active in firmware).
- Servo motor PWM control system for fin actuation is not yet implemented.
- Dead-reckoning position estimation (x, y, z integration using speed and orientation) is not implemented in the current firmware build.
- Debug GPIO trigger system (external hardware-based debug toggles) is not fully integrated into firmware.
- Complete alignment with the original Team 307 structured message specification (uint16_t standard) was simplified in the current implementation.

---

## Microcontroller/Module Startup Tip

Several challenges were encountered during system startup, particularly around communication reliability, sensor initialization, and system synchronization. The following tips summarize key lessons learned:

- Always verify GPIO assignments early, as mismatched pin mappings between schematic design and firmware caused significant debugging delays.
- Ensure I²C devices are detected before entering the main loop; adding a startup sensor check prevents silent system failure.
- UART framing issues (missing or incorrect start/end bytes) can cause cascading communication failures, so strict validation is essential.
- Implement LED indicators early in development to provide real-time feedback without relying solely on serial monitoring.
- Avoid blocking delays in the main loop, as they interfere with sensor polling and UART responsiveness.
- Use incremental testing (sensor → UART → integration) rather than building full system logic before verifying subsystems.
- Maintain a consistent message protocol format across all nodes to avoid parsing mismatches in the daisy-chain network.

---

## Lessons Learned

Working on this project provided significant insight into embedded systems design, real-time communication, and hardware-software integration. One of the most important lessons learned was the importance of system modularity. Designing the firmware in independent components (sensor acquisition, communication, and output control) made debugging and future expansion significantly easier.

Another key takeaway was the importance of strict communication protocols. Even small inconsistencies in message framing or data formatting led to major system instability, highlighting the need for disciplined protocol design in multi-node systems.

Timing and non-blocking execution were also critical lessons. Early implementations that used blocking delays caused missed sensor readings and UART buffer overflows, demonstrating the importance of event-driven or continuously polling architectures in embedded systems.

Hardware abstraction was another major learning point. Differences between the intended schematic design and actual firmware implementation revealed how important it is to keep hardware documentation synchronized with software development.

Finally, debugging strategies evolved significantly over the course of the project. LED indicators, staged subsystem testing, and sensor-first validation proved far more effective than relying solely on serial output.

Overall, the project reinforced the importance of incremental development, clear system architecture, and disciplined communication design in embedded systems engineering.

---

## Recommendations for Future Students

1. Begin development by validating hardware connections and GPIO assignments before writing full firmware logic, as early mismatches can lead to difficult debugging later.

2. Build and test each subsystem independently (sensor reading, UART communication, actuator control) before integrating them into a complete system.

3. Use strict and consistent communication protocols from the beginning, including defined start/end frames and fixed message structures.

4. Avoid blocking delays in embedded firmware and instead design systems using non-blocking loops or timed polling methods.

5. Implement basic debugging tools such as LED indicators or serial logs early in the project to simplify troubleshooting and system validation.
