#!/usr/bin/env python
# -*- coding: utf-8 -*-


def fibonacci():
    a, b = 0, 1
    while 1:
        yield a
        a, b = b, a + b

f = fibonacci()



print f.next()
print f.next()
print f.next()
print f.next()
print f.next()
print f.next()