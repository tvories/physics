# from w1thermsensor import W1ThermSensor
import datetime
import random
from .Temp import Temp
import csv
from time import sleep
import __main__


def record_temps(temp_list):
    # place holder until sensors are hooked up
    while True:
        try:
            if __main__.generate:
                temp_list.append(create_random_temp())
                sleep(2)
            else:
                for sensor in __main__.sensors:
                    temp_list.append(create_temp(sensor))
                sleep(2)

        except KeyboardInterrupt:
            return temp_list
            pass

def create_random_temp():
    sensor = "DEMO-SENSOR"
    timestamp = datetime.datetime.now()
    temp_c = random.randint(15,75)

    return Temp(sensor, timestamp, temp_c)

def create_temp(sensor):
    temp_c = sensor.get_temperature(W1ThermSensor.DEGREES_C)
    timestamp = datetime.datetime.now()
    sensor = sensor.name

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