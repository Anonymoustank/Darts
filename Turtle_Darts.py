import turtle #adapted from https://touey456.wordpress.com/2017/02/28/python-turtle-module-how-to-get-mouse-coordinates-without-clicking/

from random import randint

import time

dart_num = 1

from threading import Thread

def make_dart(x, y):
    if abs(m.enemy.xcor() - x) <= 50 and abs(m.enemy.ycor() - y) <= 50:
        print("Dead")
    exec("dart%s = turtle.Turtle()" % dart_num)
    exec("dart%s.hideturtle()" % dart_num)
    exec("dart%s.shape('dart2.gif')" % dart_num)
    exec("dart%s.penup()" % dart_num)
    exec("dart%s.goto(x + 20, y + 20)" % dart_num) #needed because image position doesn't refer to the tip of the dart
    exec("dart%s.showturtle()" % dart_num)

class Main():
    def __init__(self):
        wn = turtle.Screen()
        wn.bgpic("Dart Board.gif")
        wn.addshape("dart2.gif")
        wn.addshape("red_dot2.gif")
        wn.addshape("dot2.gif")
        wn.setup(550, 575)
        screen = wn.getcanvas()
        self.t = turtle.Turtle()
        self.t.penup()
        self.t.shape("dot2.gif")
        self.t.speed(10)
        self.enemy = turtle.Turtle()
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
            self.t.setposition(self.x-275, (self.y*-1)+290) #needed because turtle and screen are referring to different positions
    def enemy_run(self):
        while True:
            self.enemy.setposition(100, 100)
            time.sleep(1)
    def dart_click(self):
        turtle.onscreenclick(make_dart)
            
m = Main()

turtle.mainloop()

