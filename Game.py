import pygame
from sys import exit
from Paddle import Paddle
from Ball import Ball
from Text import Text
import GameConfig


class Game:
    def __init__(self, width, height, caption):
        pygame.init()
        self.window_width = width
        self.window_height = height
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption(caption)

        self.clock = pygame.time.Clock()

        self.score_p1 = 0
        self.score_p2 = 0

        self.paddle1 = Paddle(0, self.window.get_height()//2-100, "WSAD")
        self.paddle2 = Paddle(self.window.get_width()-20, self.window.get_height()//2-100, "Arrows")
        self.ball = Ball(self.window.get_size())

        self.pixel_font = pygame.font.Font("font/PixelType.ttf", 50)
        self.start_game_info_text = Text("Click space to run game!", self.pixel_font, self.window.get_width()//2, 35)

        self.game_running = False

        self.pong_sound = pygame.mixer.Sound("Music/pong.wav")
        self.pong_sound.set_volume(0.3)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.game_running = True

    def restart_game(self):
        self.game_running = False
        self.ball.rect.x = self.window.get_width()//2
        self.ball.rect.y = self.window.get_height()//2

        self.paddle1.x = 0
        self.paddle1.y = self.window.get_height()//2-100

        self.paddle2.x = self.window.get_width() - 20
        self.paddle2.y = self.window.get_height()//2-100

    def ball_collide(self):

        if self.ball.rect.y + self.ball.rect.h >= self.window.get_height():
            self.ball.y_add_value = -1
        elif self.ball.rect.y - 60 <= 0:
            self.ball.y_add_value = 1
        elif self.ball.rect.x <= 0:
            self.score_p2 += 1
            self.restart_game()
        elif self.ball.rect.x + self.ball.rect.w >= self.window.get_width():
            self.score_p1 += 1
            self.restart_game()

        if self.ball.rect.colliderect(self.paddle1):
            self.ball.x_add_value = 1
            self.pong_sound.play()
        elif self.ball.rect.colliderect(self.paddle2):
            self.ball.x_add_value = -1
            self.pong_sound.play()

    def run(self):
        while True:
            self.window.fill("Black")

            self.handle_events()

            if self.game_running:
                self.paddle1.update(self.window)
                self.paddle2.update(self.window)
                self.ball_collide()
                self.ball.update(self.window)
            else:
                self.start_game_info_text.draw(self.window)

            score_p1_text = self.pixel_font.render(f"Score: {self.score_p1}", False, "White")
            score_p1_text_rect = score_p1_text.get_rect(topleft=(20, 20))

            score_p2_text = self.pixel_font.render(f"Score: {self.score_p2}", False, "White")
            score_p2_text_rect = score_p2_text.get_rect(topright=(self.window.get_width()-20, 20))

            pygame.draw.line(self.window, "White", (0, 60), (self.window.get_width(), 60))
            pygame.draw.line(self.window, "White", (self.window.get_width()//2, 60), (self.window.get_width()//2, self.window.get_height()), width=1)

            self.window.blit(score_p1_text, score_p1_text_rect)
            self.window.blit(score_p2_text, score_p2_text_rect)

            self.clock.tick(GameConfig.FPS)

            pygame.display.update()
