# automatically generated by the FlatBuffers compiler, do not modify

# namespace: CustomAppProto

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class Milk(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Milk()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsMilk(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # Milk
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Milk
    def Type(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

    # Milk
    def Quantity(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float64Flags, o + self._tab.Pos)
        return 0.0

def MilkStart(builder):
    builder.StartObject(2)

def Start(builder):
    MilkStart(builder)

def MilkAddType(builder, type):
    builder.PrependInt8Slot(0, type, 0)

def AddType(builder, type):
    MilkAddType(builder, type)

def MilkAddQuantity(builder, quantity):
    builder.PrependFloat64Slot(1, quantity, 0.0)

def AddQuantity(builder, quantity):
    MilkAddQuantity(builder, quantity)

def MilkEnd(builder):
    return builder.EndObject()

def End(builder):
    return MilkEnd(builder)
