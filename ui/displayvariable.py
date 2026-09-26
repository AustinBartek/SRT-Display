import data.ecu as ecu

class DisplayVariable:
    def __init__(self, name, getter):
        self.name = name
        self.getter = getter

    def get_value(self):
        return self.getter()

reader = ecu.ECUReader()

def get_rpm():
    reader.get_rpm()

RPM = DisplayVariable("RPM", get_rpm)

print(RPM.get_value())