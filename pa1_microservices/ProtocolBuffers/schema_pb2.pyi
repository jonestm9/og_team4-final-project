from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DispenserStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    DispenserStatus_Unspecified: _ClassVar[DispenserStatus]
    PARTIAL: _ClassVar[DispenserStatus]
    BLOCKAGE: _ClassVar[DispenserStatus]
    OPTIMAL: _ClassVar[DispenserStatus]

class SensorStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    SensorStatus_Unspecified: _ClassVar[SensorStatus]
    SENSOR_BAD: _ClassVar[SensorStatus]
    SENSOR_GOOD: _ClassVar[SensorStatus]

class LightbulbStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    LightbulbStatus_Unspecified: _ClassVar[LightbulbStatus]
    LIGHT_BAD: _ClassVar[LightbulbStatus]
    LIGHT_GOOD: _ClassVar[LightbulbStatus]

class ResponseCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    ResponseCode_Unspecified: _ClassVar[ResponseCode]
    BAD_REQUEST: _ClassVar[ResponseCode]
    OK: _ClassVar[ResponseCode]

class ContentsStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    ContentsStatus_Unspecified: _ClassVar[ContentsStatus]
    YOU_ARE_HEALTHY: _ClassVar[ContentsStatus]
    BAD_REQ: _ClassVar[ContentsStatus]
    ORDER_PLACED: _ClassVar[ContentsStatus]

class MsgType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    MsgType_Unspecified: _ClassVar[MsgType]
    ResponseType: _ClassVar[MsgType]
    OrderType: _ClassVar[MsgType]
    HealthType: _ClassVar[MsgType]
DispenserStatus_Unspecified: DispenserStatus
PARTIAL: DispenserStatus
BLOCKAGE: DispenserStatus
OPTIMAL: DispenserStatus
SensorStatus_Unspecified: SensorStatus
SENSOR_BAD: SensorStatus
SENSOR_GOOD: SensorStatus
LightbulbStatus_Unspecified: LightbulbStatus
LIGHT_BAD: LightbulbStatus
LIGHT_GOOD: LightbulbStatus
ResponseCode_Unspecified: ResponseCode
BAD_REQUEST: ResponseCode
OK: ResponseCode
ContentsStatus_Unspecified: ContentsStatus
YOU_ARE_HEALTHY: ContentsStatus
BAD_REQ: ContentsStatus
ORDER_PLACED: ContentsStatus
MsgType_Unspecified: MsgType
ResponseType: MsgType
OrderType: MsgType
HealthType: MsgType

class Health(_message.Message):
    __slots__ = ["dispenser", "icemaker", "lightbulb", "fridge_temp", "freezer_temp", "sensor_status", "humidity", "door_openings"]
    DISPENSER_FIELD_NUMBER: _ClassVar[int]
    ICEMAKER_FIELD_NUMBER: _ClassVar[int]
    LIGHTBULB_FIELD_NUMBER: _ClassVar[int]
    FRIDGE_TEMP_FIELD_NUMBER: _ClassVar[int]
    FREEZER_TEMP_FIELD_NUMBER: _ClassVar[int]
    SENSOR_STATUS_FIELD_NUMBER: _ClassVar[int]
    HUMIDITY_FIELD_NUMBER: _ClassVar[int]
    DOOR_OPENINGS_FIELD_NUMBER: _ClassVar[int]
    dispenser: DispenserStatus
    icemaker: int
    lightbulb: LightbulbStatus
    fridge_temp: int
    freezer_temp: int
    sensor_status: SensorStatus
    humidity: float
    door_openings: int
    def __init__(self, dispenser: _Optional[_Union[DispenserStatus, str]] = ..., icemaker: _Optional[int] = ..., lightbulb: _Optional[_Union[LightbulbStatus, str]] = ..., fridge_temp: _Optional[int] = ..., freezer_temp: _Optional[int] = ..., sensor_status: _Optional[_Union[SensorStatus, str]] = ..., humidity: _Optional[float] = ..., door_openings: _Optional[int] = ...) -> None: ...

class Response(_message.Message):
    __slots__ = ["code", "contents"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    CONTENTS_FIELD_NUMBER: _ClassVar[int]
    code: ResponseCode
    contents: ContentsStatus
    def __init__(self, code: _Optional[_Union[ResponseCode, str]] = ..., contents: _Optional[_Union[ContentsStatus, str]] = ...) -> None: ...

class VeggieOrder(_message.Message):
    __slots__ = ["tomato", "cucumber", "eggplant", "broccoli", "carrot", "onion"]
    TOMATO_FIELD_NUMBER: _ClassVar[int]
    CUCUMBER_FIELD_NUMBER: _ClassVar[int]
    EGGPLANT_FIELD_NUMBER: _ClassVar[int]
    BROCCOLI_FIELD_NUMBER: _ClassVar[int]
    CARROT_FIELD_NUMBER: _ClassVar[int]
    ONION_FIELD_NUMBER: _ClassVar[int]
    tomato: float
    cucumber: float
    eggplant: float
    broccoli: float
    carrot: float
    onion: float
    def __init__(self, tomato: _Optional[float] = ..., cucumber: _Optional[float] = ..., eggplant: _Optional[float] = ..., broccoli: _Optional[float] = ..., carrot: _Optional[float] = ..., onion: _Optional[float] = ...) -> None: ...

class CansAndBottles(_message.Message):
    __slots__ = ["cans", "bottles"]
    class CanOrder(_message.Message):
        __slots__ = ["coke", "pepsi", "coors"]
        COKE_FIELD_NUMBER: _ClassVar[int]
        PEPSI_FIELD_NUMBER: _ClassVar[int]
        COORS_FIELD_NUMBER: _ClassVar[int]
        coke: int
        pepsi: int
        coors: int
        def __init__(self, coke: _Optional[int] = ..., pepsi: _Optional[int] = ..., coors: _Optional[int] = ...) -> None: ...
    class BottleOrder(_message.Message):
        __slots__ = ["sprite", "rootbeer", "fanta"]
        SPRITE_FIELD_NUMBER: _ClassVar[int]
        ROOTBEER_FIELD_NUMBER: _ClassVar[int]
        FANTA_FIELD_NUMBER: _ClassVar[int]
        sprite: int
        rootbeer: int
        fanta: int
        def __init__(self, sprite: _Optional[int] = ..., rootbeer: _Optional[int] = ..., fanta: _Optional[int] = ...) -> None: ...
    CANS_FIELD_NUMBER: _ClassVar[int]
    BOTTLES_FIELD_NUMBER: _ClassVar[int]
    cans: CansAndBottles.CanOrder
    bottles: CansAndBottles.BottleOrder
    def __init__(self, cans: _Optional[_Union[CansAndBottles.CanOrder, _Mapping]] = ..., bottles: _Optional[_Union[CansAndBottles.BottleOrder, _Mapping]] = ...) -> None: ...

class Milk(_message.Message):
    __slots__ = ["type", "quantity"]
    class MilkType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        MilkType_Unspecified: _ClassVar[Milk.MilkType]
        OnePercent: _ClassVar[Milk.MilkType]
        TwoPercent: _ClassVar[Milk.MilkType]
        FatFree: _ClassVar[Milk.MilkType]
        Whole: _ClassVar[Milk.MilkType]
        Almond: _ClassVar[Milk.MilkType]
        Cashew: _ClassVar[Milk.MilkType]
        Oat: _ClassVar[Milk.MilkType]
    MilkType_Unspecified: Milk.MilkType
    OnePercent: Milk.MilkType
    TwoPercent: Milk.MilkType
    FatFree: Milk.MilkType
    Whole: Milk.MilkType
    Almond: Milk.MilkType
    Cashew: Milk.MilkType
    Oat: Milk.MilkType
    TYPE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    type: Milk.MilkType
    quantity: float
    def __init__(self, type: _Optional[_Union[Milk.MilkType, str]] = ..., quantity: _Optional[float] = ...) -> None: ...

class Bread(_message.Message):
    __slots__ = ["type", "quantity"]
    class BreadType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        BreadType_Unspecified: _ClassVar[Bread.BreadType]
        Pumpernickel: _ClassVar[Bread.BreadType]
        Rye: _ClassVar[Bread.BreadType]
        White: _ClassVar[Bread.BreadType]
        Sourdough: _ClassVar[Bread.BreadType]
        WholeWheat: _ClassVar[Bread.BreadType]
    BreadType_Unspecified: Bread.BreadType
    Pumpernickel: Bread.BreadType
    Rye: Bread.BreadType
    White: Bread.BreadType
    Sourdough: Bread.BreadType
    WholeWheat: Bread.BreadType
    TYPE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    type: Bread.BreadType
    quantity: int
    def __init__(self, type: _Optional[_Union[Bread.BreadType, str]] = ..., quantity: _Optional[int] = ...) -> None: ...

class Meat(_message.Message):
    __slots__ = ["type", "quantity"]
    class MeatType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        MeatType_Unspecified: _ClassVar[Meat.MeatType]
        Chicken: _ClassVar[Meat.MeatType]
        Turkey: _ClassVar[Meat.MeatType]
        Ham: _ClassVar[Meat.MeatType]
        Pork: _ClassVar[Meat.MeatType]
        Steak: _ClassVar[Meat.MeatType]
        GroundBeef: _ClassVar[Meat.MeatType]
    MeatType_Unspecified: Meat.MeatType
    Chicken: Meat.MeatType
    Turkey: Meat.MeatType
    Ham: Meat.MeatType
    Pork: Meat.MeatType
    Steak: Meat.MeatType
    GroundBeef: Meat.MeatType
    TYPE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    type: Meat.MeatType
    quantity: float
    def __init__(self, type: _Optional[_Union[Meat.MeatType, str]] = ..., quantity: _Optional[float] = ...) -> None: ...

class Order(_message.Message):
    __slots__ = ["veggies", "drinks", "milk", "bread", "meat"]
    VEGGIES_FIELD_NUMBER: _ClassVar[int]
    DRINKS_FIELD_NUMBER: _ClassVar[int]
    MILK_FIELD_NUMBER: _ClassVar[int]
    BREAD_FIELD_NUMBER: _ClassVar[int]
    MEAT_FIELD_NUMBER: _ClassVar[int]
    veggies: VeggieOrder
    drinks: CansAndBottles
    milk: _containers.RepeatedCompositeFieldContainer[Milk]
    bread: _containers.RepeatedCompositeFieldContainer[Bread]
    meat: _containers.RepeatedCompositeFieldContainer[Meat]
    def __init__(self, veggies: _Optional[_Union[VeggieOrder, _Mapping]] = ..., drinks: _Optional[_Union[CansAndBottles, _Mapping]] = ..., milk: _Optional[_Iterable[_Union[Milk, _Mapping]]] = ..., bread: _Optional[_Iterable[_Union[Bread, _Mapping]]] = ..., meat: _Optional[_Iterable[_Union[Meat, _Mapping]]] = ...) -> None: ...

class Master(_message.Message):
    __slots__ = ["type", "ts", "healthBody", "orderBody", "responseBody"]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TS_FIELD_NUMBER: _ClassVar[int]
    HEALTHBODY_FIELD_NUMBER: _ClassVar[int]
    ORDERBODY_FIELD_NUMBER: _ClassVar[int]
    RESPONSEBODY_FIELD_NUMBER: _ClassVar[int]
    type: MsgType
    ts: float
    healthBody: Health
    orderBody: Order
    responseBody: Response
    def __init__(self, type: _Optional[_Union[MsgType, str]] = ..., ts: _Optional[float] = ..., healthBody: _Optional[_Union[Health, _Mapping]] = ..., orderBody: _Optional[_Union[Order, _Mapping]] = ..., responseBody: _Optional[_Union[Response, _Mapping]] = ...) -> None: ...
