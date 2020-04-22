import pygame as pg

WIDTH = 1000

HEIGHT = WIDTH

FPS = 60

turns = 0

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
        end = myfont.render("Game Over", True, (WHITE))
        screen.blit(end, (750,750))
        running = False
        
    else:
        
        points_left = Label(root, text="You have " + str(501-points) + " left.")
        
        root.withdraw()

while running == True:

    clock.tick(FPS)
    
    board = pg.image.load("Dart Board.png")

    board = pg.transform.scale(board, (750,750))

    screen.fill(BLACK)

    screen.blit(board, (0, 0))

    pg.display.update()

    running = False



root.mainloop()
    
