from socket import *

HOST = '127.0.0.1'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST,PORT)

tcpCliSock = socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
	data = (input('请输入：')).encode('utf-8')
	if not data:
		break
	tcpCliSock.send(data)
	c = tcpCliSock.recv(BUFSIZ)
	if not data:
		break
	# print(data.decode('utf-8'))
	print(c.decode('utf-8'))
tcpCliSock.close()