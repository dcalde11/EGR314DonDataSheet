---
title: Module's Selected Major Components
---

# Part 1: Major Component Selections


---

## 1. Hall Effect Sensor (Motion & Speed Sensing)

### Options Considered

#### Option 1: AS5600L-ASOM SOIC8 LF T&RDP
<img width="200" height="200" alt="image" src="https://github.com/user-attachments/assets/8a1ebea2-7ca5-44f9-b6c6-1774d983e67b" />

- **Price:** $3.20/unit  
- **Product Link:** [AS5600L-ASOM on DigiKey](https://www.digikey.com/en/products/detail/ams-osram-usa-inc/AS5600L-ASOM-SOIC8-LF-T-RDP/10324317)  
- **Datasheet:** [AS5600L Datasheet](https://look.ams-osram.com/m/657fca3b775890b7/original/AS5600L-DS000545.pdf)  

| Pros | Cons |
|------|------|
| Inexpensive | Slow shipping |
| Compatible with Thonny | Shipping fee |
| Easy to install | Hard to get readings |

#### Option 2: AS5600-ASOM SOIC8 LF T&RDP
<img width="200" height="200" alt="AS5600 Hall Effect Sensor" src="https://github.com/dcalde11/EGR314DonDataSheet/raw/f8f62ec46a2a4f0df44f42bfbb685c8b1fb6fd15/docs/03-Component-Selection/AS5600.png">


- **Price:** $3.17/unit  
- **Product Link:** [AS5600-ASOM on DigiKey](https://www.digikey.com/en/products/detail/ams-osram-usa-inc/AS5600-ASOM-SOIC8-LF-T-RDP/4914332)  
- **Datasheet:** [AS5600 Datasheet](https://look.ams-osram.com/m/7059eac7531a86fd/original/AS5600-DS000365.pdf)  

| Pros | Cons |
|------|------|
| Easy to read | Slow shipping |
| Compatible with Thonny | Shipping fee |
| Easy to install | Hard to get readings |

#### Option 3: AS5048A-HTSP-500
<img width="200" height="200" alt="image" src="https://github.com/user-attachments/assets/046b84b0-2fc0-4362-bee1-dacb8670e817" />

- **Price:** $7.90/unit  
- **Product Link:** [AS5048A on DigiKey](https://www.digikey.com/en/products/detail/ams-osram-usa-inc/AS5048A-HTSP-500/3188615)  
- **Datasheet:** [AS5048A Datasheet](https://look.ams-osram.com/m/287d7ad97d1ca22e/original/AS5048-DS000298.pdf)  

| Pros | Cons |
|------|------|
| More precise than AS5600 | SPI communication required |
| Direction detection possible | Requires precise magnet alignment |
| Easy to install | More expensive |

#### Option 4: A3212ELHLT-T
<img width="200" height="200" alt="image" src="https://github.com/user-attachments/assets/c515c5e1-c8d8-4a31-8d23-9ebcba874783" />

- **Price:** $0.53/unit  
- **Product Link:** [A3212ELHLT-T on DigiKey](https://www.digikey.com/en/products/detail/allegro-microsystems/A3212ELHLT-T/1006614)  
- **Datasheet:** [A3212 Datasheet](https://www.allegromicro.com/~/media/Files/Datasheets/A3211-12-Datasheet.ashx)  

| Pros | Cons |
|------|------|
| Controlled magnet orientation | Requires north/south pole switching |
| Direction detection possible | Requires precise magnet alignment |
| Easy to install | Detects either pole |

### Selected Sensor
- **Component:** AS5600L-ASOM (00x36) and AS5600-ASOM (00x40) 
- **Rationale:** I needed to use two different sensors because rewriting their slave address was not
possible, even with the use of a MOSFET. However, this setup allows for more controlled readings since there
will be no communication conflicts between the sensors and the ESP32. Both sensors have high enough
resolution to provide adequate response time in gathering the degrees of rotation around the Z-axis. Each
sensor is positioned to represent either pitch or yaw.
 
---

## 2. Power Regulation

### Option 1: TPS565242DRLR
<img width="200" height="200" alt="5V Voltage Regulator" src="https://github.com/dcalde11/EGR314DonDataSheet/raw/f8f62ec46a2a4f0df44f42bfbb685c8b1fb6fd15/docs/03-Component-Selection/5VoltR.png" />

- **Price:** $0.65/unit  
- **Product Link:** [TPS565242DRLR on DigiKey](https://www.digikey.com/en/products/detail/texas-instruments/TPS565242DRLR/16585745)  
- **Datasheet:** [TPS565242DRLR Datasheet](https://www.ti.com/lit/ds/symlink/tps565242.pdf)  

| Pros | Cons |
|------|------|
| Low dropout | Generates heat at high Vin |
| Fixed 3.3V output | Limited to 250mA |
| Easy to install | — |

### Option 2: TLV73312PDBVR
<img width="200" height="200" alt="image" src="https://github.com/user-attachments/assets/8a91c22b-b99c-43a8-9a07-9cd02a98f67d" />

- **Price:** $0.17/unit  
- **Product Link:** [TLV73312PDBVR on DigiKey](https://www.digikey.com/en/products/detail/texas-instruments/TLV73312PDBVR/5022371)  
- **Datasheet:** [TLV73312 Datasheet](https://www.alldatasheet.com/datasheet-pdf/download/2205575/TI2/TLV73312PDBVR.html)  

| Pros | Cons |
|------|------|
| Low dropout | Generates heat at high Vin |
| Fixed 3.3V output | Limited to 250mA |
| Easy to install | — |

### Option 3: LP38511MRX-ADJ/NOPB
<img width="200" height="200" alt="image" src="https://github.com/user-attachments/assets/8a2c37bb-ea94-447d-a0be-842722ccb03b" />

- **Price:** $1.89/unit  
- **Product Link:** [LP38511MRX on DigiKey](https://www.digikey.com/en/products/detail/texas-instruments/LP38511MRX-ADJ-NOPB/2075502)  
- **Datasheet:** [LP38511MRX Datasheet](https://www.ti.com/lit/ds/symlink/lp38511-adj.pdf)  

| Pros | Cons |
|------|------|
| High output current | Converts excess voltage to heat |
| Adjustable output voltage | Requires external resistors |
| Accurate | Thermal management required |

### Option 4: LP38511TJ-ADJ/NOPB
<img width="200" height="200" alt="image" src="https://github.com/user-attachments/assets/99ae5960-4966-4fa2-a424-29bc71ba8d54" />

- **Price:** $1.89/unit  
- **Product Link:** [LP38511TJ on DigiKey](https://www.digikey.com/en/products/detail/texas-instruments/LP38511TJ-ADJ-NOPB/2023099)  
- **Datasheet:** [LP38511TJ Datasheet](https://www.ti.com/lit/gpn/lp38511-adj)  

| Pros | Cons |
|------|------|
| High output current | Converts excess voltage to heat |
| Low dropout voltage | Adjustable voltage adds complexity |
| Adjustable output | Requires external resistors |
| Accurate | Thermal management required |

### Selected Regulator
- **Component:** TLV73312PDBVR and TPS565242DRLR
- **Rationale:** The reason we are using two different regulators is because the sensors and the ESP32 run
on 3.3 V, while the servos require roughly 5 V. Each servo has a stall current of about 2.5 A. The
TPS565242DRLR provides a controlled 5 V, 5 A output, which is adequate to power the servos and support them
during stall conditions. Both regulators operate in parallel to properly distribute power from the wall
adapter.
---

## 3. LED Indicators

### Option 1: QBLP679-RGBCW
<img width="200" height="200" alt="image" src="https://github.com/user-attachments/assets/d3756ca3-e984-466d-b36e-d0bd965d8457" />

- **Price:** $0.76/unit  
- **Product Link:** [QBLP679-RGBCW on DigiKey](https://www.digikey.com/en/products/detail/qt-brightek-qtb/QBLP679-RGBCW/13278847)  
- **Datasheet:** [QBLP679 Datasheet](https://www.qt-brightek.com/datasheet/QBLP679-RGBXW.pdf)  

| Pros | Cons |
|------|------|
| High brightness | Higher cost |
| Multiple channels | Higher complexity |
| Reduces number of LEDs | Requires multiple GPIOs |
| Accurate | Thermal management |

### Option 2: LTST-C190GKT
<img width="200" height="200" alt="image" src="https://github.com/user-attachments/assets/cbcbfd02-84c5-4eaf-8d4e-b25b22c191c2" />

- **Price:** $0.14/unit  
- **Product Link:** [LTST-C190GKT on DigiKey](https://www.digikey.com/en/products/detail/liteon/LTST-C190GKT/269230)  
- **Datasheet:** [LTST-C190GKT Datasheet](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/858/LTST-C190GKT.pdf)  

| Pros | Cons |
|------|------|
| Small footprint | Single color |
| Simple interface | Controlled by MCU pin |
| Low power consumption | Requires external resistor |
| Visible | — |

### Option 3: IN-P55QSTGRGBW
<img width="200" height="200" alt="image" src="https://github.com/user-attachments/assets/a9aaf32f-94c0-48c3-a0d4-bc4c70438904" />

- **Price:** $1.19/unit  
- **Product Link:** [IN-P55QSTGRGBW on DigiKey](https://www.digikey.com/en/products/detail/inolux/IN-P55QSTGRGBW/14555727)  
- **Datasheet:** [IN-P55 Datasheet](https://www.inolux-corp.com/datasheet/SMDLED/RGBW%20Top%20View/IN-P55QSTGRGBW_V1.0.pdf)  

| Pros | Cons |
|------|------|
| High brightness | Higher voltage input |
| Multiple channels | Higher complexity |
| Reduces number of LEDs | Requires multiple GPIOs |
| Accurate | Thermal management |

### Selected LED
- **Component:** LTST-C190GKT  
- **Rationale:** Single-color, SMT, simple interface, low power, cost-effective ($0.14/unit), ideal for basic vehicle motion/status indication. These LEDs are easy to integrate with PWM testing, and their low power draw ensures they won’t stress the 3.3V regulator. They also offer consistent brightness even with varying supply voltage, which is critical for accurate visual feedback.

---

## 4. Barrel Jack / Jumpers
### Option 1: PJ-070AH-SMT-TR
<img width="200" height="200" alt="Barrel Jack Connector" src="https://github.com/dcalde11/EGR314DonDataSheet/raw/06cb2f83ecf01079a6f8a901608ee002eb3983cb/docs/03-Component-Selection/BarrelJack.png" />

- **Price:** $1.49/unit  
- **Product Link:** [PJ-070AH-SMT-TR on DigiKey](https://www.digikey.com/en/products/detail/same-sky-formerly-cui-devices/PJ-070AH-SMT-TR/3466646)  
- **Datasheet:** [PJ-006A Datasheet](https://www.sameskydevices.com/product/resource/pj-070ah-smt-tr.pdf)  

| Pros | Cons |
|------|------|
| Standard barrel jack | Orientation matters since it points up|
| Sufficient for application | Shipping fee |
| Easy to install | Must ensure correct polarity |


### Option 1: PJ-006A-SMT-TR
<img width="200" height="200" alt="image" src="https://github.com/user-attachments/assets/7322b12c-4f87-4b09-8c01-1bb6030f3f31" />

- **Price:** $0.95/unit  
- **Product Link:** [PJ-006A-SMT-TR on DigiKey](https://www.digikey.com/en/products/detail/same-sky-formerly-cui-devices/PJ-006A-SMT-TR/408456)  
- **Datasheet:** [PJ-006A Datasheet](https://www.sameskydevices.com/product/resource/pj-006a-smt.pdf)  

| Pros | Cons |
|------|------|
| Standard barrel jack | Orientation matters |
| Sufficient for application | Shipping fee |
| Easy to install | Must ensure correct polarity |

### Option 2: PJ-006B-SMT-TR
<img width="200" height="200" alt="image" src="https://github.com/user-attachments/assets/8378c194-9761-4f94-acf5-dcb0bdc55573" />

- **Price:** $0.95/unit  
- **Product Link:** [PJ-006B-SMT-TR on DigiKey](https://www.digikey.com/en/products/detail/same-sky-formerly-cui-devices/PJ-006B-SMT-TR/408457)  
- **Datasheet:** [PJ-006B Datasheet](https://www.sameskydevices.com/product/resource/pj-006b-smt.pdf)  

| Pros | Cons |
|------|------|
| Standard barrel jack | Orientation matters |
| Sufficient for application | Shipping fee |
| Easy to install | Must ensure correct polarity |

### Option 3: FC68148S (Jumper)
<img width="200" height="200" alt="image" src="https://github.com/user-attachments/assets/39e5d7df-acec-4e3a-a7b0-95753e67676d" />

- **Price:** $1.55/unit  
- **Product Link:** [FC68148S on DigiKey](https://www.digikey.com/en/products/detail/cliff-electronic-components-ltd/FC68148S/20374233)  
- **Datasheet:** [FC68148S Datasheet](https://www.cliffuk.co.uk/products/dcconnectors/FC68148S.pdf)  

| Pros | Cons |
|------|------|
| Standard jumper | Small pitch, careful soldering |
| Allows power routing control | Jumper shunt may be separate purchase |
| Easy to integrate | Orientation matters |

### Selected Barrel Jack / Jumpers
- **Components:** PJ-070AH-SMT-TR + FC68148S  
- **Rationale:** Standard barrel jack,  easy to integrate; cost-effective ($0.95 + $1.55/unit). Using both ensures flexible power distribution, the jumper allows optional isolation of circuits for testing. The combination also minimizes PCB redesign if future expansion is needed.

---

## 5. Additional Hardware

### Selected Resistor
<img width="200" height="200" alt="image" src="https://github.com/user-attachments/assets/db28723b-d099-41ba-8cf4-d1f2f23a67bb" />

- **Component:** ERA-6AEB472V  
- **Price:** $0.10/unit  
- **Description:** 4.7 kΩ ±0.1% 0.125W 0805 Automotive AEC-Q200 Thin Film  
- **Datasheet:** [ERA-6AEB472V Datasheet](https://industrial.panasonic.com/cdbs/www-data/pdf/RDM0000/AOA0000C307.pdf)  
- **Link:** [DigiKey Product Page](https://www.digikey.com/en/products/detail/panasonic-electronic-components/ERA-6AEB472V/1465765)  
- **Rationale:** SMT 0805, precise value, automotive grade. It offers high stability under temperature variations and is ideal for reference or pull-up resistors in the I2C and ADC circuits. Its thin-film design reduces noise and improves signal accuracy.

### Selected Capacitor
<img width="200" height="200" alt="image" src="https://github.com/user-attachments/assets/81d06c28-9c3a-459e-b5a1-3b1e73eb52c9" />

- **Component:** GRM033R61A104KE15D  
- **Price:** $0.08/unit  
- **Description:** 0.1 µF ±10% 10V X5R 0201 Ceramic Capacitor  
- **Datasheet:** [GRM033R61A104KE15D Datasheet](https://search.murata.co.jp/Ceramy/image/img/A01X/G101/ENG/GRM033R61A104KE15-01A.pdf)  
- **Link:** [DigiKey Product Page](https://www.digikey.com/en/products/detail/murata-electronics/GRM033R61A104KE15D/2269163)  
- **Rationale:** SMT 0201, suitable voltage, compact and ideal for decoupling near the MCU. Its low ESR and X5R dielectric ensure stable power to sensitive analog circuits and reduce noise in I2C lines.

### Selected Capacitor
<img width="200" height="200" alt="image" src="https://github.com/user-attachments/assets/81d06c28-9c3a-459e-b5a1-3b1e73eb52c9" />

- **Component:** 1142  
- **Price:** $19.95/unit  
- **Description:** SERVOMOTOR RC 5V HIGH TORQUE 
- **Datasheet:** [1142 Datasheet](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/2203/1142_Web.pdf)  
- **Link:** [DigiKey Product Page](https://www.digikey.com/en/products/detail/adafruit-industries-llc/1142/5154658?s=N4IgTCBcDaILIHECcSCsIC6BfIA)  
- **Rationale:** - **Rationale:** We have experience using these servos, and there is also a possibility of being provided one by the professor. The range of 0–180 degrees is sufficient for adjusting the fins for this application.
---

## Summary Table of Final Choices

| Subsystem | Selected Component | Rationale |
|-----------|------------------|-----------|
| Motion Detection Sensor | AS5600L-ASOM + AS5600-ASOM | Two sensors used to avoid slave address conflicts, providing reliable I²C communication with the ESP32. High resolution allows accurate rotation measurement around the Z-axis; one sensor represents pitch, the other yaw. |
| 3.3V & 5V Regulators | TLV73312PDBVR + TPS565242DRLR | TLV73312PDBVR provides stable 3.3V for ESP32 and sensors; TPS565242DRLR provides 5V, 5A for servos including stall current. Regulators operate in parallel to efficiently distribute power from the wall adapter. |
| LED Indicator | LTST-C190GKT | Single-color SMT LEDs, low power, cost-effective, simple interface. Ideal for visual feedback and PWM testing without stressing the 3.3V regulator. |
| Barrel Jack / Jumpers | PJ-070AH-SMT-TR | Standard barrel jack for power input with flexible integration; jumper allows optional isolation of circuits for testing or future expansion. Cost-effective and easy to install. |
| Servo Motor (Control Fins) | 1142 RC Servo Motor | High-torque 5V servo used to control the fins for directional adjustments. The 0–180° motion range is sufficient for fin control, and prior experience with this servo simplifies integration and testing. |

