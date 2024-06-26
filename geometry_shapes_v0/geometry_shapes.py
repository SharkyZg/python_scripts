# Define some colors
COLORS = {
    'RED': (255, 0, 0),
    'GREEN': (0, 255, 0),
    'BLUE': (0, 0, 255),
    'YELLOW': (255, 255, 0),
    'PURPLE': (255, 0, 255)
}

# Define the pyramid vertice
PYRAMID_VERTICES = [
    [-1, -1, 0],  # vertex 0: bottom left
    [1, -1, 0],  # vertex 1: bottom right
    [1, 1, 0],   # vertex 2: top right
    [-1, 1, 0],  # vertex 3: top left
    [0, 0, 2]     # vertex 4: apex (top)
]

# Define the faces of the pyramid
PYRAMID_FACES = [
    [PYRAMID_VERTICES[0], PYRAMID_VERTICES[1], PYRAMID_VERTICES[2], COLORS['PURPLE']],
    [PYRAMID_VERTICES[0], PYRAMID_VERTICES[2], PYRAMID_VERTICES[3], COLORS['PURPLE']],
    [PYRAMID_VERTICES[0], PYRAMID_VERTICES[1], PYRAMID_VERTICES[4], COLORS['RED']],
    [PYRAMID_VERTICES[1], PYRAMID_VERTICES[2], PYRAMID_VERTICES[4], COLORS['GREEN']],
    [PYRAMID_VERTICES[2], PYRAMID_VERTICES[3], PYRAMID_VERTICES[4], COLORS['BLUE']],
    [PYRAMID_VERTICES[3], PYRAMID_VERTICES[0], PYRAMID_VERTICES[4], COLORS['YELLOW']]
]

CUBE_VERTICES = [
    [-1, -1, -1],
    [1, -1, -1],
    [1, 1, -1],
    [-1, 1, -1],
    [-1, -1, 1],
    [1, -1, 1],
    [1, 1, 1],
    [-1, 1, 1]
]

CUBE_FACES = [
    [CUBE_VERTICES[0], CUBE_VERTICES[1], CUBE_VERTICES[2], COLORS['PURPLE']],
    [CUBE_VERTICES[0], CUBE_VERTICES[2], CUBE_VERTICES[3], COLORS['PURPLE']],
    [CUBE_VERTICES[4], CUBE_VERTICES[5], CUBE_VERTICES[6], COLORS['PURPLE']],
    [CUBE_VERTICES[4], CUBE_VERTICES[6], CUBE_VERTICES[7], COLORS['PURPLE']],
    [CUBE_VERTICES[0], CUBE_VERTICES[1], CUBE_VERTICES[5], COLORS['RED']],
    [CUBE_VERTICES[0], CUBE_VERTICES[5], CUBE_VERTICES[4], COLORS['RED']],
    [CUBE_VERTICES[1], CUBE_VERTICES[2], CUBE_VERTICES[6], COLORS['GREEN']],
    [CUBE_VERTICES[1], CUBE_VERTICES[6], CUBE_VERTICES[5], COLORS['GREEN']],
    [CUBE_VERTICES[2], CUBE_VERTICES[3], CUBE_VERTICES[7], COLORS['BLUE']],
    [CUBE_VERTICES[2], CUBE_VERTICES[7], CUBE_VERTICES[6], COLORS['BLUE']],
    [CUBE_VERTICES[0], CUBE_VERTICES[3], CUBE_VERTICES[7], COLORS['YELLOW']],
    [CUBE_VERTICES[0], CUBE_VERTICES[7], CUBE_VERTICES[4], COLORS['YELLOW']]
]

# Shapes
PYRAMID = (PYRAMID_VERTICES, PYRAMID_FACES)
CUBE = (CUBE_VERTICES, CUBE_FACES)