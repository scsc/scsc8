#!/usr/bin/env python
# -*- coding: utf-8 -*-

def curryFunction( x ) :
    def summ( y ) :
        return x + y
    return summ

print curryFunction(4)(2)

######################################

curryFunction = lambda x: lambda y: x + y

######################################

def processingFunction(x, y):
    return x + y


def curryFunction(x):
    return lambda(y): processingFunction(x, y)


curryFunction = lambda(x): lambda(y): processingFunction(x,y)

print curryFunction(4)(2)

