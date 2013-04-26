#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

def timeLogging(func, *args, **kwargs):
    t = time.time()
    res = func(*args, **kwargs)
    print 'Calling: %s, returned %r elapsed time %f' % (func.__name__, res, time.time()-t)
    return res

def fibRec(n):
    if n == 0:
        return 0
    elif n < 3:
        return 1
    return fibRec(n-1) + fibRec(n-2)


def fibIter(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

timeLogging(fibRec, 40)
timeLogging(fibIter, 40)


