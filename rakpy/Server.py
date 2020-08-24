class Server:
    def rawPacket(self, pid, packet):
        return bytes([pid]) + packet
    
    def getPID(self, data):
        return data[0]
    
    def handler(self, data, address):
        pid = getPID(data)
        pk = None
    
