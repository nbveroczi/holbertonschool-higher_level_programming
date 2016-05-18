# -*- coding: utf-8 -*-
"""
Created on Wed May 18 00:46:13 2016

@author: nbveroczi
"""
"""
Script Square:
This is a script that describes a Square Class with Private attributes, Public 
attributes and Public method.
Return: the area of the square(int)
"""
#!/usr/bin/python

''' Class '''
class Square():
    
    ''' Constructor '''
    def __init__(self, side_length):
        #private attributes
        self.__side_length = side_length
        self.__side_width = (int)
        self.__center = [int,int]
        self.__color = ("")
        #public attributes
        self.name = ("")
        
    ''' Destructor '''    
    def __del__(self):
        pass
    
    ''' Getter '''
    def get_side_length(self):
        return self.__side_length
        
    def get_center(self):
        return self.__get_center
        
    def get_color(self):
        return self.__color
        
    def get_name(self):
        return self.name
        
    ''' Setter '''
    def set_side_length(self, side_length):
        self.__side_length = side_length
        
    def set_center(self, center):
        self.__center = center
        
    def set_color(self, color):
        self.__color = color
        
    def set_name(self, name):
        self.name = name
        
    ''' Public Method '''    
    def area(self):
        return self.__side_length**2
        
        