import matplotlib.pyplot as plt

def plot_elemento(ponto_inicial, ponto_final, elemento, areas):
	x1 = ponto_inicial[0]
	y1 = ponto_inicial[1]
	x2 = ponto_final[0]
	y2 = ponto_final[1]
	plt.plot([x1, x2], [y1, y2], color='silver', linestyle='-', linewidth=50*areas[elemento], zorder=1)