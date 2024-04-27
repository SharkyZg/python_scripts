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

        rotated_vertices.append([x_rotated, y_rotated, z_rotated])

    return rotated_vertices

def project_vertices(vertices):
        projected_vertices = []
        for vertex in vertices:
            x, y, z = vertex
            x_projected = int(x * 100 + SCREEN_WIDTH / 2)
            y_projected = int(y * 100 + SCREEN_HEIGHT / 2)
            z_projected = int(z * 100 + SCREEN_HEIGHT / 2)
            projected_vertices.append([x_projected, y_projected, z_projected])
        return projected_vertices

def calculate_polygons(rotation_x, rotation_y):
    polygons = []
    for face in SHAPE[1]:
        v1, v2, v3, color = face

        # Rotate the vertices
        rotated_v1 = rotate_vertices([v1], rotation_x, rotation_y)
        rotated_v2 = rotate_vertices([v2], rotation_x, rotation_y)
        rotated_v3 = rotate_vertices([v3], rotation_x, rotation_y)

        # Project the vertices
        projected_v1 = project_vertices(rotated_v1)
        projected_v2 = project_vertices(rotated_v2)
        projected_v3 = project_vertices(rotated_v3)

        polygons.append([projected_v1, projected_v2, projected_v3])

    return polygons

def rotate_angles(rotation_x, rotation_y):
    rotation_x += X_ROTATION
    rotation_y += Y_ROTATION
    if rotation_x > 2 * math.pi:
        rotation_x = 0
    if rotation_y > 2 * math.pi:
        rotation_y = 0
    return rotation_x, rotation_y

z_buffer = ZBuffer(SCREEN_WIDTH, SCREEN_HEIGHT)

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
    rotation_x , rotation_y = rotate_angles(rotation_x, rotation_y)

    # Calculate the polygons coordinates
    polygons = calculate_polygons(rotation_x, rotation_y)

    # Draw with the z_buffer algorithm
    screen.fill((0, 0, 0))
    z_buffer.clear()
    render_polygon(screen, polygons, z_buffer, color)
    
    # Update the screen
    pygame.display.flip()

    # wait for 0.1 sec
    pygame.time.delay(DELAY)

# Quit Pygame
pygame.quit()
