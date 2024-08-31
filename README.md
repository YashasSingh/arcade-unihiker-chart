

# UniHiker Chart System

## Overview

The **UniHiker Chart System** is an interactive data visualization tool designed for the UniHiker platform. This system allows users to create, customize, and display various types of charts, including line charts, bar charts, scatter plots, pie charts, histograms, box plots, and heatmaps. The system also supports real-time data visualization, data import from CSV files, chart customization, zooming and panning, and chart sharing.

## Features

- **Chart Types**: Create various types of charts, including:
  - Line Chart
  - Bar Chart
  - Scatter Plot
  - Pie Chart
  - Histogram
  - Box Plot
  - Heatmap

- **Customization**: Customize charts with options to change the title, axis labels, colors, line styles, markers, and grid visibility.

- **Data Input**:
  - Input custom data directly through the UniHiker GUI.
  - Import data from CSV files.

- **Real-Time Data**: Display and update charts in real-time with data streaming capabilities.

- **Zoom and Pan**: Enable zoom and pan on charts for detailed data exploration.

- **Chart Saving and Loading**: Save your charts as images and load them for future viewing.

- **Chart Sharing**: Save charts with a custom name, ready for sharing or further use.

## Getting Started

### Prerequisites

- **UniHiker Platform**: Ensure your UniHiker is properly set up and connected.
- **Python Libraries**:
  - `matplotlib`
  - `numpy`
  - `pandas`
  - `unihiker`
  - `pinpong`

Install the required libraries using:

```bash
pip install matplotlib numpy pandas unihiker pinpong
```

### Installation

1. Clone the repository to your UniHiker:

```bash
git clone https://github.com/your-repo/unihiker-chart-system.git
cd unihiker-chart-system
```

2. Run the main script:

```bash
python unihiker_chart_system.py
```

### Usage

- Use the UniHiker buttons to navigate through the menu options.
- Select a chart type to create and display it on the UniHiker screen.
- Customize your chart by selecting the "Customize Chart" option.
- Import data from CSV files for more complex visualizations.
- Enable zoom and pan for detailed chart exploration.
- Save your charts for later use or sharing.

## Customization

- **Custom Data Input**: Manually input X and Y values for your charts.
- **Chart Properties**: Modify chart properties like title, axis labels, colors, and styles.
- **Grid Visibility**: Toggle grid lines on or off.

## File Structure

- **`/mnt/data/`**: Directory where charts are saved as `.png` files.
- **`unihiker_chart_system.py`**: Main Python script for running the chart system.

## Roadmap

- **Network Sharing**: Implement functionality to share charts over a network.
- **Improved Input Validation**: Enhance error handling for user inputs.

## License

This project is licensed under the MIT License.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

