import pygame as pg

import time

size = 10 #ball size

dart_num = 1 #number used in dart name

doing_animation = False

WIDTH = 380

HEIGHT = 400

points = 0

FPS = 60

turns = 1

pg.init()

screen = pg.display.set_mode((WIDTH, HEIGHT))

pg.display.set_caption("Darts!")

BLACK = (0, 0, 0)

WHITE = (255, 255, 255)

pg.display.update()

clock = pg.time.Clock()

myfont = pg.font.SysFont('Arial', 45)

running = True

def give_points(points):

    turns += 1

    scored = myfont.render(str(points) + " Points", True, (WHITE))

    screen.blit(scored, (0,0))

    if turns == 8:
        screen.fill(BLACK)
        scored = myfont.render(str(points) + " Points", True, (WHITE))
        screen.blit(scored, (0,0))
        end = myfont.render("Game Over", True, (WHITE))
        screen.blit(end, (750,750))
        pg.display.update()
        running = False

board = pg.image.load("Dart Board.png")

board = pg.transform.scale(board, (750,750))

screen.blit(board, (-100, -140)) #load and display the board
        

while running == True:

    ev = pg.event.get()

    for event in ev:
        if event.type == pg.QUIT: #when the x button is clicked, the game stops running
            running = False
        if event.type == pg.MOUSEBUTTONUP: #handle click
            pos = pg.mouse.get_pos()
            print(pos)
            x, y = pg.mouse.get_pos()
            dart_name = "dart" + str(dart_num)
            exec('dart_name = pg.image.load("Dart.png")')
            exec('dart_name = pg.transform.scale(dart_name, (30, 30))')
            exec('screen.blit(dart_name, (x, y - 30))') #make dart go to y coordinate of mouse minus 30, so it lines up with the cursor
            pg.display.update()
            dart_num += 1

    clock.tick(FPS)

    dot = pg.image.load("dot.png")

    dot = pg.transform.scale(dot, (10, 10))

    screen.blit(dot, (187,195)) #load and display the dot

    pg.display.update()

pg.display.quit()
pg.quit()




    
