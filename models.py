# -*- coding UTF-8 -*-

class Perfil(object):
	'Classe padrao perfil de usuarios'

	# construtor de classe python
	def __init__(self, nome, telefone, empresa):
		self.nome = nome
		self.telefone = telefone
		self.empresa = empresa
		self.__curtidas = 0

	def imprimir(self):
		print 'Nome %s, Telefone %s, Empresa %s' % (self.nome, self.telefone, self.empresa)	

	def curtir(self):
		self.__curtidas += 1

	def	obter_curtida(self):
		return self.__curtidas

# usando herança - esta classe herda de Perfil e herda seus atributos
class Perfil_vip(Perfil):
	'Classe padrao perfil de usuarios VIP'

	def obter_creditos(self)
			return super(Perfil_vip, self).obter_curtida() * 10.0						