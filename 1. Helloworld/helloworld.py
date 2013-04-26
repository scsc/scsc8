#!/usr/bin/env python
# -*- coding: utf-8 -*-

print type("Hello, world")
print type([1,2,3,4,5])
print type ({'a':1, 'b':2})
print type((1,2,3,4,5))
print "Hell".startswith("Hel")

a,b,c,d,e = 1,2,3,4,5

print a
print b
print c
print d
print e


t = (1,)

print type (t)


t = 1,2,4
print type(t)

L= [1,2,3,4,5]
L1 = L.append(2)# DO NOT DO THIS! This is a common mistake!
print L1 # None!
L.append(33)
print L


L = [x**2 for x in range(10) if x%2 != 0]
print L


for i, x in enumerate(range(10)):
    print i, x



x= range(1,10,2)
print x

s= [1,2,3,4,5]
s1 = s[:]
print s1
s2 = s[1:]
print s2

s3 = s[-2:]
print s3

s4 = s[1:4:2]
print s4

list = [1, 2, 3, 'Вася Пупкин', 5]
print list

ingredients = ['bacon', 'sausages', 'spam', 'spam']
print 'Ingredients are: %s.' % ', '.join(ingredients)