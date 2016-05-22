# -*- coding: utf-8 -*-
"""
@author: nbveroczi
"""
"""
Script Family:
This is script that describes a Person Class with attributes
Return: a Person Class with EYES_COLORS and GENRES 
"""
#!/usr/bin/python

""" Class """
class Person():
    
    """ Class attributes """
    EYES_COLORS = ["Blue", "Green", "Brown"]
    GENRES = ["Female", "Male"]
    
    """ Constructor """
    def __init__(self, id, first_name, date_of_birth, genre, eyes_color):
        #private attributes
        self.__id = id
        self.__first_name = first_name
        self.__date_of_birth = date_of_birth
        self.__genre = genre
        self.__eyes_color = eyes_color
        #public attribute
        self.last_name = ("")
        
    ''' Destructor '''
    def __del__(self):
        pass    
    
    ''' Getter - for retrieving the data '''
    def get_id(self):
        return self.__id
        
    def get_first_name(self):
        return self.__first_name
        
    def get_date_of_birth(self):
        return self.__date_of_birth
        
    def get_genre(self):
        return self.__genre
        
    def get_eyes_color(self):
        return self.__eyes_color
        
    """ Setter - for changing the data """
    
        
        


