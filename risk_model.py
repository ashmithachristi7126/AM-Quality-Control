from config import *

def calculate_defect_risk(temp, rpm, load, vibration):

    risk = 0

    if temp > TEMP_MAX:
        risk += 30

    if vibration >= VIBRATION_LIMIT:
        risk += 25

    if rpm > RPM_MAX:
        risk += 20

    if load > LOAD_MAX:
        risk += 25

    return risk
def machine_health_score(risk):

    health = 100 - risk

    if health < 0:
        health = 0

    return health