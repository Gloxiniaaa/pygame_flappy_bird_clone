Flappy Bird Clone
This is my first Pygame game, a simple clone of Flappy Bird built with Python and Pygame. The game features a bird (white rectangle) that navigates through moving pipes (green rectangles) by jumping with the spacebar. The game starts with stationary objects, begins moving when you press the spacebar, and resets on collision. It includes audio effects for jumping, scoring, and collisions, a looping background music track, and a high score display. The game is framerate-independent for smooth gameplay across different systems.
How to Run the Game
Follow these steps to set up and play the game:

Clone the Project:

If the project is hosted on a Git repository (e.g., GitHub), clone it to your computer:git clone <repository-url>


Alternatively, download the project files (e.g., flappy_bird.py) and place them in a folder (e.g., flappy-bird-clone).


Install Python:

Download and install Python (version 3.8 or higher) from python.org.
During installation, check "Add Python to PATH" to make it accessible from the command line.
Verify installation by opening a terminal (Command Prompt on Windows, Terminal on macOS/Linux) and running:python --version

orpython3 --version

You should see the Python version (e.g., Python 3.11.0).


Install Pygame:

In the terminal, install Pygame using pip:pip install pygame

orpython -m pip install pygame

Verify installation by running Python (python or python3), typing import pygame, and checking for no errors. Exit with exit().


Prepare Audio Files (Optional):

The game uses four audio files: jump.wav, point.wav, hit.wav, and bgm.mp3. Place them in the same folder as flappy_bird.py.
If missing, download free WAV and MP3 files from freesound.org or opengameart.org (ensure they’re licensed for use, e.g., CC0). Rename them to match or update the file paths in flappy_bird.py.
The game won’t crash if files are missing; it will print warnings and skip those sounds.


Run the Game:

Navigate to the project folder in the terminal:cd path/to/flappy-bird-clone


Run the game:python flappy_bird.py

orpython3 flappy_bird.py




Gameplay:

The game starts with a stationary bird and pipes.
Press spacebar to start (bird jumps, music plays, pipes move).
Navigate through pipe gaps using spacebar to jump.
Score (top-left) increases when passing pipes; high score (top-right) updates if surpassed.
On collision or out-of-bounds, the game resets to the stationary state.
Close the window to quit.



Credits

Developer: This is my first Pygame project, created to learn game development with Python.
Grok: The AI assistant Grok, created by xAI, provided step-by-step guidance, code examples, and explanations to build this game. Grok helped with implementing game mechanics, audio, framerate independence, and debugging tips.
Audio: Sound effects and music (if used) are sourced from freesound.org or opengameart.org (update with specific credits if you have licensed audio files).

Thank you for playing my first game!