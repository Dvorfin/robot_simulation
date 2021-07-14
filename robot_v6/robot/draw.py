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

def drawText(): #  можно потом удалить наверное
    # textsurface = myfont.render("calc vec: " + str(math.floor(vec2.as_polar()[1])), False, (0, 0, 0))
    # textsurface = myfont.render("calc vec: " + str(vec2.as_polar()) + ' calc angle: ' + str(math.degrees(math.acos(vec_y))) + " " + str(math.degrees(math.asin(vec_x))), False, (0, 0, 0))
    textsurface2 = myfont.render("R   vec: " + str(robot.vector), False, (0, 0, 0))
    textsurface3 = myfont.render("polar: " + str(math.floor(robot.vector.as_polar()[1])), False, (0, 0, 0))
    # screen.blit(textsurface, (10, 10))
    screen.blit(textsurface2, (10, 50))
    screen.blit(textsurface3, (10, 100))
