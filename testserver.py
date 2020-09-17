from rakpy.Server import Server
from rakpy.utils.InternetAddress import InternetAddress

server = Server(InternetAddress("0.0.0.0", 19132))
server.setOption("name", "MCPE;My server;407;1.16.0;0;0;0;MyServer;0")
server.run()
