# PIC18F57Q43 MCC Configuration and Microcontroller Choice

## MPLabX & MCC Setup

For this project, I set up the **PIC18F57Q43** in MPLabX using MCC Melody. I enabled all the peripherals we need:  

- **EUSART1** for UART, so we can debug and send info to the team.  
- **MSSP1** in I2C master mode for talking to the AS5600 Hall effect sensor.  
- **PWM1_16BIT** to control LEDs and check sensor readings visually.  
- **ADC** on RA0, in case we want to add analog sensors later.  
- **GPIO** for status LEDs.  
- **ICSP** for programming and debugging the chip directly on the board.  

All the pins I used are conflict-free. The MCLR/RE3 pin is reserved for ICSP, which is normal — it’s basically needed to program and reset the PIC. The chip has 128 KB of flash and 8 KB of RAM, which is way more than we need right now, so there’s plenty of room if we want to expand the project later. The MCC build went through with no errors, so everything seems to work properly.  

---

## Pin Assignments

Here’s a breakdown of the pins we’re using for each peripheral:

| Function       | Peripheral     | Pin   | Notes                     |
|----------------|---------------|-------|---------------------------|
| UART TX        | EUSART1       | RC6   | Debugging / team comm     |
| UART RX        | EUSART1       | RC7   | Debugging / team comm     |
| I2C SCL        | MSSP1         | RC3   | AS5600 clock line         |
| I2C SDA        | MSSP1         | RC4   | AS5600 data line          |
| PWM LED        | PWM1_16BIT    | RC2   | Visual check for sensors  |
| Status LED GPIO| GPIO          | RA2   | General status indicator  |
| ADC Input      | ADC           | RA0   | Optional analog input     |
| MCLR           | ICSP          | RE3   | Reserved for ICSP/program |

 MCLR/RE3 is “exclusively acquired” by the ICSP module.

---

## PIC18F57Q43 Pin Images

![Pin Diagram](https://raw.githubusercontent.com/dcalde11/EGR314DonDataSheet/a67084c9d3d6aa6c7e49bd3d9a57a410ac671713/docs/08-MircoController/PINSS.png)



---

## Final Microcontroller Choice

**Chosen MCU:** PIC18F57Q43 (Surface Mount)

### Why I Picked It

I chose the PIC18F57Q43 because it has all the peripherals we need built-in, including UART, I2C, PWM, ADC, and GPIO, which makes the design and programming easier. It has over 32 I/O pins, providing room for LEDs, sensors, and potential 
future expansions, such as a second connector. It has roughly 128 KB of flash and 8 KB of RAM, meaning that memory limitations won’t be a concern for our project. Its 64 MHz HFINTOSC clock ensures smooth PWM, fast I2C communication, and stable 
UART performance. The on-chip ICSP support allows us to program and debug the microcontroller without removing it from the board, like the snap tool we have been using for the PIC18F47K42. Additionally, the PIC18F57Q43 comes in both surface 
mount and DIP packages, making prototyping flexible. Finally, full MCC Melody support ensures that code generation and peripheral configuration are quick and reliable.

