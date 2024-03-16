# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 10:03:32 2024

@author: SIRISHA KUMARI
"""

#write a func to calculate sum of 1st and last of a number
def sum(a):
    l=a%10
    while a>10:
        a=a//10
    print(l+a)
sum(785)
    
    