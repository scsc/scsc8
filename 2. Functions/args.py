#!/usr/bin/env python
# -*- coding: utf-8 -*-

def calculateSumOfArgs(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum

print calculateSumOfArgs(42,444,555,666,32)



def listArgs(farg, *args):
     print "formal arg:", farg
     for arg in args:
         print "another arg:", arg

listArgs (1,2,3,4)

def listArgs(farg, *args):
    print "formal arg:", farg
    for i, arg in enumerate(args):
        print "position arg %i: %s" % (i, arg)

listArgs (1,2,3,4)