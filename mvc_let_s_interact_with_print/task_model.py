"""
@author: nbveroczi
"""
"""
Script that describes a TaskModel Class:
This is a  script that utilizes private attributes and public methods.
Return: the value of title attribute and reverse it as well.  
"""   
#!/usr/bin/python

""" Class """
class TaskModel():

    """ Constructor """
    def __init__(self, title):
        if type(title) is not str or not title:
            raise Exception("title is not a string")
        #private attributes
        self.__title = title        
        self.__callback_title = None
        
    """ Getter - for retrieving the data """
    def get_title(self):
        return self.__title
        
    """ Setter - for changing the data """    
    def set_callback_title(self, callback_title):
        self.__callback_title = callback_title
        
    def toggle(self):
        self.__title = self.__title[::-1]
        if self.__callback_title != None:
            self.__callback_title(self.__title)
    
    def __str__(self):
        return self.__title            
            