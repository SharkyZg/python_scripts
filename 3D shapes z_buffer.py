import pygame
import math
import numpy as np
from geometry_shapes import *
from z_buffer import *

# Initialize Pygame
pygame.init()

# Set up the screen dimensions
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Define shape (PYRAMID or CUBE)
SHAPE = CUBE

# Delay in ms
DELAY = 10

# Rotation
X_ROTATION = 0.01
Y_ROTATION = 0.01

# Set up the starting rotation angles
rotation_x = math.pi / 2
rotation_y = math.pi / 4

def rotate_vertices(vertices, rotation_x, rotation_y):
    rotated_vertices = []
    for vertex in vertices:
        x, y, z = vertex

        # Rotate around X axis
        x_rotated = x
        y_rotated = y * math.cos(rotation_x) - z * math.sin(rotation_x)
        z_rotated = y * math.sin(rotation_x) + z * math.cos(rotation_x)

        # Rotate around Y axis
        x_rotated = x_rotated * math.cos(rotation_y) + z_rotated * math.sin(rotation_y)
        y_rotated = y_rotated
        z_rotated = -x_rotated * math.sin(rotation_y) + z_rotated * math.cos(rotation_y)

        rotated_vertices.append({'x': x_rotated, 'y': y_rotated, 'z': z_rotated})

    return rotated_vertices

z_buffer = ZBuffer(screen_width, screen_height)

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Rotate the geometry vertices
    rotation_x += X_ROTATION
    rotation_y += Y_ROTATION
    if rotation_x > 2 * math.pi:
        rotation_x = 0
    if rotation_y > 2 * math.pi:
        rotation_y = 0
    
    polygons = np.empty()
    for face in SHAPE[1]:
        v1, v2, v3, color = face

        rotated_v1 = rotate_vertices([v1], rotation_x, rotation_y)
        rotated_v2 = rotate_vertices([v2], rotation_x, rotation_y)
        rotated_v3 = rotate_vertices([v3], rotation_x, rotation_y)
        polygons.append([rotated_v1, rotated_v2, rotated_v3])

    # Draw with the z_buffer algorithm
    screen.fill((0, 0, 0))
    z_buffer.clear()

    render_polygon(polygons, z_buffer, color)
    
    # Update the screen
    pygame.display.flip()

    # wait for 0.1 sec
    pygame.time.delay(DELAY)

# Quit Pygame
pygame.quit()
