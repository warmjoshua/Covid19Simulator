import math, random 
from person import Person 
import model 

class Moving_Person(Person):


    def __init__(self, x, y, status):
        Person.__init__(self, x, y, status)
        self.randomize_angle()
        self.randomize_speed()
        
    def update(self):    
        if self.status != "Dead":
            self.move()
        if self.status == "Infected":
            self.counter += 1
            if self.counter >= 10:
                death_rate = random.randint(1,100)
                if death_rate in range(1, 2):
                    self.status = "Dead"
                    Person.person_dict["Dead"] += 1
                    Person.person_dict["Infected"] -= 1
                elif death_rate in range(94, 100):
                    self.status = "Recovered"
                    Person.person_dict["Recovered"] += 1
                    Person.person_dict["Infected"] -= 1
                self.set_color()
                self.counter = 0
                
        elif self.status == "Healthy":
            my_set = model.find(lambda x: self.contains((x._x, x._y)) and x.status == "Infected")
            if len(list(my_set)) != 0:
                self.status = "Infected"
                self.set_color()
                Person.person_dict["Healthy"] -= 1
                Person.person_dict["Infected"] += 1
    def get_angle(self):
        return self._angle 
    
    def set_angle(self, angle):
        self.angle = angle
        
    def get_speed(self):
        return self._speed 
    
    def set_speed(self, speed):
        self._speed = speed 
        
    def set_velocity(self, speed, angle):
        self.set_speed(speed)
        self.set_angle(angle)
        
    def randomize_angle(self):
        self._angle = 2 * math.pi * random.random()
    
    def randomize_speed(self):
        self._speed = random.randint(3,7)
        
    def move(self):
        self.change_location(self._speed * math.cos(self._angle),
                             self._speed * math.sin(self._angle))
        self.wall_bounce()
        
    def bounce(self, barrier_angle):
        self._angle = 2 * barrier_angle - self._angle
        
    def wall_bounce(self):
        x,y = self.get_location()
        w,h = self.get_dimension()
        mw, mh = model.world()
        
        left_x = x - w/2 
        right_x = x + w/2
        top_y = y - h/2 
        bottom_y = y + h/2
        
        if left_x < 0:
            self.bounce(math.pi/2)
            self.change_location(-2 * left_x, 0)
        elif right_x > mw:
            self.bounce(math.pi/2)
            self.change_location(2 * (mw - right_x), 0)
        
        if top_y < 0:
            self.bounce(0)
            self.change_location(0, -2 * top_y)
        elif bottom_y > mh:
            self.bounce(0)
            self.change_location(0, 2 * (mh - bottom_y))
        
        
        
        