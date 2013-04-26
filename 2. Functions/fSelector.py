#!/usr/bin/env python
# -*- coding: utf-8 -*-

def fSelector(selector):
    if selector < 0:
        def fSqr(x):
            return x * x
        return fSqr
    else:
        def fCube(x):
            return x * x * x
        return fCube

def operate(L, function):
    res = [function (elem) for elem in L]
    return res

L = [1, 2, 3, 100]
print operate(L, fSelector(1))

###################################################
def fSelector(selector):
    if selector < 0:
        return lambda(x): x * x
    else:
        return lambda(x): x * x * x


L = [1, 2, 3, 100]
print operate(L, fSelector(-1))

##################################################
print (lambda x: x * x)(5)
