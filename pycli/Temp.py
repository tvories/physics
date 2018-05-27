class Temp():
    def __init__(self, sensor, timestamp, temp_c, temp_f):
        self.sensor = sensor
        self.timestamp = timestamp
        self.temp_c = temp_c
        self.temp_f = temp_f

    def get_temp(self):
        print('Sensor: {sensor}'.format(sensor = self.sensor))
        print('Time: {timestamp}'.format(timestamp = self.timestamp))
        print('Temp C: {temp_c}'.format(temp_c = self.temp_c))
        print('Temp F: {temp_f}'.format(temp_f = self.temp_f))
