from socket import *
from  time import ctime

HOST =  ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST,PORT)

tcpSerSock = socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
	print('等待连接')
	tcpCliSock,addr = tcpSerSock.accept()
	print(tcpSerSock)
	print('连接来自',addr)

	while True:
		data = tcpCliSock.recv(BUFSIZ)
		if not data:
			break
		# print(data.decode('utf-8'))
		d = data.decode('utf-8')
		print(d)
		print(bytes(d,'utf-8'))
		print(ctime())
		# c = data.encode('utf-8')
		tcpCliSock.send((ctime()).encode('utf-8'))

	tcpCliSock.close()
tcpSerSock.close()
