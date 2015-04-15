import pygame


class Entity(object):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def update(self):
        pass

    def render(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, 32, 32))
        pygame.draw.rect(window, (0, 0, 0), (self.x, self.y, 32, 32), 2)


class Player(Entity):
    def __init__(self, x, y, color, world):
        super().__init__(x, y, color)
        self.world = world

    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            if not self.world.map[int(self.x / 32)][int(self.y / 32) - 1].isSolid():
                self.y -= 32
        if key[pygame.K_s]:
            if not self.world.map[int(self.x / 32)][int(self.y / 32) + 1].isSolid():
                self.y += 32
        if key[pygame.K_a]:
            if not self.world.map[int(self.x / 32) - 1][int(self.y / 32)].isSolid():
                self.x -= 32
        if key[pygame.K_d]:
            if not self.world.map[int(self.x / 32) + 1][int(self.y / 32)].isSolid():
                self.x += 32