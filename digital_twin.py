class DigitalTwin:

    def __init__(self):
        self.temperature = 0
        self.rpm = 0
        self.load = 0
        self.vibration = 0

    def update(self, temp, rpm, load, vibration):
        self.temperature = temp
        self.rpm = rpm
        self.load = load
        self.vibration = vibration

    def state(self):
        return {
            "temperature": self.temperature,
            "rpm": self.rpm,
            "load": self.load,
            "vibration": self.vibration
        }