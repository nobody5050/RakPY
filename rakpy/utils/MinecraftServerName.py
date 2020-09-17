class MinecraftServerName:
    edition = ""
    motd = ""
    name = ""
    protocol = 0
    version = ""
    players = {
        "online": 0,
        "max": 0
    }
    gamemode = ""
    serverId = 0
    
    def toString(self):
        return ";".join([
            self.edition,
            self.motd,
            self.protocol,
            self.version,
            self.players["online"],
            self.players["max"],
            self.serverId,
            self.name,
            self.gamemode
        ]) + ";"
