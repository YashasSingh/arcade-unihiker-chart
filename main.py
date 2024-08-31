import matplotlib.pyplot as plt
import numpy as np
from unihiker import GUI
from pinpong.board import Board, Pin

# Initialize GUI and Board
gui = GUI()
Board("unihiker").begin()

# Initialize buttons for navigation
btn1 = Pin(Pin.PA7, Pin.IN)  # Button 1
btn2 = Pin(Pin.PA8, Pin.IN)  # Button 2
btn3 = Pin(Pin.PA9, Pin.IN)  # Button 3

# Menu options
menu_options = ["Line Chart", "Bar Chart", "Scatter Plot"]
current_option = 0

# Function to create a line chart
def create_line_chart():
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    plt.figure()
    plt.plot(x, y, label='Sine Wave')
    plt.title('Sine Wave Chart')
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.legend()

    plt.savefig('/mnt/data/line_chart.png')
    plt.close()

# Function to create a bar chart
def create_bar_chart():
    x = ['A', 'B', 'C', 'D', 'E']
    y = [5, 7, 3, 8, 6]

    plt.figure()
    plt.bar(x, y, color='blue')
    plt.title('Bar Chart')
    plt.xlabel('Categories')
    plt.ylabel('Values')

    plt.savefig('/mnt/data/bar_chart.png')
    plt.close()

# Function to create a scatter plot
def create_scatter_plot():
    x = np.random.rand(50)
    y = np.random.rand(50)

    plt.figure()
    plt.scatter(x, y, color='red')
    plt.title('Scatter Plot')
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')

    plt.savefig('/mnt/data/scatter_plot.png')
    plt.close()

# Display the menu and handle user selection
def display_menu():
    global current_option
    gui.draw_text(10, 10, f"Select Chart Type:", color=(255, 255, 255))
    gui.draw_text(10, 40, f"{menu_options[current_option]}", color=(255, 255, 255))

    if btn1.read_digital() == 0:  # Button 1 pressed (Next option)
        current_option = (current_option + 1) % len(menu_options)
        gui.clear()  # Clear the screen before updating the option
    elif btn2.read_digital() == 0:  # Button 2 pressed (Previous option)
        current_option = (current_option - 1) % len(menu_options)
        gui.clear()
    elif btn3.read_digital() == 0:  # Button 3 pressed (Select option)
        gui.clear()
        display_chart()

# Display the selected chart
def display_chart():
    if menu_options[current_option] == "Line Chart":
        create_line_chart()
        gui.draw_image('/mnt/data/line_chart.png')
    elif menu_options[current_option] == "Bar Chart":
        create_bar_chart()
        gui.draw_image('/mnt/data/bar_chart.png')
    elif menu_options[current_option] == "Scatter Plot":
        create_scatter_plot()
        gui.draw_image('/mnt/data/scatter_plot.png')

# Main loop
while True:
    display_menu()
    gui.mainloop()
