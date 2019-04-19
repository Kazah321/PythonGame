import pygame
from pygame.math import Vector2
import random


class Charakter(pygame.sprite.Sprite):

    def __init__(self,game):
         super().__init__()
         self.game=game
         self.window = game.screen
         self.board = game.lev
         self.Image=None
         self.rect=None
         
    def draw(self):
            self._look(self.Image,self.rect)
        
    def _look(self,img,polozenie=[10,10]):
        self.window.blit(img, polozenie)
    def collision():
        pass
    
    def skalowanie(self,img,size):
        return pygame.transform.scale(img,size)
    def tick(self):
        pass

    def move(self, mov_x,mov_y):
        if mov_x !=0:
            self.move_single_axis(mov_x,0)
        if mov_y !=0:
            self.move_single_axis(0,mov_y)

    def move_single_axis(self,mov_x,mov_y):
        #move
        self.rect.x += mov_x
        self.rect.y += mov_y

        self.collision(mov_x,mov_y)

    def take_level(self, level):
        self.level = level

    def kill(self):
        pass

    def change_diraction(self):
        y = random.randint(1,2)
       # print(y)
        if self.velocity_x == 0:
            if y != 1:
                self.velocity_y *= (-1)
            else:
                self.velocity_x = self.velocity_y
                self.velocity_y = 0


        if self.velocity_y == 0:
            if y==1:
                self.velocity_x *= (-1)
            else:
                self.velocity_y = self.velocity_x
                self.velocity_x = 0


    
    
class Cat(Charakter):
    def __init__(self,pos):
        self.Image=pygame.image.load('img/cat.png')
        self.pos=Vector2(pos[0],pos[1])
        self.rect=self.Image.get_rect(x=self.pos[0],y=self.pos[1])
        self.level=None
        self.velocity_y = 2
        self.velocity_x = 0
        self.timer = 0
    def draw(self):
        return self.Image, self.rect

    def collision(self,x,y):
        for wall in self.level.walls:
            if self.rect.colliderect(wall.rect):
                if x > 0:
                    self.rect.right = wall.rect.left
                    self.change_diraction()
                if x < 0:
                    self.rect.left = wall.rect.right
                    self.change_diraction()
                if y > 0:
                    self.rect.bottom = wall.rect.top
                    self.change_diraction()
                if y < 0:
                    self.rect.top = wall.rect.bottom
                    self.change_diraction()
        for trap in self.level.traps:
            if self.rect.colliderect(trap.rect):
                if x > 0:
                    self.rect.right = trap.rect.left
                    self.change_diraction()
                if x < 0:
                    self.rect.left = trap.rect.right
                    self.change_diraction()
                if y > 0:
                    self.rect.bottom = trap.rect.top
                    self.change_diraction()
                if y < 0:
                    self.rect.top = trap.rect.bottom
                    self.change_diraction()
        for chesse in self.level.cheeses:
            if self.rect.colliderect(chesse.rect):
                if x > 0:
                    self.rect.right = chesse.rect.left
                    self.change_diraction()
                if x < 0:
                    self.rect.left = chesse.rect.right
                    self.change_diraction()
                if y > 0:
                    self.rect.bottom = chesse.rect.top
                    self.change_diraction()
                if y < 0:
                    self.rect.top = chesse.rect.bottom
                    self.change_diraction()
        #if self.rect.colliderect(self.level.player.rect):
         #   self.level.player.kill()
            
        

    def tick(self):
        self.move(self.velocity_x, self.velocity_y)
        self.timer += 1
        if(self.timer%175 == 0):
            self.change_diraction()

        #print(self.velocity_x, self.velocity_y)


class Ghost(Charakter):
    def __init__(self,pos):
        self.Image = pygame.image.load('img/ghost.png')
        self.pos = Vector2(pos[0], pos[1])
        self.rect = self.Image.get_rect(x=self.pos[0], y=self.pos[1])
        self.level = None
        self.velocity_y = 2
        self.velocity_x = 0
        self.timer = 0

    def draw(self):
        return self.Image, self.rect

    def tick(self):
        self.move(self.velocity_x, self.velocity_y)
        self.timer += 1
        if(self.timer%175 == 0):
            self.change_diraction()
    def collision(self,x,y):
        for wall in self.level.walls:
            if self.rect.colliderect(wall.rect):
                if wall.sprawdz():
                    if x > 0:
                        self.rect.right = wall.rect.left
                        self.change_diraction()
                    if x < 0:
                        self.rect.left = wall.rect.right
                        self.change_diraction()
                    if y > 0:
                        self.rect.bottom = wall.rect.top
                        self.change_diraction()
                    if y < 0:
                        self.rect.top = wall.rect.bottom
                        self.change_diraction()
