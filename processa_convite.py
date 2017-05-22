def processa_convite(convite):
	posicao_final = len(convite)
	posicao_inicial = posicao_final -4
	parte1 = convite[0:4]
	parte2 = convite[posicao_inicial: posicao_final]
	nome_formatado = parte1+parte2
	return "Enviando convite para %s" % (nome_formatado)