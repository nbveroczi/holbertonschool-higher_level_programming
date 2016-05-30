"""
@author: nbveroczi
"""
"""
Script that describes a TaskView Class:
This is a  script that utilizes private attributes and public methods
and inheritance.
Return: the value of title attribute  
"""   
#!/usr/bin/python
import Tkinter as tk

""" Class """
class TaskView(tk.Toplevel):
    
    """ Constructor """
    def __init__(self, master):
        tk.Toplevel.__init__(self, master)
        self.protocol('WM_DELETE_WINDOW', self.master.destroy)
        
        if not isinstance(master, tk.Tk):
            Exception("master is not a tk.Tk()") 
        self.master = master      
        
        #private attributes - Title lable
        self.__title_var = tk.StringVar()
        self.__title_lable = tk.Label(textvariable=self.__title_var)
        self.__title_lable.pack(side='right')
        #public attributes - Toggle button
        self.toggle_button = tk.Button(self, text="Reverse")
        self.toggle_button.pack(side='left')

    def update_title(self, title):
        if not isinstance(title, str):
            raise Exception("title is not a string")
        self.__title_var.set(title) 

    