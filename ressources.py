import pygame.image as img
import pygame.mixer as mix
mix.init()
img.init()
#images
def getImg(name):
    return img.load("{}.png".format(name)).convert()
r_arrowI = getImg('r_arrow')
enemyI = getImg('enemy')
p
#musics
