# -*- coding: UTF-8 -*-
def listar(nomes):
	    print 'Listando nomes:'
	    for nome in nomes:
			     print nome

def cadastrar(nomes):
	print 'Digite o nome:'
	nome = raw_input()
	nomes.append(nome)

def menu():
	nomes = []
	escolha = ''
	while(escolha != '0'):
		print 'Digite 1 para cadastrar, 3 para remover e 0 para terminar.'
		escolha = raw_input()

		if(escolha == '1'):
			cadastrar(nomes)
		if(escolha == '2'):
			listar(nomes)
		if(escolha == '3'):		
			remover(nomes)

def remover(nomes):
	print 'Digite o nome a remover:'
	nome = raw_input()
	nomes.remove(nome)


menu()