from config import *

def automatic_correction(temp, rpm, load, vibration):

    actions = []

    if temp > TEMP_MAX:
        temp = TEMP_MAX
        actions.append("Reduce Heater Power")

    if rpm > RPM_MAX:
        rpm = RPM_MAX
        actions.append("Adjust Motor Speed")

    if load > LOAD_MAX:
        load = LOAD_MAX
        actions.append("Reduce Mechanical Load")

    if vibration >= VIBRATION_LIMIT:
        vibration = 0
        actions.append("Activate Vibration Stabilizer")

    return temp, rpm, load, vibration, actions