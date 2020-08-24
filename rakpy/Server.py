from rakpy.BitStream import BitStream
from rakpy.protocol.ConnectedPing import ConnectedPing
from rakpy.protocol.ConnectedPong import ConnectedPong
from rakpy.protocol.UnconnectedPing import UnconnectedPing
from rakpy.protocol.UnconnectedPingOpenConnection import UnconnectedPingOpenConnection
from rakpy.protocol.UnconnectedPong import UnconnectedPong
from rakpy.ServerSocket import ServerSocket

class Server:
    def getPID(self, data):
        return data[0]
    
    def sendPacket(self, pk, address):
        pk.encode()
        buffer = BitStream.getBuffer()
        ServerSocket.putPacket(buffer, address)
        
    def sendRawPacket(self, pk, address):
        pk.encode()
        BitStream.buffer = ord(pk.PID) + BitStream.getBuffer()
        buffer = BitStream.getBuffer()
        ServerSocket.putPacket(buffer, address)
    
    def handle(self, data, address):
        pid = getPID(data)
        newPacket = None
        if pid == UnconnectedPing.PID or pid == UnconnectedPingOpenConnection.PID:
            pk = UnconnectedPong()
            pk.time = data[:8]
            pk.serverID = b"\x10\x00\x10\x00\x10\x00\x10\x00"
            pk.serverIDString = ""
            self.sendRawPacket(pk, address)
    
