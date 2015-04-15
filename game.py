import pygame


class Game():
    def __init__(self, title, window_size):
        self.title = title
        self.window_size = window_size

        pygame.init()
        self.window = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption(self.title)

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    def render(self):
        self.window.fill((0, 0, 0))

        pygame.display.update()

    def gameloop(self):
        while True:
            self.update()
            self.render()