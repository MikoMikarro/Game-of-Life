import pygame,sys
from pygame.locals import *
import time
cells = [160,90]
size = 10
pressed = False
windowSurface = pygame.display.set_mode((cells[0]*size, cells[1]*size),16)
windowSurface.fill((0,0,0))
pygame.init()
life_c = [2,3,5,6,7,8]
reviv_c = [3,6,7,8]
life = []
for i in range(cells[0]):
    life.append([])
    for l in range(cells[1]):
        life[i].append(0)
clear_one = []
def frame():
    clear_one = []
    for i in range(cells[0]):
        clear_one.append([])
        for l in range(cells[1]):
            clear_one[i].append(0)
    for i in range(cells[0]):
        for l in range(cells[1]):
            neigh = 0
            for k in range(3):
                for n in range(3):
                    try:
                        if (n,k) != (1,1)and life[i+k-1][l+n-1] == 1:
                            neigh+=1
                    except IndexError:
                        pass
            if life[i][l]== 0:
                if neigh in reviv_c:
                    clear_one[i][l] = 1
            elif life[i][l]==1:
                if neigh in life_c:
                    clear_one[i][l] = 1
            else:
                print("Fatal error")
                pygame.quit()
                sys.exit()
    return clear_one
def change(val):
    cx,cy = pygame.mouse.get_pos()
    try:
        if val:
            life[cx//size][cy//size] = 1
        else:
            life[cx//size][cy//size] = 0
    except IndexError:
        pass
def show():
    for i in range(cells[0]):
        for l in range(cells[1]):
            if life[i][l] == 1:
                pygame.draw.rect(windowSurface,(255,255,255),(i*size,l*size,size,size))
play = False
t = time.clock()
delay = .025
while True:
    if play == True and time.clock()-t > delay:
        life = frame()
        t = time.clock()
    LMB,MMB,RMB = pygame.mouse.get_pressed()
    if LMB and not RMB:
        change(True)
        play = False
    if RMB and not LMB:
        change(False)
        play = False
    if MMB:
        play = True
    show()
    for event in pygame.event.get():
        if event == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
    windowSurface.fill((0,0,0))
