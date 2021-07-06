import pygame
from settings import *

pygame.init() # инициализация пайгейм
screen = pygame.display.set_mode((width, height)) # создаем окно
pygame.display.set_caption("ROBOT SIMULATION") # название окна
clock = pygame.time.Clock() # время
pygame.font.init() # инициализация текста
myfont = pygame.font.SysFont('Comic Sans MS', 30)



def drawWindow():
    screen.fill(GREY)   # отрисовка фона
    pygame.draw.rect(screen, (28, 32, 40), (0, 0, width, height), 15) # конутр окна
    pygame.draw.circle(screen, WHITE, deliver_pos, 50, 10)

