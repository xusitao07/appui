#coding = utf-8
import socket
import sys
soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
port = 8989
soc.connect((host,port))
msg= soc.recv(1024)
soc.close()
print(msg.decode("utf-8"))