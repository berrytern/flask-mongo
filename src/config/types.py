#validation try
import pickle
from bson.binary import Binary, USER_DEFINED_SUBTYPE
from bson.codec_options import CodecOptions
def BinaryType(value):
    return Binary(pickle.dumps(value), USER_DEFINED_SUBTYPE)
class PickledBinaryDecoder(TypeDecoder):
    bson_type = Binary
    def transform_bson(self, value):
        if value.subtype == USER_DEFINED_SUBTYPE:
            return pickle.loads(value)
        return value
class StringType(object):
    def __init__(self, value):
        self.__value = value
    def __repr__(self):
        return "StringType('%s')" % (self.__value,)

class NumberType(object):
    def __init__(self, value):
        self.__value = value
    def __repr__(self):
        return "NumberType()"

