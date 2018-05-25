from w1thermsensor import W1ThermSensor

container_temp = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20,"0000046654e4")
ambient_temp = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20,"000005fafed1")

print("container_temp has temp of %.2f" % container_temp.get_temperature(W1ThermSensor.DEGREES_F))
print("ambiet_temp has temp of %.2f" % ambient_temp.get_temperature(W1ThermSensor.DEGREES_F))
