#!/usr/bin/env python
# -*- coding: utf-8 -*-

class ObjectCreator(object):
    pass

myObject = ObjectCreator()
print myObject

print type(myObject)


def classSelector(className):
     if className == 'spam':
         class Spam(object):
             pass
         return Spam
     else:
         class Sausage(object):
             pass
         return Sausage
Selected = classSelector('spam')
pieceOfSpam = Selected()

print Selected
print pieceOfSpam

#########################################################
def echo(self):
    print self.attribute

Spam = type('Spam', (), {'attribute': True, 'echo':echo})

spamObject = Spam()
print spamObject
spamObject.echo()
##########################################################

class Meta(type):
    def __new__(cls, name, bases, classDict):
        return super(Meta,cls).__new__(cls, name, bases, classDict)

    def getName(cls):
        return cls.__name__

def echo(self):
    print self.attribute

spamClass = Meta('Spam', (), {'attribute': True, 'echo':echo})

spamObject = spamClass()
print spamClass.getName()







