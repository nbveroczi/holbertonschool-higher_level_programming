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
#import json
#import os.path

""" Class """
class Person():
    
    """ Class attributes """
    EYES_COLORS = ["Blue", "Green", "Brown"]
    GENRES = ["Female", "Male"]
    
    """ Constructor """
    """__init__ is the initializer for the class. It gets passed whatever the \
    primary constructor was called """
    def __init__(self, id, first_name, date_of_birth, genre, eyes_color):
        if type(id) is not int or id < 0:
            raise Exception("id is not an integer")
        if type(first_name) is not str or len(first_name) == 0:
            raise Exception("first_name is not a string")
        if type(date_of_birth) is not list or len(date_of_birth) != 3:
            raise Exception("date_of_birth is not a valid date") 
        if date_of_birth[0] < 1 or date_of_birth[0] > 12:
            raise Exception("date_of_birth is not a valid date")  
        if date_of_birth[1] < 1 or date_of_birth[1] > 31:
            raise Exception("date_of_birth is not a valid date")  
        if type(genre) is not str and not genre in Person.GENRES:
            raise Exception("genre is not valid")
        if type(eyes_color) is not str and not eyes_color in Person.EYES_COLOR:
            raise Exception("eyes_color is not valid")              
        #private attributes
        self.__id = id
        self.__first_name = first_name
        self.__date_of_birth = date_of_birth
        self.__genre = genre
        self.__eyes_color = eyes_color
        #public attribute
        self.last_name = ("")
    
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
    def set_id(self, id):
        self.__id = id
        
    def set_first_name(self, first_name):
        self.__first_name = first_name
        
    def set_date_of_birth(self, date_of_birth):
        self.__date_of_birth = date_of_birth
        
    def set_genre(self, genre):
        self.__genre = genre
        
    def set_eyes_colors(self, eyes_colors):
        self.__eyes_color = eyes_colors
        
    """ Public Methods """
    
    """ Base Class Descriptions """   
    def __str__(self):
        return self.__first_name + " " + self.last_name

    def is_male(self):
        if self.__genre == "Male":
            return True
        else:
            pass
        
    def age(self):
        if self.__date_of_birth[0] > 5 and self.__date_of_birth[1] > 20:
            return (2015 - self.__date_of_birth[2])
        else:
            return (2016 - self.__date_of_birth[2])    
       
    """ Comparison Magic Methods """
    #Defines behavior for the equality operator, ==.            
    def __eq__(self, other):
        return self.age() == other.age()
     #Defines behavior for the inequality operator, !=.       
    def __ne__(self, other):
        return self.age() != other.age()
    #Defines behavior for the less-than operator, <.  
    def __lt__(self, other):
        return self.age() < other.age()
    #Defines behavior for the greater-than operator, >.
    def __gt__(self, other):
        return self.age() > other.age()
    #Defines behavior for the less-than-or-equal-to operator, <=.    
    def __le__(self, other):
        return self.age() <= other.age()
    #Defines behavior for the greater-than-or-equal-to operator, >=.    
    def __ge__(self, other):
        return self.age() >= other.age()
        
""" Additional Class Descriptions """
class Baby(Person):
    def can_run(self):
        return False
    def need_help(self):
        return True
    def is_young(self):
        return True
    def can_vote(self):
        return False

class Teenager(Person):
    def can_run(self):
        return True
    def need_help(self):
        return False
    def is_young(self):
        return True
    def can_vote(self):
        return False

class Adult(Person):
    def can_run(self):
        return True
    def need_help(self):
        return False
    def is_young(self):
        return False
    def can_vote(self):
        return True
            
class Senior(Person):
    def can_run(self):
        return False
    def need_help(self):
        return True
    def is_young(self):
        return False
    def can_vote(self):
        return True
    
    
    
        
        


