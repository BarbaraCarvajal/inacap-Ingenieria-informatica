import pygame
import sys
import time

run = True
frameRate = 60
frameCount = 0
width = 640
height = 480
mouseX = 0
mouseY = 0
pmouseX = 0
pmouseY = 0
movedX = 0
movedY = 0

pygame.init()
canvas = pygame.display.set_mode([width, height], pygame.RESIZABLE)



def setTitle(title):
    pygame.display.set_caption(title)

def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            global run 
            run = False

def updateVariables():
    global width
    global height
    global mouseX
    global mouseY
    global pmouseX
    global pmouseY
    global movedX
    global movedY
    sz = pygame.display.get_window_size()
    width = sz[0]
    height = sz[1]
    mouse = pygame.mouse.get_pos()
    pmouseX = mouseX
    pmouseY = mouseY
    mouseX = mouse[0]
    mouseY = mouse[1]
    movedX = mouseX - pmouseX
    movedY = mouseY - pmouseY
    
def updateFrame():
    pygame.display.flip()
    time.sleep(1/frameRate)
    global frameCount
    frameCount+=1


def update():
    updateVariables()
    events()
    updateFrame()
    

def background(color):
        pygame.draw.rect(canvas, color, [0,0,width,height])


def rect(x, y, w, h, color="white"):
    pygame.draw.rect(canvas, color, (x, y, w, h))


def draw():
    background("light blue")
    rect(mouseX, mouseY, 100, 100)



while run:
    draw()
    update()

sys.exit()