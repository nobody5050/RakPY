from rakpy.protocol.PacketIdentifiers import PacketIdentifiers
from rakpy.protocol.UnconnectedPing import UnconnectedPing

class UnconnectedPingOpenConnection(UnconnectedPing):
    PID = PacketIdentifiers.UnconnectedPingOpenConnection
