import pytest
import math
import numpy as np
from geometry_shapes import *
import shapes_advanced
from z_buffer import *

def test_project_vertices():
    vertices = [[1, 2, 3], [4, 5, 6]]
    projected_vertices = shapes_advanced.project_vertices(vertices)
    assert len(projected_vertices) == 2
    for vertex in projected_vertices:
        assert isinstance(vertex, list)
        assert len(vertex) == 3

def test_z_buffer_setup():
    z_buffer = ZBuffer(640, 480)
    assert z_buffer.width == 640
    assert z_buffer.height == 480

def test_rotate_vertices():
    vertices = [[1, 2, 3], [4, 5, 6]]
    rotation_x = math.pi / 2
    rotation_y = math.pi / 4
    rotated_vertices = shapes_advanced.rotate_vertices(vertices, rotation_x, rotation_y)
    assert len(rotated_vertices) == 2
    for vertex in rotated_vertices:
        assert isinstance(vertex, list)
        assert len(vertex) == 3
