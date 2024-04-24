import pygame
import math
import numpy as np
from geometry_shapes import *

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

# Set up the rotation angles
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
        x_projected = x_rotated * math.cos(rotation_y) + z_rotated * math.sin(rotation_y)
        y_projected = y_rotated
        z_projected = -x_rotated * math.sin(rotation_y) + z_rotated * math.cos(rotation_y)

        # Project onto 2D plane (ignore Z coordinate)
        projected_x = int(x_projected * 100 + SCREEN_WIDTH / 2)
        projected_y = int(y_projected * 100 + SCREEN_HEIGHT / 2)

        rotated_vertices.append({'2D vertices': (projected_x, projected_y), 'z_projected': z_projected})

    return rotated_vertices


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
    rotation_x += 0.01
    rotation_y += 0.01
    if rotation_x > 2 * math.pi:
        rotation_x = 0
    if rotation_y > 2 * math.pi:
        rotation_y = 0

    rotated_vertices = rotate_vertices(SHAPE[0], rotation_x, rotation_y)

    for_drawing = []
    # collect the polygons to draw with depth for painter's algorithm order
    for face in SHAPE[1]:
        v1, v2, v3, color = face

        rotated_v1 = rotate_vertices([v1], rotation_x, rotation_y)[0]
        rotated_v2 = rotate_vertices([v2], rotation_x, rotation_y)[0]
        rotated_v3 = rotate_vertices([v3], rotation_x, rotation_y)[0]

        min_z = min(rotated_v1['z_projected'], rotated_v2['z_projected'], rotated_v3['z_projected'])
        max_z = max(rotated_v1['z_projected'], rotated_v2['z_projected'], rotated_v3['z_projected'])

        projected_v1 = rotated_v1['2D vertices']
        projected_v2 = rotated_v2['2D vertices']
        projected_v3 = rotated_v3['2D vertices']

        for_drawing.append([min_z, max_z, [projected_v1, projected_v2, projected_v3], color])
    
    # sort the polygons to draw by depth
    for_drawing = sorted(for_drawing, key=lambda x: (x[0] + x[1]) / 2, reverse=True)
        
    for polygon_to_draw in for_drawing:
        pygame.draw.polygon(screen, polygon_to_draw[3], polygon_to_draw[2])

    # Update the screen
    pygame.display.flip()

    # wait for 0.1 sec
    pygame.time.delay(DELAY)

# Quit Pygame
pygame.quit()