import socket
def ip():
  ip = socket.gethostbyname(socket.gethostname())
  return ip
