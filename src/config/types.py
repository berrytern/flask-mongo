import pickle
from bson.binary import Binary, USER_DEFINED_SUBTYPE
def BinaryType(value):
    return Binary(pickle.dumps(value), USER_DEFINED_SUBTYPE)

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

