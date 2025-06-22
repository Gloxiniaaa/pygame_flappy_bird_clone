# Flappy Bird Clone

This is my first Pygame game, a simple clone of Flappy Bird built with Python and Pygame. The game features a bird (white rectangle) that navigates through moving pipes (green rectangles) by jumping with the spacebar. The game starts with stationary objects, begins moving when you press the spacebar, and resets on collision. It includes audio effects for jumping, scoring, and collisions, a looping background music track, and a high score display. The game is framerate-independent for smooth gameplay across different systems.

## How to Run the Game

Follow these steps to set up and play the game:

1. **Clone the Project**:
   - Open cmd and clone it to your computer:
     ```bash
     git clone https://github.com/Gloxiniaaa/pygame_flappy_bird_clone.git
     ```

2. **Install Python**:
   - Download and install Python (version 3.8 or higher) from [python.org](https://www.python.org/downloads/).
   - During installation, check "Add Python to PATH" to make it accessible from the command line.
   - Verify installation by opening a terminal (Command Prompt on Windows, Terminal on macOS/Linux) and running:
     ```bash
     python --version
     ```
     or
     ```bash
     python3 --version
     ```
     You should see the Python version (e.g., `Python 3.11.0`).

3. **Install Pygame**:
   - In the terminal, install Pygame using pip:
     ```bash
     pip install pygame
     ```
     or
     ```bash
     python -m pip install pygame
     ```
     Verify installation by running Python (`python` or `python3`), typing `import pygame`, and checking for no errors. Exit with `exit()`.

4. **Run the Game**:
   - Navigate to the project folder in the terminal:
     ```bash
     cd path/to/flappy-bird-clone
     ```
   - Run the game:
     ```bash
     python game.py
     ```
     or
     ```bash
     python3 game.py
     ```

5. **Gameplay**:
   - The game starts with a stationary bird and pipes.
   - Press **spacebar** to start (bird jumps, music plays, pipes move).
   - Navigate through pipe gaps using **spacebar** to jump.
   - Score (top-left) increases when passing pipes; high score (top-right) updates if surpassed.
   - On collision or out-of-bounds, the game resets to the stationary state.
   - Close the window to quit.

## Credits

- **Developer**: This is my first Pygame project, created to learn game development with Python.
- **Grok**: The AI assistant Grok, created by xAI, provided step-by-step guidance, code examples, and explanations to build this game. Grok helped with implementing game mechanics, audio, framerate independence, and debugging tips.
- **Audio**: Sound effects and music are sourced from [Myinstants](https://www.myinstants.com/en/search/?name=coin+) and [Pixabay](https://pixabay.com/music/search/8%20bit/)

Thank you!!!
