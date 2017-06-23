import socket
from math import sqrt

Host = 'localhost'
Porta = 2002

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((Host, Porta))

while True:
	mensagem, cliente = s.recvfrom(2048)
	mensagem = mensagem.decode("utf-8")
	mensagemsp = mensagem.split(" ")
	if mensagemsp[0] == "sair":
		break
	else:
		if mensagemsp[0] == "soma":
			teste = len(mensagemsp)
			if teste == 4:
				soma = int(mensagemsp[1]) + int(mensagemsp[2])
				soma = str(soma)
				soma = soma.encode("utf-8")
				s.sendto(soma, cliente)
			else:
				erro="mensagem invalida"
				erro = erro.encode("utf-8")
				s.sendto(erro, cliente)
		elif mensagemsp[0] == "raiz_quadrada":
			teste = len(mensagemsp)
			if teste == 3:
				raiz = sqrt(int(mensagemsp[1]))
				raiz = str(raiz)
				raiz = raiz.encode("utf-8")
				s.sendto(raiz, cliente)
			else:
				erro="mensagem invalida"
				erro = erro.encode("utf-8")
				s.sendto(erro, cliente)
		else:
			erro1 = "Mensagem invalida"
			erro1 = erro1.encode("utf-8")
			s.sendto(erro1, cliente)

s.close()