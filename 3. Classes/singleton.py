#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Singleton(object):
    obj = None
    def __new__(cls,*args,**kwargs):
        if cls.obj is None:
            cls.obj = object.__new__(cls,*args,**kwargs)
        return cls.obj

o1 = Singleton()
o2 = Singleton()

print o1 is o2