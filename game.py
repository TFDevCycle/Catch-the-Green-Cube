from asyncore import close_all
from typing_extensions import Self
import pygame
import time
import random
import colorama
from tkinter import *
from tkinter import messagebox
import os

global a1
global a3
global a4
global a5
global a6
global a7
global a8
global a9
global a10
global a11
global a12

global i1
global i2
global i3
global i4

global se1onoff

i1 = 0
i2 = 0
i3 = 0
i4 = 0

a1 = "X"
a3 = "X"
a4 = "X"
a5 = "X"
a6 = "X"
a7 = "X"
a8 = "X"
a9 = "X"
a10 = "X"
a11 = "X"
a12 = "X"

se1onoff = "OFF"

def game(self): 
      
    # activate the pygame library .
    # initiate pygame and give permission
    # to use pygame's functionality.
    pygame.init()            

    # create the display surface object
    # of specific dimension..e(500, 500).
    win = pygame.display.set_mode((500, 500))
    bg = pygame.image.load("stuff\Stage1.png")

    # set the pygame window name
    pygame.display.set_caption("Catch the Green Cube")

# object current co-ordinates
    self.x = 200
    self.y = 200
    self.i = 0
    self.r = 0
    self.t = 0

    self.x2 = random.randint(0,480)
    self.y2 = random.randint(0,480)

    self.x3 = random.randint(0,480)
    self.y3 = random.randint(0,480)

    # dimensions of the object
    self.width = 20
    self.height = 20

    self.score = 0
    self.deaths = 0
    self.round = 1

    # velocity / speed of movement
    self.vel = 10
    font1 = pygame.font.SysFont("none", 16)
    self.img1 = font1.render('Round: ' + str(self.round), True, (255,0,0))
    self.img2 = font1.render('Score: ' + str(self.score), True, (255,0,0))
    self.img3 = font1.render('Deaths: ' + str(self.deaths), True, (255,0,0))

    # Indicates pygame is running
    run = True
    while run:
                
        pygame.time.delay(10)
        win.blit(source=bg, dest=(0,0))

        if self.i == 0:
            pass

        if self.i == 1:
            if self.x <= self.x2:
                self.x = self.x + 1
            elif self.x >= self.x2:
                self.x = self.x - 1

            if self.y <= self.y2:
                self.y = self.y + 1
            elif self.y >= self.y2:
                self.y = self.y - 1

        if self.i == 2:
            tmp_x = self.x
            tmp_y = self.y
            for self.x in range(self.x2):
                if self.x <= self.x2:
                    self.x = self.x + 1
                elif self.x >= self.x2:
                    self.x = self.x - 1

            for self.y in range(self.y2):
                if self.y <= self.y2:
                    self.y = self.y + 1
                elif self.y >= self.y2:
                    self.y = self.y - 1

        if self.i == 3:
            tmp_x = self.x
            tmp_y = self.y
            for self.x in range(self.x2):
                if self.x <= self.x2:
                    self.x = self.x + 2
                elif self.x >= self.x2:
                    self.x = self.x - 2
                if self.x == self.x2:
                    self.x = tmp_x

            for self.y in range(self.y2):
                if self.y <= self.y2:
                    self.y = self.y + 2
                elif self.y >= self.y2:
                    self.y = self.y - 1
                if self.y == self.y2:
                    self.y = tmp_y

        if self.deaths == 1:
            global a9
            a9 = "✓"

        if self.deaths == 10:
            global a10
            a10 = "✓"

        if self.deaths == 50:
            global a11
            a11 = "✓"
            
        if self.deaths == 100:
            global a12
            a12 = "✓"
            
        if self.score >= 10:
            global a3
            a3 = "✓"

        if self.score >= 50:
            global a4
            a4 = "✓"
                    
        if self.score >= 100:
            global a5
            a5 = "✓"  

        if self.score >= 200:
            global a6
            a6 = "✓"
                              
        if self.score >= 500:
            global a7
            a7 = "✓"
                              
        if self.score >= 1000:
            global a8
            a8 = "✓"
            
        if self.score >= 10:
            self.x3 = self.x3 + 1
            if self.x3 >= 500:
                self.x3 = 0

        if self.score >= 20:
            self.x3 = self.x3 + 2
            if self.x3 >= 500:
                self.x3 = 0
                self.y3 = random.randint(0,480)


        if self.score >= 200:
            self.x3 = self.x3 + 3
            if self.x3 >= 500:
                self.x3 = 0
                self.y3 = random.randint(0,480)


        if self.score >= 300:
            self.x3 = self.x3 + 4
            self.y3 = self.x3 + 4

            if self.x3 >= 500:
                self.x3 = 0
                self.y3 = random.randint(0,480)

        if self.score >= 500:
            self.x3 = self.x3 + 5
            self.y3 = self.x3 + 5

            if self.x3 >= 500:
                self.x3 = 0
                self.y3 = random.randint(0,480)

            if self.y3 >= 500:
                self.y3 = 0
                self.y3 = random.randint(0,480)

        if a1 == "✓":
            global i1
            global i2
            global i3
            if i3 == 0:
                i2 = i2 + 1
                print(str(i2) + "/11")
                i1 = i1 + 9.090909090909091
                print(i1)
                i3 = i3 + 1
                print(i3)
        if a3 == "✓":
            if i3 == 1:
                i2 = i2 + 1
                print(str(i2) + "/11")
                i1 = i1 + 9.090909090909091
                print(i1)
                i3 = i3 + 1
        if a4 == "✓":
            if i3 == 2:
                i2 = i2 + 1
                print(str(i2) + "/11")
                i1 = i1 + 9.090909090909091
                print(i1)
                i3 = i3 + 1
        if a5 == "✓":
            if i3 == 3:
                i2 = i2 + 1
                print(str(i2) + "/11")
                i1 = i1 + 9.090909090909091
                print(i1)
                i3 = i3 + 1
        if a6 == "✓":
            if i3 == 4:
                i2 = i2 + 1
                print(str(i2) + "/11")
                i1 = i1 + 9.090909090909091
                print(i1)
                i3 = i3 + 1
        if a7 == "✓":
            if i3 == 5:
                i2 = i2 + 1
                print(str(i2) + "/11")
                i1 = i1 + 9.090909090909091
                print(i1)
                i3 = i3 + 1
        if a8 == "✓":
            if i3 == 6:
                i2 = i2 + 1
                print(str(i2) + "/11")
                i1 = i1 + 9.090909090909091
                print(i1)
                i3 = i3 + 1
        if a9 == "✓":
            if i3 == 7:
                i2 = i2 + 1
                print(str(i2) + "/11")
                i1 = i1 + 9.090909090909091
                print(i1)
                i3 = i3 + 1
        if a10 == "✓":
            if i3 == 8:
                i2 = i2 + 1
                print(str(i2) + "/11")
                i1 = i1 + 9.090909090909091
                print(i1)
                i3 = i3 + 1
        if a11 == "✓":
            if i3 == 9:
                i2 = i2 + 1
                print(str(i2) + "/11")
                i1 = i1 + 9.090909090909091
                print(i1)
                i3 = i3 + 1
        if a12 == "✓":
            if i3 == 10:
                i2 = i2 + 1
                print(str(i2) + "/11")
                i1 = i1 + 9.090909090909091
                print(i1)
                i3 = i3 + 1
        
        if i1 == 100.00000000000001:
            print("100% Complete")
            res = messagebox.askyesno("You have archieved 100%", "Do you want to reset the progress?")
            if res == "Yes":
                self.score = 0
                self.round = 0
                self.deaths = 0
            if res == "No":
                self.score = 0
                self.deaths = self.deaths + 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                ns = time.perf_counter()
                print('-----------------------')
                print('Time Played: ' + str(ns))
                print('Score: ' + str(self.score))
                print('Deaths: ' + str(self.deaths))
                print('-----------------------')

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and self.x>0:
            self.x -= self.vel
            
        if keys[pygame.K_RIGHT] and self.x<500-self.width:
            self.x += self.vel
            
        if keys[pygame.K_UP] and self.y>0:
            self.y -= self.vel
            
        if keys[pygame.K_DOWN] and self.y<500-self.height:
            self.y += self.vel
        
        if keys[pygame.K_r]:
            if se1onoff == "ON":
                self.x = self.x3
                self.y = self.y3
            elif se1onoff == "OFF":
                #self.img1 = font1.render('Round: ' + str(self.round), True, (255,0,0))
                self.img2 = font1.render('Score: ' + str(self.score), True, (255,0,0))
                self.img3 = font1.render('Deaths: ' + str(self.deaths), True, (255,0,0))
                rect3.bottom = rect1.top
                ns = time.perf_counter()
                print('------- ' + colorama.Fore.BLUE + 'Round ' + str(round) + colorama.Style.RESET_ALL + ' -------')
                print(colorama.Fore.YELLOW + 'Time Played: '+ colorama.Style.RESET_ALL + str(ns))
                print(colorama.Fore.GREEN + 'Score: ' + colorama.Style.RESET_ALL + str(self.score))
                print(colorama.Fore.RED + 'Deaths: ' + colorama.Style.RESET_ALL + str(self.deaths))
                print('------------------------')

                self.score = 0
                self.deaths = self.deaths + 1
                self.round = self.round + 1

                self.x = 0
                self.y = 0
                self.x2 = random.randint(0,480)
                self.y2 = random.randint(0,480)

                self.x3 = random.randint(0,480)
                self.y3 = random.randint(0,480)
                pygame.display.set_caption('Game Over - Create new Level')
                
        if keys[pygame.K_ESCAPE]:
            menu()

        if keys[pygame.K_1]:
            self.i = 0

        if keys[pygame.K_2]:
            self.i = 1

        if keys[pygame.K_3]:
            self.i = 2

        if keys[pygame.K_4]:
            self.i = 3

        if keys[pygame.K_LCTRL]:
            self.t = 1
            self.ts = 0

        if keys[pygame.K_LCTRL and pygame.K_p]:
            helpcontrol()

        if keys[pygame.K_t]:
            if self.t == 1:
                print("x: " + str(self.x))
                print("y: " + str(self.y))
                self.t = 0

        if keys[pygame.K_TAB]:
            scoreboard(self.score, self.deaths)

        rect1 = pygame.draw.rect(win, (0, 0, 255), (self.x, self.y, self.width, self.height))
        rect2 = pygame.draw.rect(win, (0, 255, 0), (self.x2, self.y2, 20, 20))
        
        if se1onoff == "ON":
            rect3 = pygame.draw.rect(win, (255, 0, 0), (self.x3, self.y3, 20, 20))
        elif se1onoff == "OFF":     
            rect3 = pygame.draw.rect(win, (255, 0, 0), (0, 0, 0, 0))     

        collide1 = pygame.Rect.colliderect(rect1,
                                        rect2)
        collide2 = pygame.Rect.colliderect(rect1,
                                        rect3)


        if collide1:
            #self.img1 = font1.render('Round: ' + str(self.round), True, (255,0,0))
            self.img2 = font1.render('Score: ' + str(self.score), True, (255,0,0))
            self.img3 = font1.render('Deaths: ' + str(self.deaths), True, (255,0,0))

            rect2.bottom = rect1.top

            self.score = self.score + 1


            self.x2 = random.randint(0,480)
            self.y2 = random.randint(0,480)

            self.x3 = random.randint(0,480)
            self.y3 = random.randint(0,480)  

        if collide2:
            #self.img1 = font1.render('Round: ' + str(self.round), True, (255,0,0))
            self.img2 = font1.render('Score: ' + str(self.score), True, (255,0,0))
            self.img3 = font1.render('Deaths: ' + str(self.deaths), True, (255,0,0))
            rect3.bottom = rect1.top
            ns = time.perf_counter()
            print('------- ' + colorama.Fore.BLUE + 'Round ' + str(round) + colorama.Style.RESET_ALL + ' -------')
            print(colorama.Fore.YELLOW + 'Time Played: '+ colorama.Style.RESET_ALL + str(ns))
            print(colorama.Fore.GREEN + 'Score: ' + colorama.Style.RESET_ALL + str(self.score))
            print(colorama.Fore.RED + 'Deaths: ' + colorama.Style.RESET_ALL + str(self.deaths))
            print('------------------------')

            self.score = 0
            self.deaths = self.deaths + 1
            self.round = self.round + 1

            self.x = 0
            self.y = 0
            self.x2 = random.randint(0,480)
            self.y2 = random.randint(0,480)

            self.x3 = random.randint(0,480)
            self.y3 = random.randint(0,480)
            pygame.display.set_caption('Game Over - Create new Level')
        #win.blit(self.img1, (20, 20))
        win.blit(self.img2, (0, 0))
        win.blit(self.img3, (100, 0))
        pygame.display.update()


 
class start():
    def __init__(self) -> None:
        self.startapp = Tk()
        self.startapp.title("Catch the Green Cube")
        Label(self.startapp, text="Catch the Green Cube", foreground="Blue", font="bold").pack()
        Button(self.startapp, text="Start Game", command=self.gamestart, width=50).pack()
        Button(self.startapp, text="Archievments", command=archievments, width=50).pack()
        Button(self.startapp, text="Settings", command=Settings, width=50).pack()
        Button(self.startapp, text="Controls", command=helpcontrol, width=50).pack()
        Button(self.startapp, text="Exit Game", command=self.startapp.destroy, width=50).pack()
        Label(self.startapp, text="This Game is in a Experimental Version", foreground="RED").pack()
        self.startapp.mainloop()
    def gamestart(self):
        self.startapp.destroy()
        global a1
        a1 = "✓"
        game(self)

class menu():
        def __init__(self) -> None:
            self.app1 = Tk()
            
            self.ns = time.perf_counter()
            
            self.widgets()
            self.ns = time.perf_counter()
            self.app1.mainloop()

        def close(self):
            self.app1.destroy()

        def closeall(self):
            self.app1.destroy()
            pygame.quit()
            start()


        def widgets(self):
            Button(self.app1, text="Return", width=20, command=self.close).pack()
            Button(self.app1, text="Settings", width=20, command=Settings).pack()
            Button(self.app1, text="Menu", width=20, command=self.closeall).pack()

class scoreboard():
        def __init__(self, score, deaths) -> None:
            self.score = score
            self.deaths = deaths
            self.app1 = Tk()
            
            self.ns = time.perf_counter()
            
            self.widgets()
            self.ns = time.perf_counter()
            self.app1.mainloop()

        def close(self):
            self.app1.destroy()

        def widgets(self):
            Label(self.app1, text="Time: " + str(self.ns)).pack()
            Label(self.app1, text="Score: " + str(self.score)).pack()
            Label(self.app1, text="Deaths: " + str(self.deaths)).pack()

class Settings():
        def __init__(self) -> None:
            self.app1 = Tk()
            
            self.widgets()
            self.app1.mainloop()

        def close(self):
            self.app1.destroy()

        def widgets(self):
            global se1onoff
            def se1onofffunc():
                global se1onoff
                if se1onoff == "ON":
                    se1onoff = "OFF"
                elif se1onoff == "OFF":
                    se1onoff = "ON"
                    
                btn1.config(text="Enemy Spawn: " + se1onoff)
                print(se1onoff)

            btn1 = Button(self.app1, text="Enemy Spawn: " + str(se1onoff), command=se1onofffunc)
            btn1.pack()

class helpcontrol():
    def __init__(self) -> None:
        self.controlapp = Tk()
        self.controlapp.title("Controls")
        self.widgets()
        self.controlapp.mainloop()
    def widgets(self):
        Label(self.controlapp, text="1: Turn Player Movment On", anchor=W).pack()
        Label(self.controlapp, text="2: Speed UP 2x", anchor=W).pack()
        Label(self.controlapp, text="3: Speed UP 3x", anchor=W).pack()
        Label(self.controlapp, text="4: Speed UP 4x", anchor=W).pack()
        Label(self.controlapp, text="").pack()
        Label(self.controlapp, text="ESC: Go to the Pause Menu").pack()
        Label(self.controlapp, text="TAB: Opens the Scoreboard").pack()
        Label(self.controlapp, text="CTRL+P: Opens the Control View").pack()

class archievments():
    def __init__(self) -> None:
        self.generalapp = Tk()
        self.generalapp.title("General - Archievments")
        self.Noobapp = Tk()
        self.Noobapp.title("Noob - Archievments")
        #self.Proapp = Tk()
        #self.Proapp.title("Pro - Archievments")
        #self.hackerapp = Tk()
        #self.hackerapp.title("Hacker - Archievments")
        self.scoresapp = Tk()
        self.scoresapp.title("Score - Archievments")
        self.widgets()

    def widgets(self):
        Label(self.generalapp, text="", width=50, anchor=W).pack()
        Label(self.generalapp, text="Start the Game | " + a1, anchor=W).pack()

        Label(self.Noobapp, text="", width=50, anchor=W).pack()
        Label(self.Noobapp, text="Die 1 Time | " + a9, anchor=W).pack()
        Label(self.Noobapp, text="Die 10 Time | " + a10, anchor=W).pack()
        Label(self.Noobapp, text="Die 50 Time | " + a11, anchor=W).pack()
        Label(self.Noobapp, text="Die 100 Time | " + a12, anchor=W).pack()

        Label(self.scoresapp, text="", width=50, anchor=W).pack()
        Label(self.scoresapp, text="Get a Score of 10 | " + a3, anchor=W).pack()
        Label(self.scoresapp, text="Get a Score of 50 | " + a4, anchor=W).pack()
        Label(self.scoresapp, text="Get a Score of 100 | " + a5, anchor=W).pack()
        Label(self.scoresapp, text="Get a Score of 200 | " + a6, anchor=W).pack()
        Label(self.scoresapp, text="Get a Score of 500 | " + a7, anchor=W).pack()
        Label(self.scoresapp, text="Get a Score of 1000 | " + a8, anchor=W).pack()
start()
pygame.quit()
