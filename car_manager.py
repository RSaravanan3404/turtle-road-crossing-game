from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


def car_property(new_car):
    new_car.shapesize(stretch_wid=1, stretch_len=2)
    new_car.penup()
    new_car.color(random.choice(COLORS))


class CarManager:
    def __init__(self):
        self.lane1_cars = []
        self.lane2_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car_at_lane1(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            car_property(new_car)
            random_y = random.randint(-230, -30)
            new_car.goto(300, random_y)
            self.lane1_cars.append(new_car)

    def create_car_at_lane2(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            car_property(new_car)
            random_y = random.randint(30, 230)
            new_car.goto(-300, random_y)
            self.lane2_cars.append(new_car)

    def move_cars(self):
        for car in self.lane2_cars:
            car.forward(self.car_speed)
        for car in self.lane1_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
