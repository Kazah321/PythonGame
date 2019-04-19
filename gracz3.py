import pygame
import charcter
# load image for our main character
Imgup = pygame.image.load('img/mause3.png')
Imgright = pygame.image.load('img/mause4.png')
Imgdown = pygame.image.load('img/mause5.png')
Imgleft = pygame.image.load('img/mause6.png')

class gracz(charcter.Charakter):
    
    def __init__(self,game):
        super().__init__(game)
        
        # Scal of image 
        self.Imgup = self.skalowanie(Imgup,(20,30))
        self.Imgright = self.skalowanie(Imgright,(30,20))
        self.Imgdown = self.skalowanie(Imgdown,(20,30))
        self.Imgleft = self.skalowanie(Imgleft,(30,20))
        self.Image=self.Imgup 
        #
        self.win=game.win
        
        # Make physics
        self.speed = 5
        
        # make a coliade rectangel and set start positon
        self.pos=game.lev.positon_of_gamer
        self.rect_ver=self.Imgup.get_rect(x=self.pos[0],y=self.pos[1])
        self.rect_hor=self.Imgright.get_rect(x=self.pos[0],y=self.pos[1])
        self.rect=self.rect_ver
        self.next=False
    
    def _witchimage(self,number):
        if number==0:
            self.Image=self.Imgright
        if number==1:
            self.Image=self.Imgup
        if number==2:
            self.Image=self.Imgleft
        if number==3:
            self.Image=self.Imgdown
 
    def tick(self):
        #input
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w] and not pressed[pygame.K_d] and not pressed[pygame.K_a] :
            self.move(0,-self.speed)
            self._witchimage(1)
            self._wichupdate(0)
            
        if pressed[pygame.K_s] and not pressed[pygame.K_d] and not pressed[pygame.K_a] :
            self.move(0,self.speed)
            self._witchimage(3)
            self._wichupdate(0)
            
        if pressed[pygame.K_a] and not pressed[pygame.K_w] and not pressed[pygame.K_s] :
            self.move(-self.speed,0)
            self._witchimage(2)
            self._wichupdate(1)
            
        if pressed[pygame.K_d] and not pressed[pygame.K_w] and not pressed[pygame.K_s] :
            self.move(self.speed,0)
            self._witchimage(0)
            self._wichupdate(1)
    
    def collision(self,x,y):
        for wall in self.board.walls:
            if self.rect.colliderect(wall.rect):
                if x > 0:
                    self.rect.right = wall.rect.left
                if x < 0:
                    self.rect.left = wall.rect.right
                if y > 0:
                    self.rect.bottom = wall.rect.top
                if y < 0:
                    self.rect.top = wall.rect.bottom
                    
        for chesse in self.board.cheeses:
            if self.rect.colliderect(chesse.rect):
                self.board.cheeses.remove(chesse)
                self.win.take_cheese()
                self.win.If_win()
                
        for trap in self.board.traps:
            if self.rect.colliderect(trap.rect):
                self.kill()
                trap.kill()
        for triger in self.board.trigers:
            if self.rect.colliderect(triger.rect):
                if triger.collision:
                    triger.action()
                    
        for enemy in self.board.enemy:
            if self.rect.colliderect(enemy.rect):
                self.kill()
        
        for door in self.board.doors:
            if self.rect.colliderect(door.rect):
                if door.collision:
                    if x > 0:
                        self.rect.right = door.rect.left
                    if x < 0:
                        self.rect.left = door.rect.right
                    if y > 0:
                        self.rect.bottom = door.rect.top
                    if y < 0:
                        self.rect.top = door.rect.bottom
                     
                
        if self.win.you_can_go:
            if self.rect.colliderect(self.win.rect):
                self.next =True
                self.game.next_level()
            
    def _update_pos(self,position):
        self.pos=[position[0],position[1]]
        self.rect_ver=self.Imgup.get_rect(x=self.pos[0],y=self.pos[1])
        self.rect_hor=self.Imgright.get_rect(x=self.pos[0],y=self.pos[1])
        self.rect=self.rect_ver
        
    def kill(self):
        self.game.player_death()
        
                    
    def _update_rectangle(self):
        self.rect_ver.x=self.rect.x
        self.rect_hor.x=self.rect.x
        self.rect_ver.y=self.rect.y
        self.rect_hor.y=self.rect.y
    
    def _wichupdate(self,number):
        self._update_rectangle()
        if number == 1 and self.rect != self.rect_hor:
            self.rect=self.rect_hor
        if number == 0 and self.rect != self.rect_ver:
            self.rect=self.rect_ver
                
        
    def update_level(self,level,win,pos):
        self.board = level
        self.win = win
        if self.next:
            self._update_pos(pos)
            self.next=False
        

