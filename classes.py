#import ressources as res
import pygame

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 20
        self.height = 20

        self.vel_x = 0
        self.vel_y = 0

        self.angle = 0

        self.vel_x_max = 7
        self.vel_y_max = 7

        self.hp = 3

        self.rect = pygame.Rect(x,y,self.width, self.height)

    def addForce(self, x, y):
        self.vel_x = min(self.vel_x + x, self.vel_x_max)
        self.vel_y = min(self.vel_y + y, self.vel_y_max)

    def rotate(self, angle):
        self.angle = (self.angle + angle) % 360

    def shoot(self):
        pass

    def hit(self):
        self.hp -= 1

    def draw(self, win):
        rect = pygame.draw.rect(win, (0,0,0), self.rect)
        self.rect = pygame.draw.ellipse(win, (125,125,125), (self.x, self.y, self.width, self.height))
        return [self.rect, rect]

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:

        self.x += self.vel_x
        self.y += self.vel_y


class Enemy:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.hp = 0
        self.vx = 0
        self.vy = 0

    def draw(self, win):
        pass

    def update(self, target):
        pass

    def hit(self):
        pass

class Bullet:
    def __init__(self):
        pass
