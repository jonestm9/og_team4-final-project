from typing import List
from enum import IntEnum
from dataclasses import dataclass



# Define the enumeration for RequestStatus
class RequestStatus(IntEnum):
    OK = 0
    BAD_REQUEST = 1

# Define the enumeration for ContentsStatus
class ResponseStatus(IntEnum):
    ORDER_PLACED = 0
    YOU_ARE_HEALTHY = 1
    BAD_REQUEST = 2

# Define the data class for Response
@dataclass
class ResponseBody:
    code: RequestStatus
    contents: ResponseStatus

    def __init__ (self):
        pass

    def dump (self):
        print ("Dumping contents of Response Message")
        print ("  Code: {}".format (self.code))
        print ("  Contents: {}".format (self.contents))