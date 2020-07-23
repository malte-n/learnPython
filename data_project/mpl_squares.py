import matplotlib.pyplot as plt


x_input_values = [1, 2, 3, 4, 5]
y_squares = [1, 4, 9, 16, 25]

plt.style.use('seaborn-dark')
fig, ax = plt.subplots()
ax.plot(x_input_values, y_squares, linewidth=3)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square Value", fontsize=14)

# Set size of tick labels
ax.tick_params(axis='both', labelsize=14)

plt.show()
