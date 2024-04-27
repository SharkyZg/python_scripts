import pygame
import math
import numpy as np
from geometry_shapes import *

# Set up the screen dimensions
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# Define shape (PYRAMID or CUBE)
SHAPE = CUBE

# Delay in ms
DELAY = 10

# Rotation
X_ROTATION = 0.01
Y_ROTATION = 0.01

def render_polygon(screen, polygons, z_buffer):
    pixel_array = pygame.PixelArray(screen)
    for polygon in polygons:
        color = polygon['color']
        sides = polygon['sides']
        vertices_2d = sides[:][:2]
        min_x, max_x, min_y, max_y = bounding_box(vertices_2d)
        # print(f"min_x: {min_x}, max_x: {max_x}, min_y: {min_y}, max_y: {max_y}")
        z_avg = np.array(sides[:][2]).mean()
        

        for y in range(int(min_y), int(max_y) + 1):
            for x in range(int(min_x), int(max_x) + 1):
                if z_buffer.test_and_set(x, y, z_avg):
                    pixel_array[x, y] = color
                    # print(f"x: {x}, y: {y}, z_avg: {z_avg}, color: {color}")
    pixel_array.close()

def calculate_sides_and_extract_color(rotation_x, rotation_y):
    polygons = []
    for face in SHAPE[1]:
        v1, v2, v3, color = face

        # Rotate the vertices
        rotated_v1, rotated_v2, rotated_v3 = rotate_polygon(v1, v2, v3, rotation_x, rotation_y)

        # Project the vertices
        projected_v1, projected_v2, projected_v3 = project_polygon(rotated_v1, rotated_v2, rotated_v3)

        polygons.append({'sides': [projected_v1, projected_v2, projected_v3], 'color': color})

    return polygons

def rotate_polygon(v1, v2, v3, rotation_x, rotation_y):
    # Rotate the vertices
    rotated_v1 = rotate_vertices([v1], rotation_x, rotation_y)
    rotated_v2 = rotate_vertices([v2], rotation_x, rotation_y)
    rotated_v3 = rotate_vertices([v3], rotation_x, rotation_y)
    return rotated_v1, rotated_v2, rotated_v3

def rotate_vertices(vertices, rotation_x, rotation_y):
    rotated_vertices = []
    for vertex in vertices:

        # Rotate around X and Y axis
        veretex_x_rotated = rotate_around_x_axis(vertex, rotation_x)
        vertex_x_y_rotated = rotate_around_y_axis(veretex_x_rotated, rotation_y)

        rotated_vertices.append(vertex_x_y_rotated.tolist())

    return rotated_vertices

def rotate_around_x_axis(vertex, rotation_x):
    rotation_x_matrix = np.array([[1, 0, 0], 
                                [0, math.cos(rotation_x), -math.sin(rotation_x)], 
                                [0, math.sin(rotation_x), math.cos(rotation_x)]])
    x_rotated = np.dot(vertex, rotation_x_matrix)
    return x_rotated

def rotate_around_y_axis(veretex_x_rotated, rotation_y):
    rotation_y_matrix = np.array([[math.cos(rotation_y), 0, math.sin(rotation_y)], 
                                [0, 1, 0], 
                                [-math.sin(rotation_y), 0, math.cos(rotation_y)]])
    x_and_y_rotated = np.dot(veretex_x_rotated, rotation_y_matrix)
    return x_and_y_rotated

def project_polygon(rotated_v1, rotated_v2, rotated_v3):
    # Rotate the vertices
    projected_v1 = project_vertices(rotated_v1)
    projected_v2 = project_vertices(rotated_v2)
    projected_v3 = project_vertices(rotated_v3)
    return projected_v1, projected_v2, projected_v3

def project_vertices(vertices):
        projected_vertices = []
        for vertex in vertices:
            x, y, z = vertex
            x_projected = int(x * 100 + SCREEN_WIDTH / 2)
            y_projected = int(y * 100 + SCREEN_HEIGHT / 2)
            z_projected = int(z * 100 + SCREEN_HEIGHT / 2)
            projected_vertices.append([x_projected, y_projected, z_projected])
        return projected_vertices

def rotate_angles(rotation_x, rotation_y):
    rotation_x += X_ROTATION
    rotation_y += Y_ROTATION
    if rotation_x > 2 * math.pi:
        rotation_x = 0
    if rotation_y > 2 * math.pi:
        rotation_y = 0
    return rotation_x, rotation_y

def bounding_box(vertices):
    vertices = np.array(vertices)
    min_x = vertices[0].min()
    max_x = vertices[0].max()
    min_y = vertices[1].min()
    max_y = vertices[1].max()
    return min_x, max_x, min_y, max_y

class ZBuffer:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.buffer = np.full((height, width), -float('inf'), dtype=np.float32)

    def clear(self):
        self.buffer.fill(-float('inf'))

    def test_and_set(self, x: int, y: int, z: float) -> bool:
        if z > self.buffer[x, y]:
            self.buffer[x, y] = z
            return True
        return False

    def get_z_value(self, x: int, y: int) -> float:
        return self.buffer[y, x]

# Main loop
def main():
    # Initialize Pygame
    pygame.init()


    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    z_buffer = ZBuffer(SCREEN_WIDTH, SCREEN_HEIGHT)



    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen
        screen.fill((0, 0, 0))

        # Set up the starting rotation angles
        rotation_x = math.pi / 2
        rotation_y = math.pi / 4

        # Rotate the geometry vertices
        rotation_x , rotation_y = rotate_angles(rotation_x, rotation_y)

        # Calculate the polygons coordinates
        sides_and_color = calculate_sides_and_extract_color(rotation_x, rotation_y)

        # Draw with the z_buffer algorithm
        screen.fill((0, 0, 0))
        z_buffer.clear()
        render_polygon(screen, sides_and_color, z_buffer)
        
        # Update the screen
        pygame.display.flip()

        # wait for 0.1 sec
        pygame.time.delay(DELAY)

    # Quit Pygame
    pygame.quit()

if __name__ == "__main__": main()