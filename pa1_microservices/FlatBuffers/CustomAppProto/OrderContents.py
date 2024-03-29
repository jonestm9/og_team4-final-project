# automatically generated by the FlatBuffers compiler, do not modify

# namespace: CustomAppProto

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class OrderContents(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = OrderContents()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsOrderContents(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # OrderContents
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # OrderContents
    def Veggies(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from CustomAppProto.VeggieOrder import VeggieOrder
            obj = VeggieOrder()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # OrderContents
    def Drinks(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from CustomAppProto.CansAndBottles import CansAndBottles
            obj = CansAndBottles()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # OrderContents
    def Milk(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from CustomAppProto.Milk import Milk
            obj = Milk()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # OrderContents
    def MilkLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # OrderContents
    def MilkIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        return o == 0

    # OrderContents
    def Bread(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from CustomAppProto.Bread import Bread
            obj = Bread()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # OrderContents
    def BreadLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # OrderContents
    def BreadIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        return o == 0

    # OrderContents
    def Meat(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from CustomAppProto.Meat import Meat
            obj = Meat()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # OrderContents
    def MeatLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # OrderContents
    def MeatIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        return o == 0

def OrderContentsStart(builder):
    builder.StartObject(5)

def Start(builder):
    OrderContentsStart(builder)

def OrderContentsAddVeggies(builder, veggies):
    builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(veggies), 0)

def AddVeggies(builder, veggies):
    OrderContentsAddVeggies(builder, veggies)

def OrderContentsAddDrinks(builder, drinks):
    builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(drinks), 0)

def AddDrinks(builder, drinks):
    OrderContentsAddDrinks(builder, drinks)

def OrderContentsAddMilk(builder, milk):
    builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(milk), 0)

def AddMilk(builder, milk):
    OrderContentsAddMilk(builder, milk)

def OrderContentsStartMilkVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartMilkVector(builder, numElems: int) -> int:
    return OrderContentsStartMilkVector(builder, numElems)

def OrderContentsAddBread(builder, bread):
    builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(bread), 0)

def AddBread(builder, bread):
    OrderContentsAddBread(builder, bread)

def OrderContentsStartBreadVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartBreadVector(builder, numElems: int) -> int:
    return OrderContentsStartBreadVector(builder, numElems)

def OrderContentsAddMeat(builder, meat):
    builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(meat), 0)

def AddMeat(builder, meat):
    OrderContentsAddMeat(builder, meat)

def OrderContentsStartMeatVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartMeatVector(builder, numElems: int) -> int:
    return OrderContentsStartMeatVector(builder, numElems)

def OrderContentsEnd(builder):
    return builder.EndObject()

def End(builder):
    return OrderContentsEnd(builder)
