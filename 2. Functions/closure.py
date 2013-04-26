#!/usr/bin/env python
# -*- coding: utf-8 -*-

def simpleClosure(targetMaker):
    def multilpier(arg):
        return targetMaker * arg
    return multilpier

targetFunction = simpleClosure(10)

print targetFunction(5)

#####################
simpleClosure = lambda targetMaker: (
    lambda arg: (
        targetMaker * arg
        )
    )

targetFunction = simpleClosure(10)

print targetFunction(5)
