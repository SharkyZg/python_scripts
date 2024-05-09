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
    for face in geometry_shapes_adv.PYRAMID[1]:
        
        if len(face) == 5: 
            glBegin(GL_QUADS)
            glColor3fv(face[4]) 
            glVertex3fv(face[0]) 
            glVertex3fv(face[1]) 
            glVertex3fv(face[2]) 
            glVertex3fv(face[3]) 
            glEnd()

        else: 
            glBegin(GL_TRIANGLES)
            glColor3fv(face[3]) 
            glVertex3fv(face[0]) 
            glVertex3fv(face[1]) 
            glVertex3fv(face[2])
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

        glRotatef(1, 3, 6, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        pygame.time.wait(10)

main()