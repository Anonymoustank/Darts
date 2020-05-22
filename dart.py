import pygame as pg

#red has y-coordinates from 161 to 230, both inclusive
#red has x-coordinates from 152 to 224, both inclusive

#black has y-coordinates from 184 to 207, both inclusive
#black has x-coordinates from 175 to 198, both inclusive

import time

size = 10 #ball size

dot_x = 187

dot_y = 195

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

def give_points():

    global turns

    turns += 1

    scored = myfont.render(str(points) + " Points", True, (WHITE))

    screen.blit(scored, (0,0))

    if turns == 2:
        scored = myfont.render(str(points) + " Points", True, (WHITE))
        screen.blit(scored, (0,0))
        pg.display.update()
        running = False

dict = {} #stores all darts created

def update_board():
    global board
    board = pg.image.load("Dart Board.png")

    board = pg.transform.scale(board, (750,750))

    screen.blit(board, (-100, -140)) #load and display the board

    if len(dict) != 0:
        for dart_name in dict:
            exec('dart_name = pg.image.load("Dart.png")', globals())
            exec('dart_name = pg.transform.scale(dart_name, (30, 30))')
            exec('screen.blit(dart_name, dict[dart_name])')
    
    pg.display.update()

update_board()

def dot_move():
    screen.blit(dot, (dot_x, dot_y))
    update_board()
    pg.display.update()

dart_1 = pg.image.load("Dart.png")
dart_1 = pg.transform.scale(dart_1, (30, 30))
screen.blit(dart_1, (2000, 200))
pg.display.update()


while running == True:
    keys = pg.key.get_pressed()
    if keys[pg.K_w]:
        dot_y -= 1
        dot_move()
    if keys[pg.K_s]:
        dot_y += 1
        dot_move()
    if keys[pg.K_d]:
        dot_x += 1
        dot_move()
    if keys[pg.K_a]:
        dot_x -= 1
        dot_move()

    ev = pg.event.get()

    for event in ev:
        if event.type == pg.QUIT: #when the x button is clicked, the game stops running
            running = False
        if event.type == pg.MOUSEBUTTONUP: #handle click
            dict = {}
            if dart_num > 1:
                exec('dart_name = None')
            else:
                exec('dart_1 = None')
            x = dot_x
            y = dot_y
            dart_name = "dart" + str(dart_num)
            exec('dart_name = pg.image.load("Dart.png")')
            exec('dart_name = pg.transform.scale(dart_name, (30, 30))')
            exec('screen.blit(dart_name, (x + 5, y - 25))') #make dart go to y coordinate of mouse minus 30, so it lines up with the cursor
            exec('dict[dart_name] = x+5, y-25')
            pg.display.update()
            dart_num += 1
            if dot_y >= 184 and dot_y <= 207 and dot_x >=175 and dot_x <= 198:
                points += 50
            elif 230 >= dot_y >= 161 and 224 >= dot_x >= 152:
                points += 25
            give_points()

    dot = pg.image.load("dot.png")

    dot = pg.transform.scale(dot, (10, 10))

    screen.blit(dot, (dot_x,dot_y)) #load and display the dot

    pg.display.update()

    clock.tick(FPS)

pg.display.quit()
pg.quit()




    
