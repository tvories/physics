class Temp():
    def __init__(self, sensor, timestamp, temp_c):
        self.sensor = sensor
        self.timestamp = timestamp
        self.temp_c = temp_c
        self.temp_f = round((9.0/5.0 * temp_c + 32), 2)

    def get_temp(self):
        print('Sensor: {sensor}'.format(sensor = self.sensor))
        print('Time: {timestamp}'.format(timestamp = self.timestamp))
        print('Temp C: {temp_c}'.format(temp_c = self.temp_c))
        print('Temp F: {temp_f}'.format(temp_f = self.temp_f))

    def to_csv(self):
        return [self.sensor, self.timestamp.strftime("%Y-%m-%d %H:%M:%S"), self.temp_c, self.temp_f]
