
from robot import Robot
from beer import Beer
from draw import *
import messages
from settings import *


robot = Robot(width/2, height/2) # создание робота
beer = Beer()   # создание пива

running = True
while running:
    clock.tick(60) # 60 fps

    for event in pygame.event.get(): # перебирает события
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:# -------------------------------------------------
            if event.key == pygame.K_SPACE: robot.startRobot() # если нажали пробел, то робот включен


        if event.type == pygame.KEYDOWN:# -------------------------------------------------
            if event.key == pygame.K_LCTRL: robot.stopRobot() # если нажали ctrl, то робот выключен



    drawWindow()

    beer.draw()

    robot.draw()

    pygame.image.save(screen, 'pic.png')

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



    #textsurface = myfont.render("calc vec: " + str(math.floor(vec2.as_polar()[1])), False, (0, 0, 0))
    #textsurface = myfont.render("calc vec: " + str(vec2.as_polar()) + ' calc angle: ' + str(math.degrees(math.acos(vec_y))) + " " + str(math.degrees(math.asin(vec_x))), False, (0, 0, 0))
    textsurface2 = myfont.render("R   vec: " + str(robot.vector), False, (0, 0, 0))
    textsurface3 = myfont.render("polar: " + str(math.floor(robot.vector.as_polar()[1])), False, (0, 0, 0))
    #screen.blit(textsurface, (10, 10))
    screen.blit(textsurface2, (10, 50))
    screen.blit(textsurface3, (10, 100))

    keys = pygame.key.get_pressed()  # список, в который помещается нажатая кнопка
    if keys[pygame.K_LEFT]:
        robot.rotation(-1)
    if keys[pygame.K_RIGHT]:
        robot.rotation(1)
    if keys[pygame.K_UP]:
        robot.movement(1)
    if keys[pygame.K_DOWN]:
        robot.movement(-1)

    pygame.display.flip()
    #pygame.display.update()  # обновление окна

pygame.quit()