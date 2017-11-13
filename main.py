from setup import setup
from matrizes import matrizes
from forcas_internas import forcas_internas
from resultados import resultados
from reacoes import reacoes
import numpy as np
import matplotlib.pyplot as plt

def main():
	# Carregando Setup
	prop = setup()

	# Matrizes Globais
	K, F, Kf, Ff, K2 = matrizes(prop)

	# Deslocamento de cada elemento
	X = np.linalg.inv(Kf).dot(Ff)
	#X2 = np.linalg.inv(K).dot()


	# Tensão em cada elemento
	forcin = forcas_internas(prop, X)

	F2 = reacoes(prop, X)

	# Resultado final
	resultados(F2, X, forcin)

	plt.title('Análise de Treliça Plana')
	plt.show()

if __name__ == '__main__':
    main()