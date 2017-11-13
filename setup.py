import numpy as np

def setup():
    # Sistema de coordenadas
    eixo_x = np.array([1, 0])
    eixo_y = np.array([0, 1])

    # Modelo de Treliça
    nos = { 1: [0, 0], 2: [12, 8], 3: [12, 0] }
    graus_liberdade = { 1: [1, 2], 2: [3, 4], 3: [5, 6] }
    elementos = { 1: [1, 2], 2: [2, 3] }
    grlib_restritos = [1, 2, 5, 6]
    forcas = { 1: [0, 0], 2: [50, 0], 3: [0, 0] }

    # Propriedades do Material
    mod_elast = { 1: 30.0e6, 2: 30.0e6 }
    # Propriedades da Seção
    areas = { 1: 490.86e-4, 2: 490.86e-4 }

    ngrlib = 2 * len(nos)

    # Conferindo inputs
    assert len(elementos) == len(mod_elast) == len(areas)
    assert len(grlib_restritos) < ngrlib
    assert len(forcas) == len(nos)

    return {  'eixo_x':eixo_x, 'eixo_y':eixo_y, 'nos':nos, 'graus_liberdade':graus_liberdade,\
          	  'elementos':elementos, 'grlib_restritos':grlib_restritos, 'forcas':forcas, 'ngrlib':ngrlib,\
          	  'mod_elast':mod_elast, 'areas':areas }