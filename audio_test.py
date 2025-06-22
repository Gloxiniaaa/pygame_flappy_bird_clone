import pygame

# Initialize Pygame and mixer
pygame.mixer.pre_init(44100, -16, 2, 512)  # Optional: configure audio
pygame.init()

# Set up the window
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Pygame Audio Test")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load sounds (adjust paths to your files)
try:
    jump_sound = pygame.mixer.Sound("jump.mp3")
    jump_sound.set_volume(0.5)  # 50% volume
except FileNotFoundError:
    print("jump.wav not found! Please provide a valid audio file.")

# Load background music
try:
    pygame.mixer.music.load("bgm.mp3")
    pygame.mixer.music.set_volume(0.3)  # 30% volume
    pygame.mixer.music.play(-1)  # Loop indefinitely
except FileNotFoundError:
    print("bgm.mp3 not found! Please provide a valid music file.")

# Font for instructions
font = pygame.font.SysFont("arial", 24)

# Game loop
running = True
while running:
    screen.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jump_sound.play()  # Play sound effect
            if event.key == pygame.K_p:
                pygame.mixer.music.pause()  # Pause music
            if event.key == pygame.K_r:
                pygame.mixer.music.unpause()  # Resume music
            if event.key == pygame.K_s:
                pygame.mixer.music.stop()  # Stop music

    # Draw instructions
    instructions = [
        "Press SPACE to play sound effect",
        "Press P to pause music",
        "Press R to resume music",
        "Press S to stop music",
        "Close window to quit"
    ]
    for i, text in enumerate(instructions):
        text_surface = font.render(text, True, WHITE)
        screen.blit(text_surface, (20, 20 + i * 30))

    pygame.display.flip()

pygame.mixer.music.stop()  # Stop music on quit
pygame.quit()