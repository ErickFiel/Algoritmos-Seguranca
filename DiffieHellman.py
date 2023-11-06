# Código Diffie-Hellman

def verificador_primo(p):
	# Verifica se o número inserido é primo ou não
	if p < 1:
		return -1
	elif p > 1:
		if p == 2:
			return 1
		for i in range(2, p):
			if p % i == 0:
				return -1
		return 1

def verificador_primitivo(g, p, L):
	# Verifica se o número inserido é uma raiz primitiva ou não
	for i in range(1, p):
		L.append(pow(g, i) % p)
	for i in range(1, p):
		if L.count(i) > 1:
			L.clear()
			return -1
	L.clear()
	return 1

l = []
while 1:
	P = int(input("Digite P: "))
	if verificador_primo(P) == -1:
		print("Número não é primo. Por favor, digite novamente!")
		continue
	break

while 1:
	G = int(input(f"Digite a raiz primitiva de {P}: "))
	if verificador_primitivo(G, P, l) == -1:
		print(f"Número não é uma raiz primitiva de {P}. Por favor, tente novamente!")
		continue
	break

# Chaves privadas
x1, x2 = int(input("Digite a chave privada do usuário 1: ")), int(
	input("Digite a chave privada do usuário 2: "))
while 1:
	if x1 >= P or x2 >= P:
		print(f"A chave privada de ambos os usuários deve ser menor que {P}!")
		continue
	break

# Calcula chaves públicas
y1, y2 = pow(G, x1) % P, pow(G, x2) % P

# Gera chaves secretas
k1, k2 = pow(y2, x1) % P, pow(y1, x2) % P

print(f"\nChave secreta para o usuário 1 é {k1}\nChave secreta para o usuário 2 é {k2}\n")

if k1 == k2:
	print("Chaves foram trocadas com sucesso.")
else:
	print("As chaves não foram trocadas com sucesso.")
