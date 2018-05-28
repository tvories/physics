# from w1thermsensor import W1ThermSensor
import datetime
import random
from .Temp import Temp
import csv
from time import sleep
from .__main__ import generate

# Define sensors
# sensors = []
# container_temp = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20,"0000046654e4")
# ambient_temp = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20,"000005fafed1")

# sensors.append(container_temp)
# sensors.append(ambient_temp)

def record_temps(temp_list):
    # place holder until sensors are hooked up
    while True:
        try:
            temp_list.append(create_random_temp())
            sleep(2)
        except KeyboardInterrupt:
            return temp_list
            pass

def create_random_temp():
    sensor = "DEMO-SENSOR"
    timestamp = datetime.datetime.now()
    temp_c = random.randint(15,75)

    return Temp(sensor, timestamp, temp_c)

def export_temp_csv(file_name, temp_list):
    # This function exports a list of temperatures to a csv file
    # It expects a temperature object
    with open(file_name, 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(['Sensor', 'Time', 'Temp_C', 'Temp_F'])

        # iterate through list
        for temp in temp_list:
            csv_format = temp.to_csv()
            writer.writerow(csv_format)