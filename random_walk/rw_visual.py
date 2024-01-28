import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Continua criando passeios novos, desde que o programa esteja ativo 
while True:
    # Cria um 'random walk'
    rw = RandomWalk(50_000)
    rw.fill_walk()

    # Plota os pontos no passeio 
    plt.style.use('classic')
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, 
               cmap=plt.cm.Blues, edgecolors='none', s=1)
    ax.set_aspect('equal')

    # Destaca o primeiro e o último ponto
    ax.scatter(0, 0, c='green', edgecolor='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none', s=100)
    plt.show()

    keep_running = input("Make another walk? (y/n): ").strip().lower()
    if keep_running == 'n':
        break