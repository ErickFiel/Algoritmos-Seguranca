import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random

gerador_aleatorio = Random.new().read
chave = RSA.generate(1024, gerador_aleatorio) # gera chaves pública e privada

chave_publica = chave.publickey() # exporta a chave pública para troca

mensagem = 'criptografar esta mensagem'
mensagem_encriptada = chave_publica.encrypt(mensagem, 32)
# a mensagem a ser criptografada está na linha acima 'criptografar esta mensagem'

print('mensagem criptografada:', mensagem_encriptada) # texto cifrado

arquivo = open('criptografia.txt', 'w')
arquivo.write(str(mensagem_encriptada)) # escreve o texto cifrado no arquivo
arquivo.close()

# código para descriptografar abaixo

arquivo = open('criptografia.txt', 'r')
mensagem_cifrada = arquivo.read()

mensagem_descriptografada = chave.decrypt(eval(mensagem_cifrada))

print('mensagem descriptografada:', mensagem_descriptografada)

arquivo = open('criptografia.txt', 'w')
arquivo.write(str(mensagem_cifrada))
arquivo.write(str(mensagem_descriptografada))
arquivo.close()
