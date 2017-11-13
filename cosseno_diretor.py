import numpy as np
from numpy.linalg import norm

def cosseno_diretor(vec1, vec2):
	return np.dot(vec1,vec2) / (norm(vec1) * norm(vec2))