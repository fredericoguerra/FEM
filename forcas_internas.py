from matriz_rotacao import matriz_rotacao
import numpy as np
from pontos import pontos
from numpy.linalg import norm

def forcas_internas(prop, X):
	eixo_x   = prop['eixo_x']
	eixo_y   = prop['eixo_y']
	elementos = prop['elementos']
	E 		 = prop['mod_elast']
	A 		 = prop['areas']
	# Tensão em cada elemento
	forcin = []
	for elemento in elementos:
		# Comprimento do elemento
		fromPoint, toPoint, glib = pontos(elemento, prop)
		vetor_elemento = toPoint - fromPoint

		# Matriz de rotação
		tau = matriz_rotacao(vetor_elemento, eixo_x, eixo_y)
		desl_global = np.array([0,0,X[0],X[1]])
		q = tau.dot(desl_global)

		# Forças internas e tensão no elemento
		strain = (q[1] - q[0]) / norm(vetor_elemento)
		stress = E[elemento] * strain
		forcin.append(stress)


	return forcin