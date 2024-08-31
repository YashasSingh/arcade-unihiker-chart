import matplotlib.pyplot as plt
import numpy as np
from unihiker import GUI

# Initialize GUI
gui = GUI()

# Create a simple line chart using matplotlib
def create_line_chart():
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    plt.figure()
    plt.plot(x, y, label='Sine Wave')
    plt.title('Sine Wave Chart')
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.legend()

    # Save the plot as an image
    plt.savefig('/mnt/data/chart.png')
    plt.close()

# Display the chart on UniHiker
def display_chart():
    create_line_chart()
    gui.draw_image('/mnt/data/chart.png')

# Main loop to display the chart
display_chart()
gui.mainloop()

