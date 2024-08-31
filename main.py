import matplotlib.pyplot as plt
import numpy as np
from unihiker import GUI
from pinpong.board import Board, Pin

# Initialize GUI and Board
gui = GUI()
Board("unihiker").begin()

# Initialize buttons for navigation
btn1 = Pin(Pin.PA7, Pin.IN)  # Button 1 (Next)
btn2 = Pin(Pin.PA8, Pin.IN)  # Button 2 (Previous)
btn3 = Pin(Pin.PA9, Pin.IN)  # Button 3 (Select/Enter)

# Menu options
menu_options = ["Line Chart", "Bar Chart", "Scatter Plot", "Customize Chart", "Save Chart"]
current_option = 0

# Variables for custom data input
custom_data_x = []
custom_data_y = []
custom_title = "Custom Chart"
custom_xlabel = "X Axis"
custom_ylabel = "Y Axis"
custom_color = "blue"

# Function to create a line chart
def create_line_chart(x=None, y=None):
    if x is None:
        x = np.linspace(0, 10, 100)
    if y is None:
        y = np.sin(x)

    plt.figure()
    plt.plot(x, y, label='Sine Wave', color=custom_color)
    plt.title(custom_title)
    plt.xlabel(custom_xlabel)
    plt.ylabel(custom_ylabel)
    plt.legend()

    plt.savefig('/mnt/data/line_chart.png')
    plt.close()

# Function to create a bar chart
def create_bar_chart(x=None, y=None):
    if x is None:
        x = ['A', 'B', 'C', 'D', 'E']
    if y is None:
        y = [5, 7, 3, 8, 6]

    plt.figure()
    plt.bar(x, y, color=custom_color)
    plt.title(custom_title)
    plt.xlabel(custom_xlabel)
    plt.ylabel(custom_ylabel)

    plt.savefig('/mnt/data/bar_chart.png')
    plt.close()

# Function to create a scatter plot
def create_scatter_plot(x=None, y=None):
    if x is None:
        x = np.random.rand(50)
    if y is None:
        y = np.random.rand(50)

    plt.figure()
    plt.scatter(x, y, color=custom_color)
    plt.title(custom_title)
    plt.xlabel(custom_xlabel)
    plt.ylabel(custom_ylabel)

    plt.savefig('/mnt/data/scatter_plot.png')
    plt.close()

# Function to input custom data
def input_custom_data():
    global custom_data_x, custom_data_y
    custom_data_x = []
    custom_data_y = []
    
    gui.clear()
    gui.draw_text(10, 10, "Enter X values (comma-separated):", color=(255, 255, 255))
    x_values = gui.get_input()
    gui.clear()

    gui.draw_text(10, 10, "Enter Y values (comma-separated):", color=(255, 255, 255))
    y_values = gui.get_input()
    gui.clear()

    custom_data_x = [float(x.strip()) for x in x_values.split(',')]
    custom_data_y = [float(y.strip()) for y in y_values.split(',')]

# Function to customize chart properties
def customize_chart():
    global custom_title, custom_xlabel, custom_ylabel, custom_color

    gui.clear()
    gui.draw_text(10, 10, "Enter Chart Title:", color=(255, 255, 255))
    custom_title = gui.get_input()
    gui.clear()

    gui.draw_text(10, 10, "Enter X Axis Label:", color=(255, 255, 255))
    custom_xlabel = gui.get_input()
    gui.clear()

    gui.draw_text(10, 10, "Enter Y Axis Label:", color=(255, 255, 255))
    custom_ylabel = gui.get_input()
    gui.clear()

    gui.draw_text(10, 10, "Enter Color (e.g., blue, red):", color=(255, 255, 255))
    custom_color = gui.get_input()
    gui.clear()

# Function to save the chart with a custom name
def save_chart():
    gui.clear()
    gui.draw_text(10, 10, "Enter filename to save chart:", color=(255, 255, 255))
    filename = gui.get_input()
    gui.clear()
    
    plt.savefig(f'/mnt/data/{filename}.png')

# Display the menu and handle user selection
def display_menu():
    global current_option
    gui.draw_text(10, 10, f"Select Option:", color=(255, 255, 255))
    gui.draw_text(10, 40, f"{menu_options[current_option]}", color=(255, 255, 255))

    if btn1.read_digital() == 0:  # Button 1 pressed (Next option)
        current_option = (current_option + 1) % len(menu_options)
        gui.clear()  # Clear the screen before updating the option
    elif btn2.read_digital() == 0:  # Button 2 pressed (Previous option)
        current_option = (current_option - 1) % len(menu_options)
        gui.clear()
    elif btn3.read_digital() == 0:  # Button 3 pressed (Select option)
        gui.clear()
        if menu_options[current_option] in ["Line Chart", "Bar Chart", "Scatter Plot"]:
            display_chart()
        elif menu_options[current_option] == "Customize Chart":
            customize_chart()
        elif menu_options[current_option] == "Save Chart":
            save_chart()

# Display the selected chart
def display_chart():
    if menu_options[current_option] == "Line Chart":
        if custom_data_x and custom_data_y:
            create_line_chart(custom_data_x, custom_data_y)
        else:
            create_line_chart()
        gui.draw_image('/mnt/data/line_chart.png')
    elif menu_options[current_option] == "Bar Chart":
        if custom_data_x and custom_data_y:
            create_bar_chart(custom_data_x, custom_data_y)
        else:
            create_bar_chart()
        gui.draw_image('/mnt/data/bar_chart.png')
    elif menu_options[current_option] == "Scatter Plot":
        if custom_data_x and custom_data_y:
            create_scatter_plot(custom_data_x, custom_data_y)
        else:
            create_scatter_plot()
        gui.draw_image('/mnt/data/scatter_plot.png')

# Main loop
while True:
    display_menu()
    gui.mainloop()
