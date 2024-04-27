import numpy as np
import pygame

# Define the camera matrix (simplified perspective projection)
camera_matrix = np.array([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, -5],  # camera position (z=-5)
    [0, 0, 0, 1]
])

# Define the polygon vertices
CUBE_VERTICES = np.array([
    [-1, -1, -1, 1],
    [1, -1, -1, 1],
    [1, 1, -1, 1],
    [-1, 1, -1, 1],
    [-1, -1, 1, 1],
    [1, -1, 1, 1],
    [1, 1, 1, 1],
    [-1, 1, 1, 1]
])

def project_vertex(vertex, camera_matrix):
    projected_vertex = np.dot(camera_matrix, vertex)
    return projected_vertex[:2] / projected_vertex[3]

def render_polygon(polygons, z_buffer, color):
    for polygon in polygons:
        vertices_2d = [project_vertex(vertex, camera_matrix) for vertex in polygon]
        min_x, max_x, min_y, max_y = bounding_box(vertices_2d)

        for y in range(min_y, max_y + 1):
            for x in range(min_x, max_x + 1):
                z_values = [project_vertex(vertex, camera_matrix)[2] for vertex in polygon]
                z_avg = np.mean(z_values)
                if z_buffer.test_and_set(x, y, z_avg):
                    pygame.draw.rect(screen, color, (x, y, 1, 1))

def bounding_box(vertices):
    min_x = min(v[0] for v in vertices)
    max_x = max(v[0] for v in vertices)
    min_y = min(v[1] for v in vertices)
    max_y = max(v[1] for v in vertices)
    return min_x, max_x, min_y, max_y

pygame.init()
screen_width, screen_height = 640, 480
screen = pygame.display.set_mode((screen_width, screen_height))
z_buffer = ZBuffer(screen_width, screen_height)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    z_buffer.clear()

    render_polygon([CUBE_VERTICES], z_buffer, (255, 255, 255))

    pygame.display.flip()
    pygame.time.delay(1000)