from abc import ABCMeta, abstractmethod

from rakpy.BitStream import BitStream

class Packet(BitStream):
    __metaclass__ = ABCMeta
    sendTime = None
    
    def encodeHeader(self):
        self.putByte(self.PID)
       
    @abstractmethod
    def encodePayload(self): pass
        
    def encode(self):
        self.reset()
        self.encodeHeader()
        self.encodePayload()
        
    @abstractmethod
    def decodePayload(self): pass
    
    def decodeHeader(self):
        return self.getByte()
    
    def decode(self):
        self.offset = 0
        self.decodeHeader()
        self.decodePayload()
    
    def clean(self):
        self.buffer = None
        self.offset = 0
        self.sendTime = None
