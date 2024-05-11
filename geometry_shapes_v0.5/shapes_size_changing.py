import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from geometry_shapes import *

def draw_shape(vertices, faces, scale):
    for i, face in enumerate(faces):
        glBegin(GL_TRIANGLES if len(face) == 3 else GL_QUADS if len(face) == 4 else GL_POLYGON)
        glColor3fv(COLORS[i % len(COLORS)])  # Cycle through colors
        for vertex in face:
            glVertex3fv([scale * x for x in vertices[vertex]])
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
    rotation_speed_x = 3
    rotation_speed_y = 6
    shapes = ['cube', 'pyramid', 'octahedron', 'sphere']  # Including the sphere
    current_shape = 0  # Start with the cube

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    current_shape = (current_shape + 1) % len(shapes)

        glRotatef(1, rotation_speed_x, rotation_speed_y, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        scale = 1 - 0.5 * t

        if shapes[current_shape] == 'cube':
            draw_shape(CUBE_VERTICES, CUBE_FACES, scale)
        elif shapes[current_shape] == 'pyramid':
            draw_shape(PYRAMID_VERTICES, PYRAMID_FACES, scale)
        elif shapes[current_shape] == 'octahedron':
            draw_shape(OCTAHEDRON_VERTICES, OCTAHEDRON_FACES, scale)
        elif shapes[current_shape] == 'sphere':
            draw_shape(SPHERE_VERTICES, SPHERE_FACES, scale)

        t += shape_change_rate
        if t > 2 or t < -1:
            shape_change_rate *= -1
            rotation_speed_x *= -1
            rotation_speed_y *= -1

        pygame.display.flip()
        pygame.time.wait(10)

main()
