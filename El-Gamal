import random 
from math import pow

# Gera um número aleatório entre 2 e 10 para ser utilizado como base do logaritmo discreto
a = random.randint(2, 10)

# Função para calcular o máximo divisor comum usando o algoritmo de Euclides
def mdc(a, b):
	if a < b:
		return mdc(b, a)
	elif a % b == 0:
		return b
	else:
		return mdc(b, a % b)

# Gera uma chave privada aleatória
def gerar_chave(q):
	chave = random.randint(pow(10, 20), q)
	while mdc(q, chave) != 1:
		chave = random.randint(pow(10, 20), q)
	return chave

# Função para realizar a exponenciação modular
def exponenciacao_modular(a, b, c):
	x = 1
	y = a

	while b > 0:
		if b % 2 != 0:
			x = (x * y) % c
		y = (y * y) % c
		b = int(b / 2)

	return x % c

# Função para realizar a criptografia assimétrica
def criptografar(mensagem, q, h, g):
	mensagem_encriptada = []

	k = gerar_chave(q) # Chave privada do remetente
	s = exponenciacao_modular(h, k, q)
	p = exponenciacao_modular(g, k, q)
	
	for i in range(0, len(mensagem)):
		mensagem_encriptada.append(mensagem[i])

	print("g^k usado : ", p)
	print("g^ak usado : ", s)
	for i in range(0, len(mensagem_encriptada)):
		mensagem_encriptada[i] = s * ord(mensagem_encriptada[i])

	return mensagem_encriptada, p

# Função para realizar a descriptografia
def descriptografar(mensagem_encriptada, p, chave, q):
	mensagem_descriptada = []
	h = exponenciacao_modular(p, chave, q)
	for i in range(0, len(mensagem_encriptada)):
		mensagem_descriptada.append(chr(int(mensagem_encriptada[i] / h)))
		
	return mensagem_descriptada

# Função principal
def principal():
	mensagem = 'criptografia'
	print("Mensagem Original:", mensagem)

	q = random.randint(pow(10, 20), pow(10, 50))
	g = random.randint(2, q)

	chave = gerar_chave(q) # Chave privada do receptor
	h = exponenciacao_modular(g, chave, q)
	print("g usado : ", g)
	print("g^a usado : ", h)

	mensagem_encriptada, p = criptografar(mensagem, q, h, g)
	mensagem_descriptada = descriptografar(mensagem_encriptada, p, chave, q)
	mensagem_final = ''.join(mensagem_descriptada)
	print("Mensagem Descriptografada:", mensagem_final)

if __name__ == '__main__':
	principal()
