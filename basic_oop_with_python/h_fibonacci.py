# -*- coding: utf-8 -*-
"""
Created on Tue May 17 18:31:30 2016

@author: nbveroczi
"""
"""
Function Fibonacci:
This is a function that computes the fibonacci number of the parameter using 
loops.  
Return: fibonacci number of parameter
"""
def fibonacci(x):
    
#start

    if x<2:
        return x
    else: 
        return fibonacci(x-1)+fibonacci(x-2)
    
    
        