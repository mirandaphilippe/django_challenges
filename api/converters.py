from datetime import datetime

class DataConverter:
    regex = '[0-9]{2}-[0-9]{2}-[0-9]{4}'

    def to_python(self, value):
        return datetime.strptime(value, '%d-%m-%Y')

    def from_json(self, value):
        return datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%fZ')
    
    def kelvin_to_celcius(self, value):
        return value - 273.15