
# Finite Element Method
Python code to do 2D Truss analysis.

step-by-step:

open setup.py
	enter with the nodes and their coordinates into the nos dictionary;
	for each node added previously put their degrees of freedom into graus_de_liberdade dictionary;
	put all the elements and their points associated into elementos;
	put the degrees of freedom restricted into the vector grlib_restritos;
	put the external forces in each node with their intensities in x and y axies;
	finaly, enter with area and young's modulus;
run main.py
