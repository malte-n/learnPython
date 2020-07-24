import matplotlib.pyplot as plt
from random_walk import Randomwalk


# initialize the class and create a random path by calling fill_walk()
rw = Randomwalk()
rw.fill_walk()

plt.style.use('classic')
fig, ax = plt.subplots()

# plot the points in the lists created in rw.fill_walk
ax.scatter(rw.x_values, rw.y_values, s=15)

# Display the graph
plt.show()
