
from robot import Robot
from beer import Beer
from draw import *
from settings import *
import sub


def manual():
    keys = pygame.key.get_pressed()  # список, в который помещается нажатая кнопка
    if keys[pygame.K_LEFT]:
        robot.rotation(-1)
    if keys[pygame.K_RIGHT]:
        robot.rotation(1)
    if keys[pygame.K_UP]:
        robot.movement(1)
    if keys[pygame.K_DOWN]:
        robot.movement(-1)

sub.start() # запуск мктт

robot = Robot(width/2, height/2) # создание робота
beer = Beer()   # создание пива

running = True
while running:
    clock.tick(60) # 60 fps

    for event in pygame.event.get(): # перебирает события
        if event.type == pygame.QUIT:
            running = False

    drawWindow()

    beer.draw()

    robot.draw()

    surf = pygame.Surface((850, 650))
    surf.blit(screen, (0, 0))

    #print(str(sub.get_msg()))

    # включение/отключение робота, выбор режима работы: авто/ручной
    if str(sub.get_msg()) == "Start": robot.startRobot()
    if str(sub.get_msg()) == "Auto": robot.auto()
    if str(sub.get_msg()) == "Manual":
        robot.manual()
        manual()
    if str(sub.get_msg()) == "Stop": robot.stopRobot()


    if robot.cargoTaken == True:    # если груз взят, то везем его
        robot.goTo(deliver_pos[0], deliver_pos[1])
        if robot.robot_rect.collidepoint(deliver_pos):
            robot.cargoTaken = False
            robot.cargoDelivered = True
            beer.setBeerPos(deliver_pos)

    elif not robot.cargoDelivered:  # если груз не взят и не доставлен
        robot.goTo(beer.getBeerPos()[0], beer.getBeerPos()[1])
        if robot.robot_rect.collidepoint(beer.getBeerPos()):  # определяет пересечение поверхности робота и поверхности пива
            robot.cargoTaken = True
            beer.beerTaken()  # при взятии пива удаляет его с экрана

    else:   # если груз доставлен, то уезжаем
        robot.goTo(500,500)



    pygame.display.flip()
    #pygame.display.update()  # обновление окна

pygame.quit()