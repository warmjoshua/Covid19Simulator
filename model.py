import controller, sys
import model 

from person import Person 
from movingPerson import Moving_Person

running = False
cycle_count = 0
people = set() 
object_type = None 

def world():
    return (controller.the_canvas.winfo_width(), controller.the_canvas.winfo_height())

def reset():
    global running, cycle_count, people 
    running = False 
    cycle_count = 0 
    people = set()
    Person.person_dict = {"Healthy": 0, "Infected": 0, "Recovered": 0, "Dead": 0}

def start():
    global running 
    running = True 

def stop():
    global running
    running = False

def step():
    start()
    update_all()
    stop()

def select_object(kind):
    global object_type 
    object_type = kind

def mouse_click(x, y):
    global object_type 
    if object_type =="Remove":
        my_set = people.copy()
        for person in my_set:
            if person.contains((x,y)):
                remove(person)
    elif object_type is None:
        pass 
    elif object_type == "Healthy Person":
        eval("add({}({},{},'Healthy'))".format("Person", x, y))
    elif object_type == "Moving Healthy Person":
        eval("add({}({},{},'Healthy'))".format("Moving_Person", x, y))
    elif object_type == "Infected Person":
        eval("add({}({},{},'Infected'))".format("Person", x, y))
    elif object_type == "Moving Infected Person":
        eval("add({}({},{},'Infected'))".format("Moving_Person", x, y))            
                          
def add(s):
    people.add(s)
    
def remove(s):
    people.remove(s)
    
def find(p):
    p_set = set()
    my_set= list(people)
    for person in my_set:
        if p(person):
            p_set.add(person)    
    return p_set
def update_all():
    global cycle_count
    if running:
        cycle_count += 1
        for person in people.copy():
            person.update()
        
def display_all():
    for o in controller.the_canvas.find_all():
        controller.the_canvas.delete(o)
    for p in people:
        p.display(controller.the_canvas)
        
    controller.the_progress.config(text=str(cycle_count)+" cycles/ " 
                                   + str(Person.person_dict["Healthy"]) + " Healthy/ " 
                                   + str(Person.person_dict["Infected"]) + " Infected/ "
                                   + str(Person.person_dict["Recovered"]) + " Recovered/ "
                                   + str(Person.person_dict["Dead"]) + " Dead" )
    
    
    
    
    
    
    
    
    