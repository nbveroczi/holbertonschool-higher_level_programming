# -*- coding: utf-8 -*-
"""
Created on Tue May 17 21:22:02 2016

@author: nbveroczi
"""
"""
Script Circle:
This is a script that describes a Circle Class with Private attributes, Public 
attributes and Public method.
Return: the area of the circle(float)
"""
#start
from math import pi

''' Class '''
class Circle():
    
    ''' Constructor '''
    def __init__(self, radius):
        #private attributes
        self.__radius = radius
        self.__center = [int,int]
        self.__color = ("")
        #public attributes
        self.name = ("")
        
    ''' Destructor '''
    def __del__(self):
        pass
    
    ''' Getter '''
    def get_radius(self):
        return self.__radius
        
    def get_center(self):
        return self.__center
        
    def get_color(self):
        return self.__color
        
    def get_name(self):
        return self.name
        
    ''' Setter '''
    def set_radius(self, radius):
        self.__radius = radius
        
    def set_center(self, center):
        self.__center = center
        
    def set_color(self, color):
        self.__color = color
        
    def set_name(self, name):
        self.name = name
        
    ''' Public Method '''               
    def area(self):
        return((self.__radius ** 2) * pi) #float
   
   
   
   
   
