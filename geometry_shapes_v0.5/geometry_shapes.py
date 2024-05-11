import numpy as np

# Colors for the faces
COLORS = [
    [1, 0, 0],   # Red
    [0, 1, 0],   # Green
    [0, 0, 1],   # Blue
    [1, 1, 0],   # Yellow
    [1, 0, 1],   # Magenta
    [0, 1, 1]    # Cyan
]

# Normalized vertices of the cube
CUBE_VERTICES = [
    [-1, -1,  1],
    [ 1, -1,  1],
    [ 1,  1,  1],
    [-1,  1,  1],
    [-1, -1, -1],
    [ 1, -1, -1],
    [ 1,  1, -1],
    [-1,  1, -1]
]

# Faces of the cube
CUBE_FACES = [
    [0, 1, 2, 3],
    [4, 5, 6, 7],
    [0, 1, 5, 4],
    [1, 2, 6, 5],
    [2, 3, 7, 6],
    [3, 0, 4, 7]
]

# Normalized vertices of the pyramid
PYRAMID_VERTICES = [
    [-1, -1, 0],  # 0
    [1, -1, 0],  # 1
    [1, 1, 0],    # 2
    [-1, 1, 0],  # 3
    [0, 0, 2]     # 4
]

PYRAMID_FACES = [
    [0, 1, 2, 3], 
    [0, 1, 4], 
    [1, 2, 4], 
    [2, 3, 4], 
    [3, 0, 4]
]

# Octahedron vertices (centered at the origin)
OCTAHEDRON_VERTICES = [
    [0, 0, 1],  # Top vertex
    [0, 0, -1], # Bottom vertex
    [1, 0, 0],  # Front vertex on XY-plane
    [-1, 0, 0], # Back vertex on XY-plane
    [0, 1, 0],  # Right vertex on XY-plane
    [0, -1, 0], # Left vertex on XY-plane
]

# Octahedron faces (8 triangles)
OCTAHEDRON_FACES = [
    [0, 2, 4], [0, 4, 3], [0, 3, 5], [0, 5, 2], # Upper four triangles
    [1, 4, 2], [1, 3, 4], [1, 5, 3], [1, 2, 5]  # Lower four triangles
]

def create_sphere(radius, segments):
    vertices = []
    faces = []

    # Create vertices
    for i in range(segments + 1):
        lat = np.pi * i / segments  # from 0 to pi
        for j in range(segments + 1):
            lon = 2 * np.pi * j / segments  # from 0 to 2pi
            x = radius * np.sin(lat) * np.cos(lon)
            y = radius * np.sin(lat) * np.sin(lon)
            z = radius * np.cos(lat)
            vertices.append([x, y, z])

    # Create faces
    for i in range(segments):
        for j in range(segments):
            a = i * (segments + 1) + j
            b = a + segments + 1
            faces.append([a, b, a + 1])
            faces.append([b, b + 1, a + 1])

    return vertices, faces

SPHERE_VERTICES, SPHERE_FACES = create_sphere(1, 16)  # Radius 1, 16 segments for decent detail

# Icosahedron vertices
phi = (1 + np.sqrt(5)) / 2  # Golden ratio
ICOSAHEDRON_VERTICES = [
    [-1,  phi,  0],
    [ 1,  phi,  0],
    [-1, -phi,  0],
    [ 1, -phi,  0],
    [ 0, -1,  phi],
    [ 0,  1,  phi],
    [ 0, -1, -phi],
    [ 0,  1, -phi],
    [ phi,  0, -1],
    [ phi,  0,  1],
    [-phi,  0, -1],
    [-phi,  0,  1]
]

# Icosahedron faces
ICOSAHEDRON_FACES = [
    [0, 11, 5], [0, 5, 1], [0, 1, 7], [0, 7, 10], [0, 10, 11],
    [1, 5, 9], [5, 11, 4], [11, 10, 2], [10, 7, 6], [7, 1, 8],
    [3, 9, 4], [3, 4, 2], [3, 2, 6], [3, 6, 8], [3, 8, 9],
    [4, 9, 5], [2, 4, 11], [6, 2, 10], [8, 6, 7], [9, 8, 1]
]

# Tetrahedron vertices
TETRAHEDRON_VERTICES = [
    [1, 1, 1],
    [-1, -1, 1],
    [-1, 1, -1],
    [1, -1, -1]
]

# Tetrahedron faces
TETRAHEDRON_FACES = [
    [0, 1, 2],
    [0, 3, 1],
    [0, 2, 3],
    [1, 3, 2]
]