# automatically generated by the FlatBuffers compiler, do not modify

# namespace: CustomAppProto

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ResponseBody(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ResponseBody()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsResponseBody(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # ResponseBody
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ResponseBody
    def Code(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

    # ResponseBody
    def Contents(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

def ResponseBodyStart(builder):
    builder.StartObject(2)

def Start(builder):
    ResponseBodyStart(builder)

def ResponseBodyAddCode(builder, code):
    builder.PrependInt8Slot(0, code, 0)

def AddCode(builder, code):
    ResponseBodyAddCode(builder, code)

def ResponseBodyAddContents(builder, contents):
    builder.PrependInt8Slot(1, contents, 0)

def AddContents(builder, contents):
    ResponseBodyAddContents(builder, contents)

def ResponseBodyEnd(builder):
    return builder.EndObject()

def End(builder):
    return ResponseBodyEnd(builder)
