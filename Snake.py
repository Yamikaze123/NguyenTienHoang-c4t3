import pygame
import random
from pygame.locals import *

width = 500
height = 500
display_surf = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake")

white = (255, 255, 255)

fps = 200
fps_clock = pygame.time.Clock()


class Scoreboard:
    def __init__(self, score):
        self.score = score

    def draw(self):
        pygame.draw.rect(display_surf, white, (0, 480, 500, 20))


class Food:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.r = radius

    def draw(self):
        pygame.draw.circle(display_surf, white, random.randrange(10, 500, 10), self.r)

    def update(self, snake):
        if self.x == snake.x and self.y == snake.y:
            self.x = random.randrange(10, 500, 10)
            self.y = random.randrange(10, 500, 10)


class Snake:
    def __init__(self, x, y, l, dx, dy, speed):
        self.x = x
        self.y = y
        self.head = [50, 10]
        self.tail = [30, 10]
        self.length = l
        self.dir = 'Down'
        self.speed = speed
        self.dir_x = dx
        self.dir_y = dy

    def draw(self):
        pygame.draw.rect(display_surf, white, (self.x, self.y, 10, self.length))

    def eat_food(self, food):
        if self.x == food.x and self.y == food.y:
            self.length += 10

    def change_dir(self, new_dir): #Ngan chuyen huong sai
        if self.dir == "Up" and new_dir == "Down":
            self.dir = "Up"
        elif self.dir == "Down" and new_dir == "Up":
            self.dir = "Down"
        elif self.dir == "Right" and new_dir == "Left":
            self.dir = "Right"
        elif self.dir == "Left" and new_dir == "Right":
            self.dir = "Left"

    def move(self):
        if self.dir == "Up":
            for i in range(500, 10):
                self.y -= 10
        elif self.dir == "Down":
            for i in range(500, 10):
                self.y += 10
        elif self.dir == "Right":
            for i in range(500, 10):
                self.x +=10
        elif self.dir == "Left":
            for i in range(500, 10):
                self.x -= 10

    def hit_celling(self):
        if self.y == 500:
            self.y = 0
            return True
        else:
            return False

    def hit_floor(self):
        if self.y == 0:
            self.y = 500
            return True
        else:
            return False

    def hit_wall(self):
        if self.x == 500:
            self.x = 0
            return True
        elif self.x == 0:
            self.x = 500
            return True
        else:
            return False

    def die(self):
        if self.head == self.tail:
            print("You lose the game")

