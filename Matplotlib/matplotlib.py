import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Plotting a line graph
plt.plot(x, y, marker='o', linestyle='--', color='g', label='Line Plot')

# Adding labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Plot')

# Adding a legend
plt.legend()

# Displaying the plot
plt.grid(True)
plt.show()
