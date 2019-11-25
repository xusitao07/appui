#coding = utf-8
import socket,sys
serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
port = 8989
serversocket.bind((host,port))
serversocket.listen(5)

while True:
    clientsocket,addr = serversocket.accept()
    print("链接地址：%s"%str(addr))
    msg = "欢迎访问菜鸟教程"+"\r\n"
    clientsocket.send(msg.encode(("utf-8")))
    clientsocket.close()