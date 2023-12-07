from typing import List
from enum import Enum
from dataclasses import dataclass


# Define the enumeration for MilkType
class MilkType(Enum):
    OnePercent = 0
    TwoPercent = 1
    FatFree = 2
    Whole = 3
    Almond = 4
    Cashew = 5
    Oat = 6

# Define the enumeration for BreadType
class BreadType(Enum):
    WholeWheat = 0
    Pumpernickel = 1
    Rye = 2
    White = 3
    Sourdough = 4

# Define the enumeration for MeatType
class MeatType(Enum):
    GroundBeef = 0
    Chicken = 1
    Turkey = 2
    Ham = 3
    Pork = 4
    Steak = 5

# Define the data classes
@dataclass
class VeggieOrder:
    tomato: float
    cucumber: float
    eggplant: float
    broccoli: float
    carrot: float
    onion: float

    def __init__ (self):
        pass

@dataclass
class CanOrder:
    coke: int
    pepsi: int
    coors: int

    def __init__ (self):
        pass

@dataclass
class BottleOrder:
    sprite: int
    rootbeer: int
    fanta: int

    def __init__ (self):
        pass

@dataclass
class CansAndBottles:
    cans: CanOrder
    bottles: BottleOrder

    def __init__ (self):
        pass

@dataclass
class Milk:
    type: MilkType
    quantity: float

@dataclass
class Bread:
    type: BreadType
    quantity: int

@dataclass
class Meat:
    type: MeatType
    quantity: float



@dataclass
class OrderBody:
    veggies: VeggieOrder
    drinks: CansAndBottles
    milk: List[Milk]
    bread: List[Bread]
    meat: List[Meat]

    def __init__ (self):
        pass

    def dump (self):
        print ("Dumping contents of Order Message")
        print ("  Contents: {}".format (self))
