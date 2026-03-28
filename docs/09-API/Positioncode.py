from machine import Pin, SoftI2C, PWM, UART
import time
import math

print("SYSTEM WITH UART MESSAGE PROTOCOL")

#  PROTOCOL 
START_BYTE = 0x7E
END_BYTE   = 0x7F

BOARD_ID = 0x02
BROADCAST_ID = 0x00

MAX_MSG_LEN = 64

MSG_TYPE = {
    1: "SPEED_UPDATE",
    2: "DEBUG_TOGGLE",
    3: "POSITION_UPDATE",
    4: "BUS_TOGGLE",
    5: "ACK"
}

uart_buffer = bytearray()

#I2C BUSES
i2c0 = SoftI2C(scl=Pin(22), sda=Pin(21), freq=100000)
i2c1 = SoftI2C(scl=Pin(26), sda=Pin(25), freq=100000)

# UART
uart2 = UART(2, 9600, tx=17, rx=16)

# SENSOR 
ADDR_36 = 0x36
ADDR_40 = 0x40
RAW_MSB = 0x0C
RAW_LSB = 0x0D

# LED 
led_b0_36 = Pin(4, Pin.OUT)
led_b0_40 = Pin(2, Pin.OUT)
led_b1_36 = Pin(13, Pin.OUT)
led_b1_40 = Pin(12, Pin.OUT)

#  BUTTONS 
bus_button = Pin(27, Pin.IN, Pin.PULL_UP)
debug_button = Pin(5, Pin.IN, Pin.PULL_UP)
debug_pin23 = Pin(23, Pin.IN, Pin.PULL_DOWN)

active_bus = 0
previous_bus = 0
last_bus_button = 1

debug_mode = 0
last_debug = 1
last_debug23 = 0
debug_state = 0


ALPHA = 0.3
filtered_angles = {(0, ADDR_36): None, (0, ADDR_40): None,
                   (1, ADDR_36): None, (1, ADDR_40): None}
v = 0.0
x = y = z = 0.0
last_time = time.ticks_ms()

servo_a = PWM(Pin(14))
servo_b = PWM(Pin(15))
servo_a.freq(50)
servo_b.freq(50)
servo_a.duty_u16(int((1.5 / 20) * 65535))
servo_b.duty_u16(int((1.5 / 20) * 65535))

def angle_to_duty(angle):
    angle = max(0, min(180, angle))
    pulse = 0.6 + (angle / 180.0) * (2.4 - 0.6)
    return int((pulse / 20.0) * 65535)

def set_servo_logical(servo, logical):
    logical = max(-90, min(90, logical))
    servo.duty_u16(angle_to_duty(logical + 90))

def sensor_to_servo(sensor_deg):
    s = sensor_deg % 360.0
    return -s/2 if s <= 180 else (s-180)/2

def read_angle(i2c, addr, led):
    try:
        msb = i2c.readfrom_mem(addr, RAW_MSB, 1)[0]
        lsb = i2c.readfrom_mem(addr, RAW_LSB, 1)[0]
        raw = ((msb << 8) | lsb) & 0x0FFF
        led.on()
        time.sleep_ms(5)
        led.off()
        return raw * 360.0 / 4096.0
    except:
        return None

def stabilize(bus, addr, new):
    if new is None:
        return None
    key = (bus, addr)
    prev = filtered_angles[key]
    filtered_angles[key] = new if prev is None else ALPHA*new + (1-ALPHA)*prev
    return filtered_angles[key]

# MESSAGE SEND
def send_message(msg_type, receiver, payload):
    msg = bytearray()
    msg.append(START_BYTE)
    msg.append(len(payload) + 3)
    msg.append(BOARD_ID)
    msg.append(receiver)
    msg.append(msg_type)
    msg.extend(payload)
    msg.append(END_BYTE)
    uart2.write(msg)

def send_ack(msg_type, value=0):
    payload = bytearray([msg_type, value & 0xFF])
    send_message(5, BROADCAST_ID, payload)

#  MESSAGE PROCESS
def process_uart():
    global uart_buffer, v, debug_mode, active_bus

    if uart2.any():
        uart_buffer.extend(uart2.read())

    if len(uart_buffer) > 256:
        uart_buffer = bytearray()

    while True:
        if START_BYTE not in uart_buffer:
            uart_buffer.clear()
            return

        start = uart_buffer.index(START_BYTE)

        if len(uart_buffer) < start + 5:
            return

        length = uart_buffer[start + 1]

        if length > MAX_MSG_LEN:
            uart_buffer.pop(start)
            continue

        if len(uart_buffer) < start + length + 3:
            return

        end_index = start + length + 2

        if uart_buffer[end_index] != END_BYTE:
            uart_buffer.pop(start)
            continue

        msg = uart_buffer[start:end_index+1]
        uart_buffer = uart_buffer[end_index+1:]

        sender = msg[2]
        receiver = msg[3]
        msg_type = msg[4]
        payload = msg[5:-1]

        # Ignore own
        if sender == BOARD_ID:
            continue

     
        if receiver != BOARD_ID and receiver != BROADCAST_ID:
            uart2.write(msg)
            continue

      
        if msg_type == 1:
            try:
                v = float(payload.decode())
                send_ack(1, int(v))
            except:
                pass

        elif msg_type == 2:
            debug_mode ^= 1
            send_ack(2, debug_mode)

        elif msg_type == 4:
            active_bus ^= 1
            send_ack(4, active_bus)

        elif receiver == BROADCAST_ID:
            uart2.write(msg)

# MAIN LOOP 
print("SYSTEM RUNNING")

while True:
    now = time.ticks_ms()

    # ---------- UART ----------
    process_uart()

    #  BUS BUTTON 
    bb = bus_button.value()
    if last_bus_button == 1 and bb == 0:
        active_bus ^= 1
        if previous_bus == 1 and active_bus == 0:
            set_servo_logical(servo_a, 0)
            set_servo_logical(servo_b, 0)
        previous_bus = active_bus
        time.sleep(0.25)
    last_bus_button = bb

    # DEBUG 
    db = debug_button.value()
    if last_debug == 1 and db == 0:
        debug_mode ^= 1
        time.sleep(0.25)
    last_debug = db

    current23 = debug_pin23.value()
    if last_debug23 == 0 and current23 == 1:
        debug_mode ^= 1
        time.sleep(0.25)
    last_debug23 = current23

    if debug_mode:
        debug_state ^= 1
        led_b0_36.value(debug_state)
        led_b1_36.value(debug_state)
        led_b0_40.value(not debug_state)
        led_b1_40.value(not debug_state)
        time.sleep(0.5)
        continue

    # ---------- NORMAL ----------
    led_b0_36.off()
    led_b0_40.off()
    led_b1_36.off()
    led_b1_40.off()

    if active_bus == 0:
        yaw = stabilize(0, ADDR_36, read_angle(i2c0, ADDR_36, led_b0_36))
        pitch = stabilize(0, ADDR_40, read_angle(i2c0, ADDR_40, led_b0_40))

        if yaw and pitch:
            dt = time.ticks_diff(now, last_time)/1000
            last_time = now
            x += v * math.cos(math.radians(pitch)) * math.cos(math.radians(yaw)) * dt
            y += v * math.cos(math.radians(pitch)) * math.sin(math.radians(yaw)) * dt
            z += v * math.sin(math.radians(pitch)) * dt

        msg = "{:.2f},{:.2f},{:.2f},{:.2f}".format(x,y,z,v)
        send_message(3, BROADCAST_ID, msg.encode())

    else:
        yaw = stabilize(1, ADDR_36, read_angle(i2c1, ADDR_36, led_b1_36))
        pitch = stabilize(1, ADDR_40, read_angle(i2c1, ADDR_40, led_b1_40))

        if yaw is not None:
            set_servo_logical(servo_a, sensor_to_servo(yaw))
        if pitch is not None:
            set_servo_logical(servo_b, sensor_to_servo(pitch))

    time.sleep(0.6)
