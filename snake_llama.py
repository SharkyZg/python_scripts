import pygame
import time
import random
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 640, 480
BLOCK_SIZE = 20
SPEED = 10
INITIAL_SNAKE = [(100+2*BLOCK_SIZE, 100), (100+BLOCK_SIZE, 100), (100, 100)]
INITIAL_FOOD = (400, 300)
INITIAL_DIRECTION = "RIGHT"

# Initialize the score
score = 0

# Set up some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Set up the high score
def get_high_score():
    try:
        with open("high_score.txt", "r") as file:
            return int(file.read())
    except FileNotFoundError:
        with open("high_score.txt", "w") as file:
            file.write(str(0))
            return 0
        
def update_high_score(new_high_score):
    with open("high_score.txt", "w") as file:
        file.write(str(new_high_score))
        
high_score = get_high_score()

def reset_game():
    global snake, food, direction, score
    snake = list(INITIAL_SNAKE)
    food = INITIAL_FOOD
    direction = INITIAL_DIRECTION
    score = 0

def game_over():
    global snake, food, direction, score, high_score
    font = pygame.font.Font(None, 36)

    if score > high_score:
        high_score = score
        update_high_score(high_score)
    
    score_text = font.render(f"Final Score: {score}", True, (255, 255, 255))
    retry_text = font.render("Press any key to play again", True, (255, 255, 255))
    high_score_text = font.render(f"High Score: {high_score}", True, (255, 255, 255))  


    screen.fill(BLACK)
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2 - score_text.get_height() // 2 - 2 * score_text.get_height()))
    screen.blit(high_score_text, (WIDTH // 2 - high_score_text.get_width() // 2, HEIGHT // 2 - score_text.get_height()))
    screen.blit(retry_text, (WIDTH // 2 - retry_text.get_width() // 2, HEIGHT // 2 + score_text.get_height() ))
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                reset_game()
                return

reset_game()

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "DOWN":
                direction = "UP"
            elif event.key == pygame.K_DOWN and direction != "UP":
                direction = "DOWN"
            elif event.key == pygame.K_LEFT and direction != "RIGHT":
                direction = "LEFT"
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                direction = "RIGHT"

    # Move the snake
    head_x, head_y = snake[0]
    if direction == "UP":
        new_head = (head_x, head_y - BLOCK_SIZE)
    elif direction == "DOWN":
        new_head = (head_x, head_y + BLOCK_SIZE)
    elif direction == "LEFT":
        new_head = (head_x - BLOCK_SIZE, head_y)
    elif direction == "RIGHT":
        new_head = (head_x + BLOCK_SIZE, head_y)

    snake.insert(0,new_head)

    # Load a font (you may need to adjust the path)
    font = pygame.font.Font(None, 36)

    # Check for collision with food
    if snake[0] == food:
        score += 1 # Increase the score
        while True:
            food = (random.randint(0, WIDTH//BLOCK_SIZE - 1) * BLOCK_SIZE,
                    random.randint(0, HEIGHT//BLOCK_SIZE - 1) * BLOCK_SIZE)
            if food not in snake:
                break
    else:
        snake.pop()

    # Check for collision with wall or self
    if (snake[0][0] < 0 or snake[0][0] >= WIDTH or
            snake[0][1] < 0 or snake[0][1] >= HEIGHT or snake[0] in snake[1:]):
        game_over()

    screen.fill(BLACK)
    
    for x, y in snake:
        pygame.draw.rect(screen, WHITE, (x, y, BLOCK_SIZE, BLOCK_SIZE))
        
    pygame.draw.rect(screen, RED, (food[0], food[1], BLOCK_SIZE, BLOCK_SIZE))

    # Render the score
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    time.sleep(1 / SPEED)