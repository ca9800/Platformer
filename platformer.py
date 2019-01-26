"""
platformer.py
Author: claire
Credit: johari, meg, dina, mr. dennisson, ggame tutorials, random clasmates in general 
Assignment:
Write and submit a program that implements the sandbox platformer game:
https://github.com/HHS-IntroProgramming/Platformer
"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, Frame

black = Color(0x000000, 1.0)
grey = Color(0xC0C0C0, 1.0)
pink = Color(0xFF00FF, 1.0)
white = Color(0xffffff, 1.0)
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
thinline = LineStyle(2, black)
blkline = LineStyle(1, black)
coolline = LineStyle(1, grey)




#makes the walls
class Box(Sprite):
     asset = RectangleAsset(40, 40, thinline, blue)
     #place = (x, y)
     def __init__(self, x, y):
        super().__init__(Box.asset, (x, y))
        self.x = x
        self.y = y


#makes springs
class Spring(Sprite):
    assett = RectangleAsset(15, 3, blkline, red)
    def __init__(self, x, y):
        super().__init__(Spring.assett, (x,y))
        self.x = x
        self.y = y
        self.g = 0
    
    def step(self):
        self.g += 0.3
        self.y += self.g
        scollisions = self.collidingWithSprites(Box)
        if scollisions:
            self.y -= self.g
            self.g = 0


class Player(Sprite):
    assettt = CircleAsset(15, coolline, pink)
    def __init__(self, x, y):
        super().__init__(Player.assettt, (x, y))
        self.x = x
        self.y = y


g = 0


class Platformer(App):
    def __init__(self):
        super().__init__()
        self.clickx = 0
        self.clicky = 0
        self.player = 0
        self.spring = 0
        self.playerxx = None
        self.listenKeyEvent('keydown', 'c', self.buildPlayer) #creates character
        self.listenKeyEvent('keydown', 'b', self.buildBox) #creates a block
        self.listenMouseEvent('mousemove', self.move)
        self.listenKeyEvent('keydown', 'l', self.moveright) #controls characters movements
        self.listenKeyEvent('keydown', 'j', self.moveleft)
        self.listenKeyEvent('keydown', 'i', self.moveup)
        self.listenKeyEvent('keydown', 'k', self.movedown)
        self.listenKeyEvent('keydown', 's', self.buildSpring) #creates a spring
    

    
    def buildPlayer (self, event):
        global g
        if self.playerxx:
            self.playerxx.destroy()
            g = 0
        self.playerxx = Player(self.clickx - 15, self.clicky - 15)
 
    
    def buildBox(self, event):
        x = self.clickx - self.clickx%40
        y = self.clicky - self.clicky%40
        Box(x-15, y-15)
 
        
    def buildSpring(self, event):
        self.spring = (Spring(self.clickx-5, self.clicky-5))

    
    def move(self, event):
        self.clickx = event.x
        self.clicky = event.y

    
    def moveup(self, event):
        global g
        if g == 0:
            g = -10
            collisions = (self.playerxx.collidingWithSprites(Box))
            if collisions:
                self.playerxx.y += 40


    def movedown(self, event):
        self.playerxx.y += 10
        collisions = (self.playerxx.collidingWithSprites(Box))
        if collisions:
            self.playerxx.y -= 10
 
    
    def moveright(self, event):
        self.playerxx.x += 5
        collisions = (self.playerxx.collidingWithSprites(Box))
        if collisions:
            self.playerxx.x -= 5
   
            
    def moveleft(self, event):
        self.playerxx.x -= 5
        collisions = (self.playerxx.collidingWithSprites(Box))
        if collisions:
            self.playerxx.x += 5
   
            
    def step(self):
        global g
        if self.playerxx:
            g += 0.5
            self.playerxx.y += g
            collisions =  (self.playerxx.collidingWithSprites(Box))
            spcollisions = (self.playerxx.collidingWithSprites(Spring))
            if collisions:
                self.playerxx.y -= g
                g = 0
            if spcollisions:
                g = -10
        springs = (self.getSpritesbyClass(Spring))
        for spring in springs:
            spring.step()



            
myapp = Platformer()
myapp.run()
        
        
        
        
        
        
        
        

