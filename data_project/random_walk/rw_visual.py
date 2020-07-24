import matplotlib.pyplot as plt
from random_walk import Randomwalk





# initialize the class and create a random path by calling fill_walk()
while True:

    # initialize the imported class and call its method
    rw = Randomwalk(50_000)
    rw.fill_walk()

    plt.style.use('classic')

    # mostly ax used to plot and scatter the graphs
    fig, ax = plt.subplots(figsize=(16, 9))


    # plot the points in the lists created in rw.fill_walk
    point_numbers = range(rw.num_points)
    ax.plot(rw.x_values, rw.y_values, linewidth=2, color='black')
    # ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.get_cmap('Blues'), edgecolors='none', s=1)

    # emphasize the first and last points
    # ax.scatter(0, 0, c='green', edgecolors='none', s=50)
    # ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=50)

    #Remove the axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    # Display the graph
    plt.show()

    # only works when running in the shell
    keep_running = input("Make another walk? (Y/n): ").lower()

    if keep_running == 'n':
        break
