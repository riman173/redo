import pygame
import sys, os

class Actor(pygame.sprite.Sprite):
    grav = 6#2.9
    maxVel = 70
    velDamp = .1
    accDamp = .35
    accDefault = 3
    groundAcc = 8.4
    airAcc = 5 
    left, right, onGround, onWall = False, False, False, False
    def __init__(self, (x, y)):
        pygame.sprite.Sprite.__init__(self)
        self.disp = self.pos = [x,y]
        self.vel = [0.0, 0.0]
        self.acc = [0.0, Actor.grav]
        self.image = pygame.Surface((30,30)).convert()
        self.rect = self.image.get_rect()
        self.initialpos = self.pos
        self.rect.center = self.disp 
    def setLocation(self,(x,y)):
       
        self.pos = [a-b+c for a,b,c in zip(self.pos,self.disp,[x,y])]
        self.disp = [x,y]
        self.vel = [0,0]
        self.rect.center = self.disp
    def jump(self):
        if self.onGround is True or self.onWall is True:
            self.vel[1] = -100
            self.onGround, self.onWall = False, False
    def offset(self, x, y):
        self.pos = [a + b for a,b in zip(self.pos, [x,y])]
        self.disp = [a+b for a,b in zip(self.disp, [x,y])]
        self.rect.center = self.disp

    def update(self, offset=[0.0, 0.0]):
        self.pos = [a+Actor.velDamp*b for a,b in zip(self.pos, self.vel)]
        self.disp = [a+b for a,b in zip( self.pos, offset)]
        #On above line: self.pos = [a +b + Actor.velDamp*c for a, b, c in zip(stuff)]
        if abs(self.vel[0]) > Actor.maxVel and self.acc[0]*self.vel[0] > 0:
            self.acc[0] = 0

        self.vel = [a[0]+Actor.accDamp*a[1] for a in zip(self.vel, self.acc)]
        
        if not (self.left or self.right):
            if (self.onGround):
                self.acc[0] = -.2*self.vel[0]
            else:
                self.acc[0] = -.12*self.vel[0]

        self.rect.center = self.disp 
        if self.left:
            self.leftPress()
        elif self.right:
            self.rightPress()

    def leftPress(self):
        if self.onGround: self.acc[0] = -Actor.groundAcc
        else: self.acc[0] = -Actor.airAcc

    def rightPress(self):
        if self.onGround: self.acc[0] = Actor.groundAcc
        else: self.acc[0] = Actor.airAcc

    def reset(self):
        self.pos = self.initialpos
        self.rect.center = self.pos    
