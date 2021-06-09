#Before you start it is necesary to install Adafruit library and rest below

import Adafruit_DHT
import time
import datetime

#Chose model of your sensor and to which pin it is connected

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4
LOG_FILE = open("LOG.txt", "+a")
LOG_Title = ["\tDate of measurment : ", str(datetime.date.today()), "\n"]
LOG_FILE.writelines(LOG_Title)

while True:
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        print(time.strftime("%H:%M:%S"),f": Temp = {temperature}C // Humidity = {humidity}%") #Printing data
        LOG = [time.strftime("%H:%M:%S"),f": Temp = {temperature}C // Humidity = {humidity}\n"]
        LOG_FILE.writelines(LOG) #Writing data to LOG file
    else:
        print("Sensor failture. Check wiring.");
    time.sleep(3); # Set time each every data read (sec)
