import numpy as np
from cosseno_diretor import cosseno_diretor

def matriz_rotacao(vetor_elemento, eixo_x, eixo_y):
	# Cálculo dos cossenos diretores
	x_proj = cosseno_diretor(vetor_elemento, eixo_x)
	y_proj = cosseno_diretor(vetor_elemento, eixo_y)
	return np.array([[x_proj,y_proj,0,0],[0,0,x_proj,y_proj]])

""" Retorna a matriz de rotação 2 x 4:
	| x_proj, y_proj,      0,      0|
	|      0,      0, x_proj, y_proj|"""