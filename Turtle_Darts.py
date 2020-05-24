import turtle #adapted from https://touey456.wordpress.com/2017/02/28/python-turtle-module-how-to-get-mouse-coordinates-without-clicking/

from random import randint, choice, uniform

count = 3

x_list = [-69, -198, 63, 192]

y_list = [60, -50, 170, -160]

import sys

import time

dart_num = 1

from threading import Thread

def make_dart(x, y):
    global dart_num
    global count
    if count > 0:
        if abs(m.enemy.xcor() - x) <= 50 and abs(m.enemy.ycor() - y) <= 50:
            count += 3
        exec("dart%s = turtle.Turtle()" % dart_num, globals())
        exec("dart%s.hideturtle()" % dart_num)
        exec("dart%s.shape('dart2.gif')" % dart_num)
        exec("dart%s.penup()" % dart_num)
        exec("dart%s.goto(x + 20, y + 20)" % dart_num) #needed because image position doesn't refer to the tip of the dart
        exec("dart%s.showturtle()" % dart_num)
        if dart_num > 1:
            exec("dart%s.hideturtle()" % str(dart_num - 1))
        dart_num += 1

class Main():
    def __init__(self):
        wn = turtle.Screen()
        wn.addshape("Board.gif")
        self.background = turtle.Turtle() #easier to make the background a turtle to move it around
        self.background.penup()
        self.background.shape("Board.gif")
        self.background.goto(142.5,-65)
        wn.addshape("dart2.gif")
        wn.addshape("red_dot2.gif")
        wn.addshape("dot2.gif")
        wn.setup(550, 480)
        screen = wn.getcanvas()
        self.author = turtle.Turtle() #writes score
        self.author.penup()
        self.author.hideturtle()
        self.author.color("white")
        self.author.goto(200, 215)
        self.t = turtle.Turtle() #the player (green)
        self.t.penup()
        self.t.shape("dot2.gif")
        self.t.speed(10)
        self.enemy = turtle.Turtle()#enemy dot (red)
        self.enemy.hideturtle() 
        self.enemy.penup()
        self.enemy.shape("red_dot2.gif")
        self.enemy.speed(10)
        self.x = 300
        self.y = 300
        screen.bind('<Motion>', self.set_coords) #bind mouse movement to screen
        a = Thread(target = self.run)
        a.setDaemon(True)
        a.start()
        b = Thread(target = self.enemy_run)
        b.setDaemon(True)
        b.start()
        c = Thread(target = self.dart_click())
        c.setDaemon(True)
        c.start()
    def set_coords(self, event):
        self.x = event.x
        self.y = event.y
    def run(self):
        while True:
            if count < 0:
                self.t.hideturtle()
                if dart_num != 1:
                    exec("dart%s.hideturtle()" % str(dart_num))
                sys.exit()
            self.t.setposition(self.x-275, (self.y*-1)+240) #needed because turtle and screen are referring to different positions
    def enemy_run(self):
        while True:
            global count
            if count <= 0:
                self.enemy.hideturtle()
                self.author.clear()
                self.author.write("0", font=("Arial", 16, "normal"))
                self.author.clear()
                self.author.goto(-40, -10)
                self.author.write("Score: %s" % str(dart_num - 1), font=("Arial", 16, "normal"))
                sys.exit()
            self.enemy.setposition(choice(x_list), choice(y_list))
            self.enemy.showturtle()
            time.sleep(0.65)
            self.author.clear()
            self.author.write(count, font=("Arial", 16, "normal"))
            count -= 1
            self.enemy.hideturtle()
            self.enemy.setposition(1000, 0)
            time.sleep(0.65)
            self.author.clear()
            self.author.write(count, font=("Arial", 16, "normal"))
            count -= 1
    def dart_click(self):
        global count
        if count < 1:
            sys.exit()
        else:
            turtle.onscreenclick(make_dart)
            
m = Main()

turtle.mainloop()

