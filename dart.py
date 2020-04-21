import pygame as pg
from tkinter import *
from tkinter.simpledialog import askstring

root = Tk()

WIDTH = 1000

HEIGHT = WIDTH

FPS = 60

turns = 0

pg.init()

screen = pg.display.set_mode((WIDTH, HEIGHT))

pg.display.set_caption("Darts!")

root.title("Points Scored")

root.geometry("500x500")

root.withdraw()

BLACK = (0, 0, 0)

pg.display.update()

clock = pg.time.Clock()

running = True

def give_points(points):

    root.deiconify()

    turns += 1

    scored = Label(root, text="You scored " + str(points) + " points.")

    if 501-points <= 0:
        
        points_left = Label(root, "You have won in " + str(turns) + " turns!")
        
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
    
