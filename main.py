import pygame as pg
import classes
import ressources
pg.init()

w = h = 600
win = pg.display.set_mode((w,h))
pg.display.set_caption("Le jeu pute à clic")

run = True
while run:
    win.fill((250,250,250))
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
pg.quit()
