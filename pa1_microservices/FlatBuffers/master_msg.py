from typing import List
from enum import Enum, IntEnum
from dataclasses import dataclass
from health_msg import HealthBody
from order_msg import OrderBody
from response_msg import ResponseBody

class Types(IntEnum):
    HEALTH = 0
    ORDER = 1
    RESPONSE = 2


# Define the data class for Health
@dataclass
class Master:
    type: Types
    ts: float
    body: HealthBody | OrderBody | ResponseBody

    def __init__ (self):
        pass

    def dump (self):
        print ("Dumping contents of Health Message")
        print ("  Type: {}".format (self.type))
        print ("  Ts: {}".format (self.ts))
        print ("  Body: {}".format (self.body))
