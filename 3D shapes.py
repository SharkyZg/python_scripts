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

# Rotation
X_ROTATION = 0.01
Y_ROTATION = 0.01

# Set up the starting rotation angles
rotation_x = math.pi / 2
rotation_y = math.pi / 4

def project_vertices(vertices, rotation_x, rotation_y):
    projected_vertices = []
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

       # Perspective projection (divide by z-coordinate to get 2D coordinates)
        factor = 4 / (z_projected + 5)  # adjust this value for better perspective effect
        projected_x = int(x_projected * factor * 100 + SCREEN_WIDTH / 2)
        projected_y = int(y_projected * factor * 100 + SCREEN_HEIGHT / 2)

        projected_vertices.append({'2D vertices': (projected_x, projected_y), 'z_projected': z_projected})

    return projected_vertices


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

    projected_vertices = project_vertices(SHAPE[0], rotation_x, rotation_y)

    # Create a list to store the polygons to draw with their average Z-coordinate
    polygons_to_draw = []
    
    for face in SHAPE[1]:
        v1, v2, v3, color = face

        rotated_v1 = project_vertices([v1], rotation_x, rotation_y)[0]
        rotated_v2 = project_vertices([v2], rotation_x, rotation_y)[0]
        rotated_v3 = project_vertices([v3], rotation_x, rotation_y)[0]

        # Calculate the average Z-coordinate of the polygon
        avg_z = (rotated_v1['z_projected'] + rotated_v2['z_projected'] + rotated_v3['z_projected']) / 3

        projected_v1 = rotated_v1['2D vertices']
        projected_v2 = rotated_v2['2D vertices']
        projected_v3 = rotated_v3['2D vertices']

        polygons_to_draw.append([avg_z, [projected_v1, projected_v2, projected_v3], color])

    # Sort the polygons by their average Z-coordinate (depth)
    polygons_to_draw.sort(reverse=True)

    # Draw the polygons in the correct order
    for polygon in polygons_to_draw:
        pygame.draw.polygon(screen, polygon[2], polygon[1])

    # Update the screen
    pygame.display.flip()

    # wait for 0.1 sec
    pygame.time.delay(DELAY)

# Quit Pygame
pygame.quit()
