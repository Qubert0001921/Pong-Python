import pygame
from random import randint

class Ball:
    def __init__(self, window_size):
        self.surf = pygame.Surface((20, 20))
        pygame.draw.circle(self.surf, "White", (10, 10), 10)

        self.rect = self.surf.get_rect(center=(window_size[0]//2, window_size[1]//2))
        values = [-1, 1]

        self._velocity = 2
        self._x_add_value = values[randint(0, 1)] * self.velocity
        self._y_add_value = values[randint(0, 1)] * self.velocity

    @property
    def velocity(self):
        return self._velocity

    @property
    def x_add_value(self):
        return self._x_add_value

    @x_add_value.setter
    def x_add_value(self, value):
        self._x_add_value = value * self.velocity

    @property
    def y_add_value(self):
        return self._y_add_value

    @y_add_value.setter
    def y_add_value(self, value):
        self._y_add_value = value * self.velocity

    def draw(self, window: pygame.Surface):
        window.blit(self.surf, self.rect)

    def update(self, window: pygame.Surface):
        self.draw(window)
        # self.add_value_to_rect_x(self.x_add_value)
        # self.add_value_to_rect_y(self.y_add_value)
        self.rect.x += self.x_add_value * self.velocity
        self.rect.y += self.y_add_value * self.velocity
