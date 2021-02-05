from tkinter import Button, Label, Canvas 
 
import model 
 
the_canvas = None 
the_progress = None 
 
 
def reset_button(parent, **config):
    return Button(parent, command=model.reset, **config)

def start_button(parent, **config):
    return Button(parent, command=model.start, **config) 

def stop_button(parent, **config):
    return Button(parent, command=model.stop, **config) 
 
def step_button(parent, **config):
    return Button(parent, command=model.step, **config) 
 
def object_button(parent, **config):
    def doit():
        model.select_object(config['text'])
    return Button(parent, command=doit, **config)
 
 
 
def simulation_canvas(parent, **config):
    global the_canvas 
    the_canvas = Canvas(parent, **config)
    the_canvas.bind("<ButtonRelease>", lambda event : model.mouse_click(event.x, event.y))
    return the_canvas

def progress(parent, **config):
    global the_progress
    the_progress = Label(parent, **config) 
    return the_progress

def repeater(root):
    model.update_all()
    model.display_all()
    root.after(30, repeater, root)