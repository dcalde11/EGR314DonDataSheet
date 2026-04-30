from machine import Pin, SoftI2C, UART
import time

# ================= LED SETUP =================
leds = [
    Pin(4, Pin.OUT),  # LED0 TX
    Pin(5, Pin.OUT),  # LED1 RX
    Pin(6, Pin.OUT),  # LED2 SENSOR OK
    Pin(7, Pin.OUT)   # LED3 ERROR
]

# ================= I2C SETUP =================
i2c = SoftI2C(scl=Pin(35), sda=Pin(36), freq=100000)
ADDR = 0x36

# ================= UART SETUP =================
uart = UART(2, baudrate=9600, tx=Pin(38), rx=Pin(10))

# ================= CONFIG =================
my_id = b'D'
MAX_MESSAGE_LEN = 64

# ================= SENSOR VALUE =================
current_angle = 0.0

# ================= SENSOR TIMING =================
last_sensor_read = 0
SENSOR_INTERVAL_MS = 100  # 10 Hz

# ================= LED HELPERS =================
def leds_off():
    for l in leds:
        l.value(0)

def led_tx():
    leds[0].value(1)
    time.sleep(0.05)
    leds[0].value(0)

def led_rx():
    leds[1].value(1)
    time.sleep(0.05)
    leds[1].value(0)

def led_sensor_ok(state):
    leds[2].value(1 if state else 0)

def led_error(state):
    leds[3].value(1 if state else 0)

# ================= SENSOR CHECK =================
def check_sensor():
    return ADDR in i2c.scan()

sensor_ok = check_sensor()
led_sensor_ok(sensor_ok)

# ================= UART SEND =================
def send_message(sender, receiver, payload):
    frame = b'AZ' + sender + receiver + payload + b'YB'

    led_tx()  # TX indicator
    uart.write(frame)

    print("TX FRAME:", frame)

# ================= MESSAGE HANDLER =================
def handle_message(frame):
    global current_angle

    if len(frame) < 5:
        return

    if frame[:2] != b'AZ' or frame[-2:] != b'YB':
        return

    sender = frame[2:3]
    receiver = frame[3:4]
    payload = frame[4:-2]

    print("RX FRAME:", frame)

    # RX indicator
    led_rx()

    if receiver != my_id:
        return

    # ================= RELAY LOGIC =================
    if sender == b'G':
        word = payload

        angle_str = "{:.2f}".format(current_angle)
        combined = word + b'|' + angle_str.encode()

        send_message(my_id, b'E', combined)

# ================= UART BUFFER =================
buffer = b''

# ================= MAIN LOOP =================
while True:

    # -------- UART RECEIVE --------
    if uart.any():
        data = uart.read()
        if data:
            buffer += data

            if len(buffer) > MAX_MESSAGE_LEN:
                buffer = b''

            if b'AZ' in buffer and b'YB' in buffer:
                try:
                    start = buffer.index(b'AZ')
                    end = buffer.index(b'YB') + 2
                    frame = buffer[start:end]

                    handle_message(frame)

                    buffer = buffer[end:]

                except:
                    buffer = b''

    # -------- SENSOR STATUS --------
    sensor_ok = check_sensor()
    led_sensor_ok(sensor_ok)
    led_error(not sensor_ok)

    if not sensor_ok:
        continue

    # -------- SLOW SENSOR READ (10 Hz) --------
    now = time.ticks_ms()

    if time.ticks_diff(now, last_sensor_read) > SENSOR_INTERVAL_MS:
        last_sensor_read = now

        try:
            data = i2c.readfrom_mem(ADDR, 0x0C, 2)
            raw = ((data[0] << 8) | data[1]) & 0x0FFF
            angle = raw * 360.0 / 4096.0

            current_angle = angle

            print("Angle:", angle)

        except Exception as e:
            print("Sensor error:", e)
            led_error(True)