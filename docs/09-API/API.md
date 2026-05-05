# API – Message Definitions (Hall Effect / Position Subsystem)

## Overview
This subsystem communicates over a UART daisy-chain network using a structured message protocol while its foundation 
comes from the [Team 307 – Message Types (uint16_t)](https://egr-314-team-307-spring-2026.github.io/Team307.github.io/04-Team-Block-Diagram/Team-Diagram/) some chabges were made and will
be reflected in the team website. Each message is framed and includes sender/receiver addressing.

- **START BYTE:** 0x7E  
- **END BYTE:** 0x7F  
- **Broadcast ID:** 0x00  
- **Board ID:** 0x02  

All messages listed below exist inside the message data field of the class protocol.

---

## Message Summary

### Messages Sent by This Subsystem

| Message Type | Name              | Description |
|-------------|------------------|------------|
| 3           | POSITION_UPDATE  | Sends position (x,y,z) and speed |

---

### Messages Received by This Subsystem

| Message Type | Name            | Description |
|-------------|----------------|------------|
| 1           | SPEED_UPDATE   | Updates system velocity |
| 2           | DEBUG_TOGGLE   | Toggles debug mode |
| 4           | BUS_TOGGLE     | Switches active bus |

---

### Broadcast Messages Acted On

| Message Type | Name            | Description |
|-------------|----------------|------------|
| 2           | DEBUG_TOGGLE   | System-wide debug control |
| 4           | BUS_TOGGLE     | System-wide bus control |

---

## Detailed Message Definitions

### Message Type 1 – Speed Update

| Byte | Variable Name | Type     | Min | Max | Description |
|------|--------------|----------|-----|-----|------------|
| 1    | message_type | uint8_t  | 1   | 1   | Identifier |
| 2    | sender_id    | uint8_t  | 0   | 255 | Sender |
| 3    | receiver_id  | uint8_t  | 0   | 255 | Target |
| 4–n  | speed        | float    | -100.0 | 100.0 | Velocity |

**Total Bytes:** Variable (typically 8–12)

**Used For:** Motor to Hall subsystem

**Example:**
[1, 1, 2, 25.5]

---

### Message Type 2 – Debug Toggle

| Byte | Variable Name | Type     | Min | Max | Description |
|------|--------------|----------|-----|-----|------------|
| 1    | message_type | uint8_t  | 2   | 2   | Identifier |
| 2    | sender_id    | uint8_t  | 0   | 255 | Sender |
| 3    | receiver_id  | uint8_t  | 0   | 255 | Target |
| 4    | debug_state  | uint8_t  | 0   | 1   | Toggle debug |

**Total Bytes:** 4

**Used For:** Any subsystem to All (broadcast)

**Example:**
[2, 1, 0, 1]

---

### Message Type 3 – Position Update

| Byte | Variable Name | Type     | Min | Max | Description |
|------|--------------|----------|-----|-----|------------|
| 1    | message_type | uint8_t  | 3   | 3   | Identifier |
| 2    | sender_id    | uint8_t  | 0   | 255 | Sender |
| 3    | receiver_id  | uint8_t  | 0   | 255 | Target |
| 4–7  | x            | float    | -1000 | 1000 | X position |
| 8–11 | y            | float    | -1000 | 1000 | Y position |
| 12–15| z            | float    | -1000 | 1000 | Z position |
| 16–19| speed        | float    | -100 | 100 | Velocity |

**Total Bytes:** 20

**Used For:** Hall subsystem to Broadcast

**Example:**
[3, 2, 0, 1.2, 3.4, 5.6, 2.0]

---

### Message Type 4 – Bus Toggle

| Byte | Variable Name | Type     | Min | Max | Description |
|------|--------------|----------|-----|-----|------------|
| 1    | message_type | uint8_t  | 4   | 4   | Identifier |
| 2    | sender_id    | uint8_t  | 0   | 255 | Sender |
| 3    | receiver_id  | uint8_t  | 0   | 255 | Target |
| 4    | bus_state    | uint8_t  | 0   | 1   | Active bus |

**Total Bytes:** 4

**Used For:** Any subsystem

**Example:**
[4, 1, 0, 1]

---

### Message Type 5 – Acknowledgement (ACK)

| Byte | Variable Name | Type     | Min | Max | Description |
|------|--------------|----------|-----|-----|------------|
| 1    | message_type | uint8_t  | 5   | 5   | Identifier |
| 2    | sender_id    | uint8_t  | 0   | 255 | Sender |
| 3    | receiver_id  | uint8_t  | 0   | 255 | Target |
| 4    | original_type| uint8_t  | 0   | 255 | Message being acknowledged |
| 5    | value        | uint8_t  | 0   | 255 | Returned data |

**Total Bytes:** 5

**Used For:** Confirmation of valid message reception

**Example:**
[5, 2, 0, 1, 25]

---

## Protocol

### Message Handling Rules
- Messages not addressed to this board are forwarded immediately  
- Messages addressed to this board are processed  
- Broadcast messages (receiver_id = 0) are processed and forwarded  
- Messages sent by this board and returned are discarded  

---

### Error Handling
- Messages without START/END bytes are ignored  
- Messages exceeding buffer size are trashed  
- Invalid or malformed messages are ignored  

---

### Priority Rules
1. Incoming messages are processed and forwarded first  
2. Outgoing messages are sent after processing  
3. No communication blocking in daisy-chain network  

---

## Notes / Improvements Over Team Spec
- Original team design lacked:
  - Byte-level structure
  - Data type definitions
  - Min/Max bounds  

---

## Firmware Implementation (Message Handling System)

### Overview
The firmware runs on an ESP32-S3 using MicroPython and integrates UART communication, a Hall effect sensor via I²C, and LED status indicators. It operates as a real-time node in a daisy-chain messaging system.

---

## UART Communication

The system uses a framed UART protocol with `AZ` (start) and `YB` (end) delimiters. Each message contains a sender ID, receiver ID, and payload.

### Message Types Handled
- **Receiving:** 1 message type (relay + sensor update input)
- **Sending:** 1 message type (processed relay output with sensor angle appended)

When a valid frame is received:
- The message is parsed into sender, receiver, and payload  
- Messages not addressed to the device are ignored or forwarded  
- TX/RX LEDs indicate communication activity  

If the sender is `b'G'`, the system appends the latest sensor angle and forwards it to `b'E'`.

---

## I²C Sensor System

A Hall effect rotary sensor (address `0x36`) is read using SoftI2C at 10 Hz.

- Converts raw 12-bit data into 0–360° angle  
- Stores latest angle for message processing  
- Sensor failure triggers error state  

---

## LED Status Indicators

- **TX (GPIO4):** UART transmission activity  
- **RX (GPIO5):** UART reception activity  
- **Sensor OK (GPIO6):** Valid I²C sensor detection  
- **Error (GPIO7):** Sensor failure or communication fault  

---

## System Behavior

- UART constantly polled  
- Sensor updates every 100 ms  
- Non-blocking loop execution  
- Invalid frames discarded  

---

## Communication Summary

- **Messages Received:** 1 primary relay/input type  
- **Messages Sent:** 1 relay output with appended sensor angle  

---

## Key Design Notes

- Simplified framed protocol (`AZ` / `YB`)  
- Combines sensing + communication loop  
- Prioritizes real-time execution over protocol complexity  

---

## Firmware Source Code

[Download Basic UART Code](https://raw.githubusercontent.com/dcalde11/EGR314DonDataSheet/4a1f67aaadf7519277476e082b6c2123e0716abe/docs/09-API/BasicCodewithUart.py)
