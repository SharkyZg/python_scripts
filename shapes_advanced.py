import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import geometry_shapes_adv

def Cube():

    glBegin(GL_QUADS)

    for face in geometry_shapes_adv.CUBE[1]:
        
        glColor3fv(face[4])
        glVertex3fv(face[0])
        glVertex3fv(face[1])
        glVertex3fv(face[2])
        glVertex3fv(face[3])
    
    glEnd()

def Pyramid():

    glBegin(GL_QUADS)
    # Base
    glColor3f(1, 0, 0)  # Red
    glVertex3f(-1, -1, 0)
    glVertex3f(1, -1, 0)
    glVertex3f(1, 1, 0)
    glVertex3f(-1, 1, 0)

    glEnd()

    glBegin(GL_TRIANGLES)
    # Front face
    glColor3f(0, 1, 0)  # Green
    glVertex3f(-1, -1, 0)
    glVertex3f(1, -1, 0)
    glVertex3f(0, 0, 1)

    # Right face
    glColor3f(0, 0, 1)  # Blue
    glVertex3f(1, -1, 0)
    glVertex3f(1, 1, 0)
    glVertex3f(0, 0, 1)

    # Back face
    glColor3f(1, 1, 0)  # Yellow
    glVertex3f(1, 1, 0)
    glVertex3f(-1, 1, 0)
    glVertex3f(0, 0, 1)

    # Left face
    glColor3f(1, 0, 1)  # Magenta
    glVertex3f(-1, 1, 0)
    glVertex3f(-1, -1, 0)
    glVertex3f(0, 0, 1)
    
    glEnd()

def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0,0.0, -5)

    glEnable(GL_DEPTH_TEST)  # Enable depth testing

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 3, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Pyramid()
        pygame.display.flip()
        pygame.time.wait(10)

main()