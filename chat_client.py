from socket import *

serverHost = "localhost"
serverPort = 50009

sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.connect((serverHost, serverPort))

while True:
	msg = input("Você: ")
	sockobj.send(bytes(msg, 'utf-8'))
	hmsg = sockobj.recv(1024)
	print ("Ele: ", str(hmsg, 'utf-8'))
	
