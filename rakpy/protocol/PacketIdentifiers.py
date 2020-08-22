class PacketIdentifiers:
    UnconnectedPing = 0x01
    UnconnectedPingOpenConnection = 0x02
    UnconnectedPong = 0x1c
    ConnectedPing = 0x00
    ConnectedPong = 0x03
    OpenConnectionRequest1 = 0x05
    OpenConnectionReply1 = 0x06
    OpenConnectionRequest2 = 0x07
    OpenConnectionReply2 = 0x08
    ConnectionRequest = 0x09
    ConnectionRequestAccepted = 0x10
    IncompatibleProtocol = 0x19
    GamePacket = 0x8e
    NACK = 0xa0
    ACK = 0xc0
