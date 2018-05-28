from w1thermsensor import W1ThermSensor

sensors = []
generate = False

ambient_temp = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20,"0000046654e4")
container_temp = ambient_temp = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20,"000005fafed1")
container_temp.name = "container_temp"
ambient_temp.name = "ambient_temp"

sensors.append(container_temp)
sensors.append(ambient_temp)