# automatically generated by the FlatBuffers compiler, do not modify

# namespace: CustomAppProto

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ResponseContents(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ResponseContents()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsResponseContents(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # ResponseContents
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ResponseContents
    def ResponseType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

def ResponseContentsStart(builder):
    builder.StartObject(1)

def Start(builder):
    ResponseContentsStart(builder)

def ResponseContentsAddResponseType(builder, responseType):
    builder.PrependInt8Slot(0, responseType, 0)

def AddResponseType(builder, responseType):
    ResponseContentsAddResponseType(builder, responseType)

def ResponseContentsEnd(builder):
    return builder.EndObject()

def End(builder):
    return ResponseContentsEnd(builder)