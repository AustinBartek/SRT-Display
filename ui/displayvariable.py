import value_reader

class DisplayVariable:
    def __init__(self, name, getter):
        self.name = name
        self.getter = getter

    def get_value(self):
        return self.getter()

def get_rpm():
    v
RPM = DisplayVariable("RPM", )