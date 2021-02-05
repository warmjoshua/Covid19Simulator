from tkinter import Tk, Frame, TOP, LEFT, BOTTOM, RAISED, BOTH 

import controller 


root = Tk()
root.title("Covid-19 Simulator")
root.protocol("WM_DELETE_WINDOW", quit)

frame = Frame(root)

frame.pack(side=TOP) 
controller.reset_button(frame, text="Reset").pack(side=LEFT)
controller.start_button(frame, text="Start").pack(side=LEFT)
controller.stop_button(frame, text="Stop").pack(side=LEFT)
controller.step_button(frame, text="Step").pack(side=LEFT)
controller.object_button(frame, text="Healthy Person").pack(side=LEFT)   
controller.object_button(frame, text="Moving Healthy Person").pack(side=LEFT)
controller.object_button(frame, text="Infected Person").pack(side=LEFT)   
controller.object_button(frame, text="Moving Infected Person").pack(side=LEFT)
controller.object_button(frame, text="Remove").pack(side=LEFT)  
controller.progress(frame, text="0 updates/ 0 Healthy/ 0 Infected/ 0 Recovered/ 0 Dead", width=50, relief=RAISED).pack(side=LEFT)

controller.simulation_canvas(root, width=700, height=450, bg="white").pack(side=BOTTOM, expand=True, fill=BOTH)