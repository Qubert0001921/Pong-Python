import pygame


class Text:
    def __init__(self, text, font: pygame.font.Font, x, y, color="White"):
        self.surf = font.render(text, False, color)
        self.rect = self.surf.get_rect(center=(x, y))

    def draw(self, window: pygame.Surface):
        window.blit(self.surf, self.rect)

