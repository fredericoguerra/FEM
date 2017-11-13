import matplotlib.pyplot as plt

def plot_nos(nos):
    x = [i[0] for i in nos.values()]
    y = [i[1] for i in nos.values()]
    size = 40
    offset = size / 4000.
    plt.scatter(x, y, c='silver', s=size, zorder=5)
    for i, location in enumerate(zip(x, y)):
        plt.annotate(i + 1, (location[0] - offset, location[1] - offset), zorder=10)