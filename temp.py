import Adafruit_DHT
import time
import csv
import math
from datetime import datetime
from ADCDevice import *
adc = ADCDevice()
dht = Adafruit_DHT.DHT11
gpio = 17
def get_temp(pin):
    value = adc.analogRead(pin)
    voltage = value / 255.0 * 3.3
    Rt = 10 * voltage / (3.3 - voltage)
    tempK = 1/(1/(273.15 + 25) + math.log(Rt/10)/3950.0)
    temp = tempK - 273.15
    return temp
def setup():
    global adc
    if adc.detectI2C(0x4b):
        adc = ADS7830()
    else:
        print('No device found')
        raise SystemExit
def loop():
    pre_time = 0
    with open('temps.csv','w',newline='') as file:
        w = csv.writer(file)
        w.writerow(['time','temperature','humidity'])
        print('starting')
        while True:
            now = datetime.now()
            time = datetime.strftime(now,'%H:%M')
            if time != pre_time:
                pre_time = time
                temp1 = get_temp(0)
                temp2 = get_temp(1)
                humidity, temp3 = Adafruit_DHT.read_retry(dht,gpio)
                temp = round((temp1 + temp2 + temp3) / 3)
                w.writerow([time,temp,humidity])
                print(time)
def destroy():
    adc.close()
if __name__ == '__main__':
    print('Program is starting...')
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
