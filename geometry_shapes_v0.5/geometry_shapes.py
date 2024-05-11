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