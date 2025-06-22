import pygame
import random

# Initialize Pygame and mixer
pygame.mixer.pre_init(44100, -16, 2, 512)  # Configure audio: 44.1kHz, 16-bit, stereo, 512 buffer
pygame.init()

# Set up the window
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird Clone")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Bird properties
bird = pygame.Rect(200, HEIGHT // 2, 30, 30)
bird_velocity = 0
GRAVITY = 0.5
JUMP = -10

# Pipe properties
PIPE_WIDTH = 50
PIPE_GAP = 150
PIPE_SPEED = 3
PIPE_SPAWN_INTERVAL = 100  # Frames between pipe spawns (~1.67s at 60 FPS)
MAX_PIPES = 3  # Maximum number of pipes on screen
pipes = []
pipe_timer = 0

# Score and high score
score = 0
high_score = 0
font = pygame.font.SysFont("arial", 30)

# Load sound effects
try:
    jump_sound = pygame.mixer.Sound("jump.mp3")
    jump_sound.set_volume(0.5)  # 50% volume
except FileNotFoundError:
    print("jump.wav not found! Sound effect skipped.")
    jump_sound = None

try:
    point_sound = pygame.mixer.Sound("coin.mp3")
    point_sound.set_volume(0.5)
except FileNotFoundError:
    print("coin.wav not found! Sound effect skipped.")
    point_sound = None

try:
    hit_sound = pygame.mixer.Sound("hit.mp3")
    hit_sound.set_volume(0.5)
except FileNotFoundError:
    print("hit.wav not found! Sound effect skipped.")
    hit_sound = None

# Load background music
try:
    pygame.mixer.music.load("bgm.mp3")
    pygame.mixer.music.set_volume(0.1)  # 10% volume
except FileNotFoundError:
    print("bgm.mp3 not found! Background music skipped.")

# Game state
game_started = False

# Clock for frame rate
clock = pygame.time.Clock()

# Function to create a new pipe pair
def create_pipe():
    pipe_height = random.randint(150, 400)
    top_pipe = pygame.Rect(WIDTH, 0, PIPE_WIDTH, pipe_height)
    bottom_pipe = pygame.Rect(WIDTH, pipe_height + PIPE_GAP, PIPE_WIDTH, HEIGHT - pipe_height - PIPE_GAP)
    return {"top": top_pipe, "bottom": bottom_pipe, "scored": False}

# Function to reset game
def reset_game():
    global bird, bird_velocity, pipes, pipe_timer, score, game_started, high_score
    if score > high_score:
        high_score = score
    bird = pygame.Rect(200, HEIGHT // 2, 30, 30)
    bird_velocity = 0
    pipes = [create_pipe()]
    pipe_timer = 0
    score = 0
    game_started = False
    if hit_sound:
        hit_sound.play()  # Play hit sound on reset
    pygame.mixer.music.stop()  # Stop music on reset

# Initialize with one pipe
pipes.append(create_pipe())

# Game loop
running = True
while running:
    clock.tick(60)  # 60 FPS

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not game_started:
                    game_started = True
                    # pygame.mixer.music.play(-1)  # Start background music
                bird_velocity = JUMP
                if jump_sound:
                    jump_sound.play()  # Play jump sound

    if game_started:
        # Update bird
        bird_velocity += GRAVITY
        bird.y += bird_velocity

        # Update pipes
        pipe_timer += 1
        if pipe_timer >= PIPE_SPAWN_INTERVAL and len(pipes) < MAX_PIPES:
            pipes.append(create_pipe())
            pipe_timer = 0

        for pipe in pipes[:]:  # Copy list to allow removal
            pipe["top"].x -= PIPE_SPEED
            pipe["bottom"].x -= PIPE_SPEED
            if pipe["top"].x < -PIPE_WIDTH:
                pipes.remove(pipe)
            if not pipe["scored"] and pipe["top"].x + PIPE_WIDTH < bird.x:
                score += 1
                pipe["scored"] = True
                if point_sound:
                    point_sound.play()  # Play point sound

        # Collision detection
        for pipe in pipes:
            if bird.colliderect(pipe["top"]) or bird.colliderect(pipe["bottom"]):
                reset_game()
        if bird.y > HEIGHT or bird.y < 0:
            reset_game()

    # Draw
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, bird)
    for pipe in pipes:
        pygame.draw.rect(screen, GREEN, pipe["top"])
        pygame.draw.rect(screen, GREEN, pipe["bottom"])


    # Current score (top-left)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # High score (top-right)
    high_score_text = font.render(f"High Score: {high_score}", True, WHITE)
    high_score_rect = high_score_text.get_rect(topright=(WIDTH - 10, 10))
    screen.blit(high_score_text, high_score_rect)
    pygame.display.flip()

pygame.mixer.music.stop()  # Stop music on quit
pygame.quit()