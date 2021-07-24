import time

from draw import *

class Robot():
    def __init__(self, x_start, y_start):   # задаем начальные координаты робота
        self.robot_height = 50  # размеры робота
        self.robot_width = self.robot_height
        self.angle = -90  # угол поворота
        self.speed = 0.0005    # скорость робота
        self.rotation_speed = 1.8   # скорость поворота
        self.cargoTaken = False
        self.cargoDelivered = False
        self.robotStarted = False   # робот запущен
        self.robotAuto = False      # ручное или автоматическое управление роботом
        self.vector = pygame.math.Vector2(1, 0) # вектор направления движения
        self.robot = pygame.Surface((self.robot_height, self.robot_width), pygame.SRCALPHA) # создание поверхности робота
        self.robot.fill(YELLOW) # заливка цветом

        pygame.draw.line(self.robot, WHITE, [10, 0], [37, 0], 9)    # линия на роботе
        self.robot_rect = self.robot.get_rect(center =(x_start,y_start))    # получение координат прямоугольника

        self.previous_x_pos = 0
        self.previous_y_pos = 0

    def draw(self):
        self.rotated_robot = pygame.transform.rotozoom(self.robot, self.angle, 0.9)     # повернутая поверхность
        self.robot_rect = self.rotated_robot.get_rect(center=self.robot_rect.center)    # получение координат повернутого прямоугольника
        screen.blit(self.rotated_robot, self.robot_rect)     # отрисовка робота на экране по координатам прямоугольника

    def rotation(self, direction):
        if direction == 1:
            self.angle -= self.rotation_speed # поворот поверхности
            if self.angle <= -359: self.angle = 0
            self.vector.rotate_ip(+self.rotation_speed) # поврот вектора движения

        if direction == -1:
            self.angle += self.rotation_speed
            if self.angle >= 359: self.angle = 0
            self.vector.rotate_ip(-self.rotation_speed)

    def movement(self, move): #какой то косяк с неровным движением
        if move == 1:
            self.robot_rect.center += self.vector * 5.5
        if move == -1:
            self.robot_rect.center -= self.vector * 5.5

    def getRobotPos(self):
        return self.robot_rect.center

    def goTo(self, x_pos, y_pos, Rob_x, Rob_y): # на вход подаем координату места, куда ехать

        if self.robotStarted and self.robotAuto:  # если робот запущен и в автоматическом режим, то едем
            # if not self.cargoTaken: # если груз не взято, то едем
            dx = Rob_x - x_pos  # расчет расстояния до пива
            dy = Rob_y - y_pos
            dist = math.sqrt(dx * dx + dy * dy)  # расстояние до пива
            if dist != 0:
                vec_x = dx / dist  # косинус
                vec_y = dy / dist  # синус
            else:
                vec_x, vec_y = 1, 1

            vec2 = pygame.math.Vector2(-vec_x, -vec_y)  # вектор пайгейма
            vec2.normalize()  # нормализация вектора

            if math.fabs(self.vector.as_polar()[1] - vec2.as_polar()[1]) <= 1:
                self.movement(1)

            elif (vec2.as_polar()[1]<=0 and self.vector.as_polar()[1]>=0):
                if (math.fabs(self.vector.as_polar()[1]) + math.fabs(vec2.as_polar()[1]) >=180):
                    self.rotation(1)
                else:
                    self.rotation(-1)

            elif (vec2.as_polar()[1]>=0 and self.vector.as_polar()[1]<=0):
                if (math.fabs(self.vector.as_polar()[1]) + math.fabs(vec2.as_polar()[1]) >=180):
                    self.rotation(-1)
                else:
                    self.rotation(1)

            elif (self.vector.as_polar()[1]>0 and vec2.as_polar()[1]>0) :
                if math.fabs(self.vector.as_polar()[1]) > math.fabs(vec2.as_polar()[1]):
                    self.rotation(-1)
                else:
                    self.rotation(1)

            elif (self.vector.as_polar()[1]<0 and vec2.as_polar()[1]<0):
                if math.fabs(self.vector.as_polar()[1]) > math.fabs(vec2.as_polar()[1]):
                    self.rotation(1)
                else:
                    self.rotation(-1)

    def startRobot(self):
        self.robotStarted = True

    def stopRobot(self):
        self.robotStarted = False

    def auto(self):
        self.robotAuto = True

    def manual(self):
        self.robotAuto = False
