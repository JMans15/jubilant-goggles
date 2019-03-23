import ressources as res

class Player:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.hp = 0
        self.vx = 0
        self.vy = 0

    def shoot(self):
        pass

    def hit(self):
        pass

    def draw(self, win):
        pass

    def update(self):
        pass


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
