import struct

class Boh:
    size = 3

    def __init__(self, value1=None, value2=None, ):
        self.value1 = value1
        self.value2 = value2

    def from_binary(self, data):
        if len(data) < self.size:
           raise ValueError(f'Insufficient data for {self.__class__.__name__}') 
        self.value1 = struct.unpack('<?', data[0:1])[0]
        self.value2 = struct.unpack('<H', data[1:3])[0]

    def to_binary(self):
        data = bytearray()
        data += struct.pack('<?', self.value1)
        data += struct.pack('<H', self.value2)
        return data

    def values(self):
        return (
            self.value1,
            self.value2,
        )
class Test:
    size = 46

    def __init__(self, value1=None, value2=None, value3=None, value4=None, value5=None, value7=None, value6=None, value8=None, value9=None, value10=None, value11=None, value12=None, ):
        self.value1 = value1
        self.value2 = value2
        self.value3 = value3
        self.value4 = value4
        self.value5 = value5
        self.value7 = value7
        self.value6 = value6
        self.value8 = value8
        self.value9 = value9
        self.value10 = value10
        self.value11 = value11
        self.value12 = value12

    def from_binary(self, data):
        if len(data) < self.size:
           raise ValueError(f'Insufficient data for {self.__class__.__name__}') 
        self.value1 = struct.unpack('<?', data[0:1])[0]
        self.value2 = struct.unpack('<H', data[1:3])[0]
        self.value3 = struct.unpack('<h', data[3:5])[0]
        self.value4 = struct.unpack('<B', data[5:6])[0]
        self.value5 = struct.unpack('<b', data[6:7])[0]
        self.value7 = struct.unpack('<I', data[7:11])[0]
        self.value6 = struct.unpack('<i', data[11:15])[0]
        self.value8 = struct.unpack('<Q', data[15:23])[0]
        self.value9 = struct.unpack('<q', data[23:31])[0]
        self.value10 = struct.unpack('<f', data[31:35])[0]
        self.value11 = struct.unpack('<d', data[35:43])[0]
        self.value12 = Boh()
        self.value12.from_binary(data[43:46]) 

    def to_binary(self):
        data = bytearray()
        data += struct.pack('<?', self.value1)
        data += struct.pack('<H', self.value2)
        data += struct.pack('<h', self.value3)
        data += struct.pack('<B', self.value4)
        data += struct.pack('<b', self.value5)
        data += struct.pack('<I', self.value7)
        data += struct.pack('<i', self.value6)
        data += struct.pack('<Q', self.value8)
        data += struct.pack('<q', self.value9)
        data += struct.pack('<f', self.value10)
        data += struct.pack('<d', self.value11)
        data += self.value12.to_binary()
        return data

    def values(self):
        return (
            self.value1,
            self.value2,
            self.value3,
            self.value4,
            self.value5,
            self.value7,
            self.value6,
            self.value8,
            self.value9,
            self.value10,
            self.value11,
            self.value12,
        )
