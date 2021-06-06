import Adafruit_DHT
import time
import datetime

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4
DHT_LOG = "LOG_DHT11.txt"
LOG_FILE = open(DHT_LOG, "w")
DATE = str(datetime.date.today())
a = str("\n")
LOG_FILE.write(DATE)
LOG_FILE.write(a)
while True:
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        print("Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature,humidity)) #Printing data
        LOG = [time.strftime("%H:%M  "), "Temp={0:0.1f}C Humidity={1:0.1f}\n".format(temperature,humidity)]
        LOG_FILE.writelines(LOG) #Wiriting to file
    else:
        print("Sensor failture. Check wiring.");
    time.sleep(1); # Set time each every data read (sec)
