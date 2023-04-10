import math
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

angle=[10,20,30,40,50]
rot_angle=30
Width=200
Height=220


theta=1
y_trans=1
def draw_teapot(y_trans):
    global motion

    global y_translate
    global theta
    global up_down
    global rot_angle

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glColor(1,1,1)
    glTranslate(0, -3, -4)
    glRotate(90, 1, 0, 0)
    glutSolidCylinder(4, 1, 360, 1)

    glRotate(-90, 1, 0, 0)
    glPushMatrix()
    glColor3d(1, 0, 1)

    glPushMatrix()
    x = 3.2 * math.cos(angle[0])
    Z = 3.2 * math.sin(angle[0])
    glTranslate(x, 0,Z )
    glTranslate(0, theta, 0)
    glRotate(rot_angle,0,1,0)
    glutWireTeapot(.45)
    glRotate(90,1,0,0)
    glutSolidCylinder(.03, y_trans, 360, 1)
    glPopMatrix()

    glPushMatrix()
    x = 3.2* math.cos(angle[1])
    Z= 3.2 * math.sin(angle[1])
    glTranslate(x, 0,Z )
    glTranslate(0, theta+.02, 0)
    glRotate(rot_angle,0,1,0)
    glutWireTeapot(.45)
    glRotate(90, 1, 0, 0)
    glutSolidCylinder(.03, y_trans+.02, 360, 1)
    glPopMatrix()

    glPushMatrix()
    x = 3.2 * math.cos(angle[2])
    Z = 3.2 * math.sin(angle[2])
    glTranslate(x, 0,Z )
    glTranslate(0, theta+.04, 0)
    glRotate(rot_angle,0,1,0)
    glutWireTeapot(.45)
    glRotate(90, 1, 0, 0)
    glutSolidCylinder(.03, y_trans+.04, 360, 1)
    glPopMatrix()

    glPushMatrix()
    x = 3.2 * math.cos(angle[3])
    Z = 3.2 * math.sin(angle[3])
    glTranslate(x, 0,Z )
    glTranslate(0, theta+.06, 0)
    glRotate(rot_angle,0,1,0)
    glutWireTeapot(.45)
    glRotate(90, 1, 0, 0)
    glutSolidCylinder(.03, y_trans+.06, 360, 1)
    glPopMatrix()

    glPushMatrix()
    x = 3.2 * math.cos(angle[4])
    Z = 3.2 * math.sin(angle[4])
    glTranslate(x, 0, Z)
    glTranslate(0, theta+.08, 0)
    glRotate(rot_angle,0,1,0)
    glutWireTeapot(.45)
    glRotate(90, 1, 0, 0)
    glutSolidCylinder(.03, y_trans+.08, 360, 1)
    glPopMatrix()
    glPopMatrix()

    if(theta>=1):
        motion=1

    elif (theta <= .3):
        motion = 0

    if (motion == 1):
        theta -= .002

    elif (motion == 0):
        theta += .002

    for i in range(0,5,1):
       angle[i] +=.006

    rot_angle+=1

def display():
    global y_trans
    global up_down

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(40, float(Width) / float(Height), 1, 20)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0, 1, 7, 0, 0, 0, 0, 1, -1)

    if (y_trans >= 1):
      up_down=1
    elif(y_trans<=.3):
        up_down=0
    if(up_down==1):
        y_trans -= .002
    elif(up_down==0):
        y_trans += .002

    draw_teapot(y_trans)
    glutSwapBuffers()

def game_timer(v):
    display()
    glutTimerFunc(3, game_timer, 1)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB |GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutInitWindowPosition(250, 50)
    glutCreateWindow(b"dansing teapot")
    glutDisplayFunc(display)
    # glEnable(GL_DEPTH_TEST)
    glutTimerFunc(1000, game_timer, 1)
    glutMainLoop()

if __name__ == "__main__":
  main()

