# automatically generated by the FlatBuffers compiler, do not modify

# namespace: CustomAppProto

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class Master(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Master()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsMaster(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # Master
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Master
    def Type(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

    # Master
    def Ts(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float64Flags, o + self._tab.Pos)
        return 0.0

    # Master
    def BodyType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # Master
    def Body(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            from flatbuffers.table import Table
            obj = Table(bytearray(), 0)
            self._tab.Union(obj, o)
            return obj
        return None

def MasterStart(builder):
    builder.StartObject(4)

def Start(builder):
    MasterStart(builder)

def MasterAddType(builder, type):
    builder.PrependInt8Slot(0, type, 0)

def AddType(builder, type):
    MasterAddType(builder, type)

def MasterAddTs(builder, ts):
    builder.PrependFloat64Slot(1, ts, 0.0)

def AddTs(builder, ts):
    MasterAddTs(builder, ts)

def MasterAddBodyType(builder, bodyType):
    builder.PrependUint8Slot(2, bodyType, 0)

def AddBodyType(builder, bodyType):
    MasterAddBodyType(builder, bodyType)

def MasterAddBody(builder, body):
    builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(body), 0)

def AddBody(builder, body):
    MasterAddBody(builder, body)

def MasterEnd(builder):
    return builder.EndObject()

def End(builder):
    return MasterEnd(builder)
