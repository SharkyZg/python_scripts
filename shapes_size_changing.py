import pygame
from pygame.locals import * 
from OpenGL.GL import *
from OpenGL.GLU import *

def Cube(t):
    vertices = [  
         [-(1 - 0.5 * t), -(1 - 0.5 * t),  (1 - 0.5 * t)],  
         [(1 - 0.5 * t), -(1 - 0.5 * t),  (1 - 0.5 * t)],  
         [(1 - 0.5 * t),  (1 - 0.5 * t),  (1 - 0.5 * t)],  
         [-(1 - 0.5 * t),  (1 - 0.5 * t),  (1 - 0.5 * t)],  

         [-(1 - 0.5 * t), -(1 - 0.5 * t), -(1 - 0.5 * t)],  
         [(1 - 0.5 * t), -(1 - 0.5 * t), -(1 - 0.5 * t)],  
         [(1 - 0.5 * t),  (1 - 0.5 * t), -(1 - 0.5 * t)],  
         [-(1 - 0.5 * t),  (1 - 0.5 * t), -(1 - 0.5 * t)]  
     ]

    glBegin(GL_QUADS)

    glColor3fv((1, 0, 0))
    glVertex3fv(vertices[0])
    glVertex3fv(vertices[1])
    glVertex3fv(vertices[2])
    glVertex3fv(vertices[3])

    glColor3fv((0, 1, 0))
    glVertex3fv(vertices[4])
    glVertex3fv(vertices[5])
    glVertex3fv(vertices[6])
    glVertex3fv(vertices[7])

    glColor3fv((0, 0, 1))
    glVertex3fv(vertices[0])
    glVertex3fv(vertices[1])
    glVertex3fv(vertices[5])
    glVertex3fv(vertices[4])

    glColor3fv((1, 1, 0))
    glVertex3fv(vertices[1])
    glVertex3fv(vertices[2])
    glVertex3fv(vertices[6])
    glVertex3fv(vertices[5])

    glColor3fv((1, 0, 1))
    glVertex3fv(vertices[2])
    glVertex3fv(vertices[3])
    glVertex3fv(vertices[7])
    glVertex3fv(vertices[6])

    glColor3fv((0, 1, 1))
    glVertex3fv(vertices[3])
    glVertex3fv(vertices[0])
    glVertex3fv(vertices[4])
    glVertex3fv(vertices[7])

    glEnd()

def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0,0.0, -5) 

    glEnable(GL_DEPTH_TEST)   # Enable depth testing

    t = 0
    shape_chage_rate = 0.003
    rotation_speed_x = 3
    rotation_speed_y = 6

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, rotation_speed_x, rotation_speed_y, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube(t)

        t += shape_chage_rate
        if t > 2:
            shape_chage_rate *= -1
            rotation_speed_x *= -1
            rotation_speed_y *= -1 
        elif t < -1:
            shape_chage_rate *= -1
            rotation_speed_x *= -1
            rotation_speed_y *= -1

        pygame.display.flip() 
        pygame.time.wait(10)

main()
