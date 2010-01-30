#!/usr/bin/env python2.6

import sys
from time import clock

from p2t import *
from point_set import dude

# PyGame Constants
import pygame
from pygame.gfxdraw import trigon
from pygame.locals import *
from pygame import Color


def load_points(file_name):
    infile = open(file_name, "r")
    points = []
    while infile:
        line = infile.readline()
        s = line.split()
        if len(s) == 0:
            break
        points.append((float(s[0]), float(s[1])))
    return points

def main(file_name, translate, zoom):
    
    SCREEN_SIZE = 800,600
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE,0,8)
    pygame.display.set_caption('poly2tri demo')
    
    black = Color(0,0,0)
    red = Color(255, 0, 0)
    screen.fill(black)
    
    points = load_points(file_name)
    polyline = []  
           
    for p in points:
        polyline.append(Point(p[0]*zoom + translate[0],p[1]*zoom + translate[1]))

    cdt = CDT(polyline)
    
    t0 = clock()
    cdt.triangulate()
    print "Elapsed time (ms) = " + str(clock()*1000.0)
    triangles = cdt.triangles
        
    # The Main Event Loop
    done = False
    while not done:
        # Drawing:
        for t in triangles:
          trigon(screen, int(t.a.x), int(t.a.y), int(t.b.x), int(t.b.y), int(t.c.x), int(t.c.y), red)
        # Update the screen
        pygame.display.update()
            
        # Event Handling:
        events = pygame.event.get( )
        for e in events:
            if( e.type == QUIT ):
                done = True
                break
            elif (e.type == KEYDOWN):
                if( e.key == K_ESCAPE ):
                    done = True
                    break
                if( e.key == K_f ):
                    pygame.display.toggle_fullscreen()

    return

if __name__=="__main__":
    if len(sys.argv) == 5:
      file_name = sys.argv[1]
      tx = float(sys.argv[2])
      ty = float(sys.argv[3])
      zoom = float(sys.argv[4])
      main(file_name, [tx, ty], zoom)
      exit()
    
    print
    print("  Usage: filename translate-x translate-y zoom")
    print("Example: python test.py data/dude.dat 100 -200 1")
    print("         python test.py data/nazca_monkey.dat 400 300 4.5")  

