from socket import *

serverHost = 'localhost'
serverPort = 50007

mensagem = [b'Ola mundo da internet!']

sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.connect((serverHost, serverPort))

for linha in mensagem:
	sockobj.send(linha)
	
	data = sockobj.recv(1024)
	print ("CLiente recebeu:", data)
