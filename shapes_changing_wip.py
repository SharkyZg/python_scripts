import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

def CubeToSphere(t):
    vertices = []
    num_slices = 16
    num_stacks = 8

    # Generate vertices for the object
    for i in range(num_stacks + 1):
        z = (2 * i / num_stacks - 1)
        r = math.sqrt(1 - z ** 2)
        for j in range(num_slices + 1):  # Include an extra point to wrap around
            theta = 2 * math.pi * j / num_slices
            x = r * math.cos(theta) * (1 - t) + (t * math.cos(theta))
            y = r * math.sin(theta) * (1 - t) + (t * math.sin(theta))
            vertices.append([x, y, z])

    # Begin drawing quad strips and add color
    glBegin(GL_QUAD_STRIP)
    for i in range(num_stacks):
        for j in range(num_slices + 1):  # Complete the loop by including the first vertex
            glColor3f(i/num_stacks, j/num_slices, (i+j)/(num_stacks+num_slices))
            glVertex3fv(vertices[i * (num_slices + 1) + j])
            glVertex3fv(vertices[(i + 1) * (num_slices + 1) + j])
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)
    glEnable(GL_DEPTH_TEST)

    t = 0
    shape_change_rate = 0.003
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Rotate the object slightly on each frame
        glRotatef(1, 3, 6, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        CubeToSphere(t)

        # Change transformation over time
        t += shape_change_rate
        if t > 2:
            shape_change_rate *= -1
        elif t < -1:
            shape_change_rate *= -1

        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
