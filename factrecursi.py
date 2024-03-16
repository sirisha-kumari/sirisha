# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 12:43:21 2024

@author: SIRISHA KUMARI
"""

#factorial
def fact(n):
    if n==0:
        return 1
    return(n*fact(n-1))
print(fact(5))
