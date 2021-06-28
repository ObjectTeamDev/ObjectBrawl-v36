class Writer:
    def __init__(self, client, endian: str = 'big'):
        self.client = client
        self.endian = endian
        self.buffer = b''
        self.bitIDX = 0

    def writeInt(self, data, length=4):
        self.bitIDX = 0
        self.buffer += data.to_bytes(length, 'big')

    def writeUInteger(self, integer: int, length: int = 1):
        self.bitIDX = 0
        self.buffer += integer.to_bytes(length, self.endian, signed=False)
    
    def writeArrayVint(self, data):
        self.bitIDX = 0
        for x in data:
            self.writeVInt(x)

    def writeUInt8(self, integer: int):
        self.bitIDX = 0
        self.writeUInteger(integer)

    def writeBool(self, boolean: bool):
        self.bitIDX = 0
        if boolean:
            self.writeUInt8(1)
        else:
            self.writeUInt8(0)

    def writeHexa(self, data):
        self.bitIDX = 0
        if data:
            if data.startswith('0x'):
                data = data[2:]

            self.buffer += bytes.fromhex(''.join(data.split()).replace('-', ''))

    def send(self):
        self.encode()
        packet = self.buffer
        self.buffer = b'';
        if self.id != 20100:
            self.buffer += bytes.fromhex("FFFF0000000000")
        self.buffer += self.id.to_bytes(2, 'big', signed=True)
        self.writeInt(len(packet), 3)
        if hasattr(self, 'version'):
            self.writeInt16(self.version)
        else:
            self.writeInt16(0)
        self.buffer += packet
        
        self.client.send(self.buffer)

    def writeVInt(self, data, rotate: bool = True):
        self.bitIDX = 0
        final = b''
        if data == 0:
            self.writeByte(0)
        else:
            data = (data << 1) ^ (data >> 31)
            while data:
                b = data & 0x7f

                if data >= 0x80:
                    b |= 0x80
                if rotate:
                    rotate = False
                    lsb = b & 0x1
                    msb = (b & 0x80) >> 7
                    b >>= 1
                    b = b & ~0xC0
                    b = b | (msb << 7) | (lsb << 6)

                final += b.to_bytes(1, 'big')
                data >>= 7
        self.buffer += final

    def writeString(self, string: str = None):
        self.bitIDX = 0
        if string is None:
            self.writeInt((2**32)-1)
        else:
            encoded = string.encode('utf-8')
            self.writeInt(len(encoded))
            self.buffer += encoded

    def writeByte(self, data):
        self.bitIDX = 0
        self.writeInt(data, 1)

    def writeInt16(self, data):
        self.bitIDX = 0
        self.writeInt(data, 2)

    def writeDataReference(self, csv, value):
        self.bitIDX = 0
        self.writeVInt(csv)
        self.writeVInt(value)
    
    def writeBoolean(self, value): #EXPERIMENTAL
        if self.bitIDX == 0:
            if value:
                self.writeByte(1)
            else:
                self.writeByte(0)
            self.bitIDX = 1
