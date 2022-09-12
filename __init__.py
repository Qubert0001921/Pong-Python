import pygame
from Game import Game

game_width, game_height = 1300, 750
game_caption = "Pong game"


def main():
    global game_width, game_height, game_caption
    game = Game(game_width, game_height, game_caption)
    game.run()


if __name__ == "__main__":
    main()
