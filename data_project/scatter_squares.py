import matplotlib.pyplot as plt

x_input_values = range(1, 5001)
y_squares = [x**2 for x in x_input_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()

# s=x sets the size of the dots
ax.scatter(x_input_values, y_squares, cmap=plt.get_cmap('Blues'), s=10)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square Value", fontsize=14)

# Set size of tick labels
ax.tick_params(axis='both', which='major', labelsize=14)

# Set the range for each axis
ax.axis([0, 1100, 0, 1100000])

plt.show()

# saves the file as png and trims white space
# plt.savefig.('suqares_plot.png', bbox_inches='tight')
