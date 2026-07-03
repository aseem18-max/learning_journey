# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import time

def obvious_search(L, k):
    '''This function is the the most easiest but yet most time
    inefficient way of finding an elmemnt in a list.
    '''
    for x in L:
        if x==k:
            return 1
    return 0

def binary_search(L, k):
    '''This function is an alternative for the obvious search. It does
    exactly what is expected from the obvious_search, but in an efficient way.
    This method is popularly called the binary search.
    '''
    begin=0
    end=len(L)-1
    while(end-begin>1):
        mid=(begin+end)//2
        if(L[mid]>k):
            end=mid-1
        if(L[mid]==k):
            return 1
        if(L[mid]<k):
            begin=mid+1
    if(L[begin]==k or L[end]==k):
        return
    else:
        return 0
            
def rbinary_search(L, k, begin, end):
    '''This will recursively compute binary search.'''
    
    #if begin and end are same then we just need to check L[begin]
    if(begin==end):
        if(L[begin]==k):
            return 1
        else:
            return 0
        
    #if begin and end are consecutive then check them individually
    if(end-begin==1):
        if(L[end]==k or L[begin]==k):
            return 1
        else:
            return 0
        
    
    if(end-begin>1):
        mid=(begin+end)//2
        if(L[mid]>k):
            end=mid-1
        if(L[mid]<k):
            begin=mid+1
        if(L[mid]==k):
            return 1
    if(end-begin<0):
        return 0
    return rbinary_search(L, k, begin, end)
    

l=list(range(10000000))

a=time.time()
obvious_search(l, 9999999)
b=time.time()
print(b-a)

c=time.time()
binary_search(l, 9999999)
d=time.time()
print(d-c)

e=time.time()
rbinary_search(l, 9999999, 0, len(l)-1)
f=time.time()
print(f-e)
