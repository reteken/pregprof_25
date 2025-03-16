# import all the necessary libraries
import numpy as np
import matplotlib.pyplot as plt


# defining a user-defined function to plot the three-dimensional scatter plot
def three_dimensional_scatter(x1, y1, z1, x2, y2, z2):
    # creating figure object in the plot
    fig = plt.figure(figsize=(9, 9))
    # created three-dimensional workspace
    ax = plt.axes(projection="3d")
    # plotting the first three-dimensional scatter plot using the parameters
    ax.scatter3D(x1, y1, z1, color="green")
    # plotting the second three-dimensional scatter plot using the parameters
    ax.scatter3D(x2, y2, z2, color="red")
    # defining title to the plot
    plt.title("Creating three-dimensional scatter plot using matplotlib and numpy")
    # defining legends to the plot
    plt.legend(["first", "second"])
    # displaying the three-dimensional scatter plot
    plt.show()


# creating the main() function
def main():
    # creating data points for the z-axis
    z1 = np.arange(0, 256, 1)
    # creating data points for the x-axis
    x1 = np.random.randint(256, size=(256))
    # creating data points for the y axis
    y1 = np.random.randint(256, size=(256))
    z2 = np.arange(0, 256, 1)
    # creating data points for the x-axis
    x2 = np.random.randint(256, size=(256))
    # creating data points for the y axis
    y2 = np.random.randint(256, size=(256))
    # calling the main() function
    three_dimensional_scatter(x1, y1, z1, x2, y2, z2)


# declaring the main() function as the driving code of the program.
if __name__ == "__main__":
    main()
