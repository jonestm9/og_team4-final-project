# automatically generated by the FlatBuffers compiler, do not modify

# namespace: CustomAppProto

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class CansAndBottles(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = CansAndBottles()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsCansAndBottles(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # CansAndBottles
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # CansAndBottles
    def Cans(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from CustomAppProto.CanOrder import CanOrder
            obj = CanOrder()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # CansAndBottles
    def Bottles(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from CustomAppProto.BottleOrder import BottleOrder
            obj = BottleOrder()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

def CansAndBottlesStart(builder):
    builder.StartObject(2)

def Start(builder):
    CansAndBottlesStart(builder)

def CansAndBottlesAddCans(builder, cans):
    builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(cans), 0)

def AddCans(builder, cans):
    CansAndBottlesAddCans(builder, cans)

def CansAndBottlesAddBottles(builder, bottles):
    builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(bottles), 0)

def AddBottles(builder, bottles):
    CansAndBottlesAddBottles(builder, bottles)

def CansAndBottlesEnd(builder):
    return builder.EndObject()

def End(builder):
    return CansAndBottlesEnd(builder)
