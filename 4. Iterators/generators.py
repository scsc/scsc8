#!/usr/bin/env python
# -*- coding: utf-8 -*-

def gGenerator():
    lst = range(20)
    for elem in lst:
        yield elem * elem

generator = gGenerator()
print generator

#print generator.next()
#print generator.next()

for sqm in generator:
    print sqm
