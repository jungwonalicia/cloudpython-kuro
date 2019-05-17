class Car:
    color = '검정'
    speed = 100
    
    def __init__(self, color, speed):
        self.color = color
        self.speed = speed
        
    def speed_up(self):
        print('속도를 Up')
        
    def speed_down(self):
        print('속도를 Down')

class Truck(Car):
    적재량 = 1
    
    def __init__(self, color, speed, 적재량):
        Car.__init__(self, color, speed)
        self.적재량 = 적재량
        
    def 적재량알아보기(self):
        return self.적재량


truck1 = Truck('red', 200, 2)
print(truck1.color) # Car
print(truck1.speed) # Car
print(truck1.적재량) # Truck

print('--------------------')
truck2 = Truck('green', 300, 3)
print(truck2.color) # Car
print(truck2.speed) # Car
print(truck2.적재량) # Truck

print('--------------------')
truck1.speed_up()
truck1.speed_down()
print(truck1.적재량알아보기())

print('-------------------------')






    
    
    
    
    
    