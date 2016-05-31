"""                                                                           
@author: nbveroczi                                                            
"""
"""                                                                           
Script that describes a TaskController Class:                                 
This is a  script that utilizes private attributes and public methods         
and inheritance.                                                             
Return: the value display should be current value of model                    
"""
#!/usr/bin/python                                                             
import Tkinter as tk
from task_model import TaskModel
from task_view import TaskView

""" Class """
class TaskController():

    """ Constructor """
    def __init__(self, master, model):
        if not isinstance(master, tk.Tk):
            raise Exception("master is not a tk.Tk()")
        if not isinstance(model, TaskModel):
            raise Exception("model is not a TaskModel")
        # private attributes
        self.__model = model
        # create the view
        self.__view = TaskView(master)
        # link view elements with controller
        self.__view.toggle_button.config(command=self.reverse_string)
        self.title_change(self.__model.get_title())

    # model from view elements
    def reverse_string(self):
        self.__model.set_callback_title(self.title_change)
        self.__model.toggle()
        
    # update view from model
    def title_change(self, title):
        self.__view.update_title(title)
