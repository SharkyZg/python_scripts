import numpy as np
from geometry_shapes import *

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