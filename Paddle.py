import pygame


class Paddle:
    def __init__(self, x, y, input_type):
        super().__init__()
        self.x = x
        self.y = y
        self.width = 20
        self.height = 200
        self.rect = pygame.rect.Rect((x, y), (self.width, self.height))
        self.input_type = input_type

    def handle_input(self, window_height):
        keys = pygame.key.get_pressed()

        up = pygame.K_UP
        down = pygame.K_DOWN

        if self.input_type == "WSAD":
            up = pygame.K_w
            down = pygame.K_s

        if keys[up] and self.y - 63 >= 0:
            self.y -= 5
        if keys[down] and self.y <= window_height - self.height:
            self.y += 5

    def draw(self, window: pygame.Surface):
        pygame.draw.rect(window, "White", self.rect)

    def update(self, window: pygame.Surface):
        self.draw(window)
        self.rect.update((self.x, self.y), (self.width, self.height))
        self.handle_input(window.get_height())


