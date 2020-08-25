import time as t
from rakpy.BitStream import BitStream
from rakpy.protocol.ConnectedPing import ConnectedPing
from rakpy.protocol.ConnectedPong import ConnectedPong
from rakpy.protocol.UnconnectedPing import UnconnectedPing
from rakpy.protocol.UnconnectedPingOpenConnection import UnconnectedPingOpenConnection
from rakpy.protocol.UnconnectedPong import UnconnectedPong
from rakpy.ServerSocket import ServerSocket

class Server:
    address = None
    startTime = None
    
    options = {
                  "name": "",
                  "custom_handler": lambda data, address, socket: 0,
                  "custom_packets": [0x80]
              }

    def __init__(self, address):
        self.address = address
        
    def setOption(self, name, value):
        self.options[name] = value

    def getPID(self, data):
        return data[0]
    
    def sendPacket(self, pk, address):
        pk.encode()
        buffer = BitStream.getBuffer()
        ServerSocket.putPacket(self, buffer, address)
        
    def sendRawPacket(self, pk, address):
        pk.encode()
        BitStream.buffer = bytes([pk.PID]) + BitStream.getBuffer()
        buffer = BitStream.getBuffer()
        ServerSocket.putPacket(self, buffer, address)
    
    def handle(self, data, address):
        pid = self.getPID(data)
        pk = None
        if pid == UnconnectedPing.PID or pid == UnconnectedPingOpenConnection.PID:
            pk = UnconnectedPong()
            pk.time = int(t.time() - self.startTime)
            pk.serverID = int.from_bytes(b"\x10\x00\x10\x00\x10\x00\x10\x00", "big")
            pk.serverIDString = self.options["name"]
            self.sendRawPacket(pk, address)

    def run(self):
        sock = ServerSocket(self.address)
        self.socket = sock.socket
        self.startTime = t.time()
        while True:
            if sock.getPacket() != None:
                data, address = sock.getPacket()
                self.handle(data, address)
