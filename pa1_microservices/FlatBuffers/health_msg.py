from typing import List
from enum import IntEnum
from dataclasses import dataclass


# Define the enumeration for DispenserOptions
class DispenserOptions(IntEnum):
    OPTIMAL = 0
    PARTIAL = 1
    BLOCKAGE = 2

# Define the enumeration for LightStatus
class LightStatus(IntEnum):
    GOOD = 0
    BAD = 1

# Define the enumeration for SensorStatus
class SensorStatus(IntEnum):
    GOOD = 0
    BAD = 1


@dataclass
class HealthBody:
    dispenser: DispenserOptions
    icemaker: int
    lightbulb: LightStatus
    fridge_temp: int
    freezer_temp: int
    sensor_status: SensorStatus
    humidity: float
    door_openings: int

    def __init__ (self):
        pass

    def dump (self):
        print ("Dumping contents of Health Message")
        print ("  Contents: {}".format (self))