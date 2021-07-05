import pygame
from pygame.locals import *

pygame.init()

screen_width = 600
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Demo HMI for robot simulation')

font = pygame.font.SysFont('Comic Sans MS', 30)

# цвета
bg = (144, 128, 168)
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)
grey = (110, 110, 110)


clicked = False
msg = "Waiting for command"


class button():
    # цвета кнопок и текста
    button_col = (201, 166, 253)
    hover_col = (177, 117, 229)
    click_col = (121, 80, 139)
    text_col = black
    width = 180
    height = 70

    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text

    def draw_button(self):

        global clicked
        action = False

        pos = pygame.mouse.get_pos()  # получение координат мыши

        # прямогульник кнопки
        button_rect = Rect(self.x, self.y, self.width, self.height)


        if button_rect.collidepoint(pos): # проверка попадения мыши в поверхность кнопки
            if pygame.mouse.get_pressed()[0] == 1:
                clicked = True
                pygame.draw.rect(screen, self.click_col, button_rect)
            elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
                clicked = False
                action = True
            else:
                pygame.draw.rect(screen, self.hover_col, button_rect)
        else:
            pygame.draw.rect(screen, self.button_col, button_rect)


        # помещение текста в кнопку
        text_img = font.render(self.text, True, self.text_col)
        text_len = text_img.get_width()
        screen.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 25))
        return action


start = button(75, 500, 'Start')
stop = button(325, 500, 'Stop')
left = button(75, 400, 'Turn left')

angle = 0
run = True
while run:

    screen.fill(bg)

    if left.draw_button():
        angle +=1
        print(angle)

    if start.draw_button():
        msg = "Robot started"
        print("start")
    if stop.draw_button():
        msg = "Robot stopped"
        print("stop")


    pygame.draw.rect(screen, grey, (100, 100, 400, 50))
    message = font.render(msg, True, white)
    screen.blit(message, (120, 110))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
