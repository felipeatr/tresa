import socket

Host = 'localhost'
Porta = 2002

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
	mensagem = input("digite os paramentros para operação, EX: soma 1 2 / raiz_quadrada 9 / sair encerra o programa:")
	mensagemnl = mensagem + ' /n'
	smensagem = mensagemnl.encode('utf-8')
	s.sendto(smensagem, (Host, Porta))
	if mensagem == "sair":
		break
	else:
		resultado, serverAddress = s.recvfrom(2048)
		resultado = resultado.decode('utf-8')
		print (resultado)