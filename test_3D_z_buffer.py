import pytest
import math
import numpy as np
import geometry_shapes
import shapes_advanced
from z_buffer import *

vertices = geometry_shapes.CUBE_FACES[0][:3]

def test_project_vertices():
    projected_vertices = shapes_advanced.project_vertices(vertices)
    assert len(projected_vertices) == 3
    for vertex in projected_vertices:
        assert isinstance(vertex, list)
        assert len(vertex) == 3

def test_z_buffer_setup():
    z_buffer = ZBuffer(640, 480)
    assert z_buffer.width == 640
    assert z_buffer.height == 480

def test_rotate_vertices():
    rotation_x = math.pi / 2
    rotation_y = math.pi / 4
    rotated_vertices = shapes_advanced.rotate_vertices(vertices, rotation_x, rotation_y)
    assert len(rotated_vertices) == 3
    for vertex in rotated_vertices:
        assert isinstance(vertex, list)
        assert len(vertex) == 3

    rotated_vertices = np.array(rotated_vertices)
    
    rotation_x_matrix = np.array([[1, 0, 0], 
                                [0, math.cos(rotation_x), -math.sin(rotation_x)], 
                                [0, math.sin(rotation_x), math.cos(rotation_x)]])
    x_rotated = np.dot(vertices, rotation_x_matrix)

    rotation_y_matrix = np.array([[math.cos(rotation_y), 0, math.sin(rotation_y)], 
                                [0, 1, 0], 
                                [-math.sin(rotation_y), 0, math.cos(rotation_y)]])
    x_and_y_rotated = np.dot(x_rotated, rotation_y_matrix)

    assert np.array_equal(rotated_vertices, x_and_y_rotated)


