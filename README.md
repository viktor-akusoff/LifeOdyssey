## Life Odyssey

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Life Odyssey is a desktop application built with PySide6 and NumPy that provides a visual and interactive simulation of Conway's Game of Life, a classic cellular automaton.

### Features

- **Interactive Drawing:** Draw your own patterns of live cells on the grid to explore different starting configurations.
- **Multiple Colors:** Experience the Game of Life with an added dimension of color.  Cells can have different colors, and these colors interact according to the simulation rules.
- **Animation and Playback Control:** Watch your patterns evolve over time with smooth animations. Control the simulation speed, pause, play, and navigate through individual frames.
- **Save and Load:** Save interesting patterns or simulation states and load them later to continue your exploration.
- **Create New Boards:** Customize the board size to experiment with different scales and complexities.
- **Calculate Iterations:**  Automatically calculate and display multiple iterations of the Game of Life to analyze long-term behavior.
- **Clean Board:**  Quickly reset the board to a blank slate for new creations.

### Requirements

- Python 3.6 or higher
- PySide6
- NumPy

### Installation

1. Clone the repository: 
   ```bash
   git clone https://github.com/your-username/life-odyssey.git
   ```
2. Navigate to the project directory:
   ```bash
   cd life-odyssey
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. Run the application:
   ```bash
   python main.py
   ```
2. Use the drawing tools to create a starting pattern on the grid.
3. Use the playback controls to run the simulation.
4. Explore the menus for additional options, such as saving/loading, creating new boards, and calculating iterations.

### Controls

- **Mouse Click & Drag:** Draw or erase cells (depending on the selected mode).
- **Play Button:** Start/pause the simulation.
- **Stop Button:** Stop the simulation and reset to the initial frame.
- **Skip Forward/Backward Buttons:** Jump ahead or backward by multiple frames.
- **Frame Spinbox:** Manually select a specific simulation frame.
- **Palette Button:** Choose a different color for drawing.
- **Draw Button:** Switch to drawing mode.
- **Erase Button:** Switch to erasing mode.

### File Menu

- **New Field:** Create a new game board with custom dimensions.
- **Open Field:** Load a previously saved game board state from a `.npy` file.
- **Save Field:** Save the current game board state to a `.npy` file.

### Edit Menu

- **Clean Field:**  Clear all cells on the board.
- **Calculate Field:**  Calculate and display multiple iterations of the simulation.

### Help Menu

- **Documentation:** (Link to documentation if available)
- **About:**  Display information about the application.


### Contributing

Contributions to Life Odyssey are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request. 

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 
