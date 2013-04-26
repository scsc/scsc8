#!/usr/bin/env python
# -*- coding: utf-8 -*-



def aCube(n):
    return n * n * n

def genMap(func, iterable):
    for item in iterable:
        yield func(item)



def mymap(func, iterable):
    return list(genMap(func, iterable))

lst = [1,2,2,3,4]
l = mymap(iterable=lst, func=aCube)

print l