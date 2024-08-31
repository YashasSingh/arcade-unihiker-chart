import matplotlib.pyplot as plt
import numpy as np
from unihiker import GUI
from pinpong.board import Board, Pin
import os
import random
import time

# Initialize GUI and Board
gui = GUI()
Board("unihiker").begin()

# Initialize buttons for navigation
btn1 = Pin(Pin.PA7, Pin.IN)  # Button 1 (Next)
btn2 = Pin(Pin.PA8, Pin.IN)  # Button 2 (Previous)
btn3 = Pin(Pin.PA9, Pin.IN)  # Button 3 (Select/Enter)

# Menu options
menu_options = [
    "Line Chart", "Bar Chart", "Scatter Plot", "Pie Chart", "Histogram",
    "Customize Chart", "Save Chart", "Load Chart", "Real-Time Data"
]
current_option = 0

# Variables for custom data input
custom_data_x = []
custom_data_y = []
custom_title = "Custom Chart"
custom_xlabel = "X Axis"
custom_ylabel = "Y Axis"
custom_color = "blue"
custom_linestyle = "-"
custom_marker = ""
custom_grid = True

# Function to create a line chart
def create_line_chart(x=None, y=None):
    if x is None:
        x = np.linspace(0, 10, 100)
    if y is None:
        y = np.sin(x)

    plt.figure()
    plt.plot(x, y, label='Sine Wave', color=custom_color, linestyle=custom_linestyle, marker=custom_marker)
    plt.title(custom_title)
    plt.xlabel(custom_xlabel)
    plt.ylabel(custom_ylabel)
    if custom_grid:
        plt.grid(True)
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
    if custom_grid:
        plt.grid(True)

    plt.savefig('/mnt/data/bar_chart.png')
    plt.close()

# Function to create a scatter plot
def create_scatter_plot(x=None, y=None):
    if x is None:
        x = np.random.rand(50)
    if y is None:
        y = np.random.rand(50)

    plt.figure()
    plt.scatter(x, y, color=custom_color, marker=custom_marker)
    plt.title(custom_title)
    plt.xlabel(custom_xlabel)
    plt.ylabel(custom_ylabel)
    if custom_grid:
        plt.grid(True)

    plt.savefig('/mnt/data/scatter_plot.png')
    plt.close()

# Function to create a pie chart
def create_pie_chart(x=None, labels=None):
    if x is None:
        x = [20, 30, 25, 25]
    if labels is None:
        labels = ['A', 'B', 'C', 'D']

    plt.figure()
    plt.pie(x, labels=labels, colors=[custom_color] * len(x), autopct='%1.1f%%')
    plt.title(custom_title)

    plt.savefig('/mnt/data/pie_chart.png')
    plt.close()

# Function to create a histogram
def create_histogram(x=None):
    if x is None:
        x = np.random.randn(1000)

    plt.figure()
    plt.hist(x, bins=20, color=custom_color)
    plt.title(custom_title)
    plt.xlabel(custom_xlabel)
    plt.ylabel(custom_ylabel)
    if custom_grid:
        plt.grid(True)

    plt.savefig('/mnt/data/histogram.png')
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
    global custom_title, custom_xlabel, custom_ylabel, custom_color, custom_linestyle, custom_marker, custom_grid

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

    gui.draw_text(10, 10, "Enter Line Style (e.g., -, --, :):", color=(255, 255, 255))
    custom_linestyle = gui.get_input()
    gui.clear()

    gui.draw_text(10, 10, "Enter Marker (e.g., o, x, *):", color=(255, 255, 255))
    custom_marker = gui.get_input()
    gui.clear()

    gui.draw_text(10, 10, "Show Grid? (yes/no):", color=(255, 255, 255))
    grid_input = gui.get_input().strip().lower()
    custom_grid = True if grid_input == "yes" else False
    gui.clear()

# Function to save the chart with a custom name
def save_chart():
    gui.clear()
    gui.draw_text(10, 10, "Enter filename to save chart:", color=(255, 255, 255))
    filename = gui.get_input()
    gui.clear()
    
    plt.savefig(f'/mnt/data/{filename}.png')

# Function to load a saved chart from the library
def load_chart():
    gui.clear()
    files = os.listdir('/mnt/data')
    image_files = [file for file in files if file.endswith('.png')]

    if not image_files:
        gui.draw_text(10, 10, "No saved charts found.", color=(255, 255, 255))
        gui.mainloop()
        return

    for i, file in enumerate(image_files):
        gui.draw_text(10, 30 + i * 20, f"{i + 1}: {file}", color=(255, 255, 255))

    gui.draw_text(10, 10, "Enter chart number to load:", color=(255, 255, 255))
    chart_number = int(gui.get_input()) - 1
    gui.clear()

    if 0 <= chart_number < len(image_files):
        gui.draw_image(f'/mnt/data/{image_files[chart_number]}')
    else:
        gui.draw_text(10, 10, "Invalid selection.", color=(255, 255, 255))

# Function to display real-time data on a line chart
def display_real_time_data():
    global custom_data_x, custom_data_y

    plt.ion()  # Turn on interactive mode
    fig, ax = plt.subplots()

    custom_data_x = []
    custom_data_y = []

    for i in range(50):  # Simulate 50 points of real-time data
        new_x = i
        new_y = random.uniform(-1, 1)

        custom_data_x.append(new_x)
        custom_data_y.append(new_y)

        ax.clear()
        ax.plot(custom_data_x, custom_data_y, color=custom_color, linestyle=custom_linestyle, marker=custom_marker)
        ax.set_title(custom_title)
        ax.set_xlabel(custom_xlabel)
        ax.set_ylabel(custom_ylabel)
        if custom_grid:
            ax.grid(True)
        plt.draw()
        plt.pause(0.1)  # Pause to simulate real-time data

    plt.ioff()  # Turn off interactive mode
    plt.savefig('/mnt/data/real_time_data_chart.png')
    plt.close()
    gui.draw_image('/mnt/data/real_time_data_chart.png')

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
        if menu_options[current_option] in ["Line Chart", "Bar Chart", "Scatter Plot", "Pie Chart", "Histogram"]:
            display_chart()
        elif menu_options[current_option] == "Customize Chart":
            customize_chart()
        elif menu_options[current_option] == "Save Chart":
            save_chart()
        elif menu_options[current_option] == "Load Chart":
            load_chart()
        elif menu_options[current_option] == "Real-Time Data":
            display_real_time_data()

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
    elif menu_options[current_option] == "Pie Chart":
        create_pie_chart()
        gui.draw_image('/mnt/data/pie_chart.png')
    elif menu_options[current_option] == "Histogram":
        create_histogram()
        gui.draw_image('/mnt/data/histogram.png')

# Main loop
while True:
    display_menu()
    gui.mainloop()
