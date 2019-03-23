import pygame as pg
import classes


pg.init()

w = h = 600
win = pg.display.set_mode((w,h))
pg.display.set_caption("Le jeu pute à clic")
clock = pg.time.Clock()
player = classes.Player(300,300)
gameObject = [player]

win.fill((0,255,255))
pg.display.flip()

run = True
while run:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    for go in gameObject:
        go.update()

    dirty_rect = []

    for go in gameObject:
        dirty_rect.extend(go.draw(win))

    pg.display.update(dirty_rect)
    clock.tick(30)

pg.quit()
