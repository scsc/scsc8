#!/usr/bin/env python
# -*- coding: utf-8 -*-

list = [1, 2, 3]
for i in list :
   print(i)
############################################
sequence = "sample sequence"

it = iter(sequence)
while True:
    try:
        value = it.next()
    except StopIteration:
        break
    print value
##############################################











