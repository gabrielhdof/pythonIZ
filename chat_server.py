from socket import *

meuHost = ""
minhaPort = 50009

sockobj = socket(AF_INET, SOCK_STREAM)

sockobj.bind((meuHost, minhaPort))
sockobj.listen(5)

while True:
	conexão, endereço = sockobj.accept()
	print ("Server conectado por: ", endereço)
	
	while True:
		
		msg = conexão.recv(1024)
		
		if not msg: break
		
		print ("Ele: ", str(msg, 'utf-8'))
		ymsg = input("Vocẽ: ")
		conexão.send(bytes(ymsg, 'utf-8'))
