import numpy as np
import pygame
from geometry_shapes import *
import statistics

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

def render_polygon(screen, polygons, z_buffer, color):
    for polygon in polygons:
        vertices_2d = polygon[:][:2]
        min_x, max_x, min_y, max_y = bounding_box(vertices_2d)
        print(f"min_x: {min_x}, max_x: {max_x}, min_y: {min_y}, max_y: {max_y}")
        z_avg = np.array(polygon[:][2]).mean()
        for y in range(int(min_y), int(max_y) + 1):
            for x in range(int(min_x), int(max_x) + 1):
                if z_buffer.test_and_set(x, y, z_avg):
                    pygame.draw.rect(screen, color, pygame.Rect(x, y, 1, 1))
                    print(f"x: {x}, y: {y}, z_avg: {z_avg}, color: {color}")

def bounding_box(vertices):
    vertices = np.array(vertices)
    min_x = vertices[0].min()
    max_x = vertices[0].max()
    min_y = vertices[1].min()
    max_y = vertices[1].max()
    return min_x, max_x, min_y, max_y