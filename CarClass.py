class Car:
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        if self.__speed >= 5:
            self.__speed -= 5
        else:
            self.__speed = 0

    def get_speed(self):
        return self.__speed


car = Car(2015, "Ferrari")
for _ in range(5):
    car.accelerate()
    print("Current speed:", car.get_speed())
car.brake()
print("Speed after braking:", car.get_speed())
