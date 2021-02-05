import random
import model
class Person(object):
    
    person_dict = {"Healthy": 0, "Infected": 0, "Recovered": 0, "Dead": 0}
    radius = 8

    def __init__(self, x, y, status):
        self.set_location(x, y)
        self.set_dimension(16, 16)
        self.counter = 0
        self.status = status
        self.set_color()
        Person.person_dict[status] += 1
        
    def display(self, canvas):
        canvas.create_oval(self._x - self.radius, self._y - self.radius,
                           self._x + self.radius, self._y + self.radius, fill=self.color )
        
    def set_color(self):
        if self.status == "Healthy":
            self.color = "#008000"
        elif self.status == "Infected":
            self.color = "#FFA500"
        elif self.status == "Recovered":
            self.color = "#0000ff"
        else:
            self.color = "#FF0000"     
        
    def update(self):
        if self.status == "Infected":
            self.counter += 1
            if self.counter >= 10:
                death_rate = random.randint(1,100)
                if death_rate in range(1, 2):
                    self.status = "Dead"
                    Person.person_dict["Dead"] += 1
                    Person.person_dict["Infected"] -= 1
                elif death_rate in range(94,100):
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
                
                    
                    
                
    
    def get_location(self):
        return (self._x, self._y)
    
    def set_location(self, x, y):
        self._x = x 
        self._y = y
        
    def change_location(self, dx, dy):
        self._x += dx 
        self._y += dy 
        
    def get_dimension(self):
        return (self._width, self._height)
    
    def set_dimension(self, width, height):
        self._width = width 
        self._height = height
        
    def change_dimension(self, dw, dh):
        self._width += dw 
        self._height += dh 
        
    def distance(self, xy):
        return ((self._x - xy[0]) ** 2 + (self._y - xy[1]) ** 2) ** 0.5
    
    def contains(self, xy):
        return self.distance(xy) < self.radius       
               
               
               
