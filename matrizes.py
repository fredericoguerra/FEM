import numpy as np
from plot_elemento import plot_elemento
from pontos import pontos
from plot_nos import plot_nos
from matriz_rotacao import matriz_rotacao
from numpy.linalg import norm

def matrizes(prop):
	# Matriz global dos elementos
	ngrlib    = prop['ngrlib']
	nos    = prop['nos']
	elementos = prop['elementos']
	forcas   = prop['forcas']
	areas    = prop['areas']
	eixo_x   = prop['eixo_x']
	eixo_y   = prop['eixo_y']

	plot_nos(nos)

	K = np.zeros((ngrlib,ngrlib))

	for elemento in elementos:
		# Geometria do elemento
		ponto_inicial, ponto_final, grlib = pontos(elemento, prop)
		vetor_elemento = ponto_final - ponto_inicial

		plot_elemento(ponto_inicial, ponto_final, elemento, areas)   # Plotagem do Elemento

		# Propriedades do elemento
		L = norm(vetor_elemento)
		area   = prop['areas'][elemento]
		E      = prop['mod_elast'][elemento]

		Ck = E * area / L

		k = np.array([[1,-1],[-1,1]])

		# Matriz de Rotação
		tau = matriz_rotacao(vetor_elemento, eixo_x, eixo_y)
		k_r = tau.T.dot(k).dot(tau)

		# Coordenadas locais para globais
		index = grlib-1
		B = np.zeros((4,ngrlib))

		for i in range(4):
			B[i,index[i]] = 1.0
		K_rG = B.T.dot(k_r).dot(B)

		K += Ck * K_rG
	Kf = K
	# Vetor de Forças
	F = []
	for f in forcas.values():
		F.extend(f)
	F = np.array(F)
	Ff = F
	# Remoção de nós restritos
	remover_indices = np.array(prop['grlib_restritos']) - 1
	for i in [0,1]:
		Kf = np.delete(Kf, remover_indices, axis=i)
	K2 = np.delete(K, remover_indices, axis=1)
	Ff = np.delete(Ff, remover_indices)

	return K, F, Kf, Ff, K2