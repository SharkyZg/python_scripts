import numpy as np
import pygame

pygame.init()

class ZBuffer:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.buffer = np.full((height, width), -float('inf'), dtype=np.float32)

    def clear(self):
        self.buffer.fill(-float('inf'))

    def test_and_set(self, x: int, y: int, z: float) -> bool:
        if z > self.buffer[y, x]:
            self.buffer[y, x] = z
            return True
        return False

    def get_z_value(self, x: int, y: int) -> float:
        return self.buffer[y, x]

def project_vertex(vertex: np.ndarray, camera_matrix: np.ndarray) -> np.ndarray:
    """Project a 3D vertex onto the screen using the camera matrix"""
    return np.dot(camera_matrix, vertex)

def render_polygon(polygon: list, z_buffer: ZBuffer, color: tuple) -> None:
    """Render a polygon using the Z-buffer algorithm"""
    num_vertices = len(polygon)
    vertices_2d = [project_vertex(vertex, camera_matrix) for vertex in polygon]
    min_x, max_x, min_y, max_y = bounding_box(vertices_2d)

    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            z_values = [project_vertex(vertex, camera_matrix)[2] for vertex in polygon]
            z_avg = np.mean(z_values)
            if z_buffer.test_and_set(x, y, z_avg):
                # Draw the pixel
                pygame.draw.rect(screen, color, (x, y, 1, 1))

def bounding_box(vertices: list) -> tuple:
    """Compute the bounding box of a polygon"""
    min_x = min(vertex[0] for vertex in vertices)
    max_x = max(vertex[0] for vertex in vertices)
    min_y = min(vertex[1] for vertex in vertices)
    max_y = max(vertex[1] for vertex in vertices)
    return min_x, max_x, min_y, max_y

# Example usage
pygame.init()
screen_width, screen_height = 640, 480
screen = pygame.display.set_mode((screen_width, screen_height))

camera_matrix = np.array([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, -5],  # camera position (z=-5)
    [0, 0, 0, 1]
])

z_buffer = ZBuffer(screen_width, screen_height)

polygon = [
    np.array([-1, -1, 0]),
    np.array([1, -1, 0]),
    np.array([1, 1, 0]),
    np.array([-1, 1, 0])
]

render_polygon(polygon, z_buffer, (255, 255, 255))  # White color

pygame.display.flip()
pygame.time.delay(1000)
