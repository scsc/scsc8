#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Parent(object):
    def whoAmI(self) : return 'parent'

class Child(Parent):
    def whoAmI(self): return 'child'

x = Parent()
print x.whoAmI()

y = Child()
print y.whoAmI()
y.__class__ = Parent
print y.whoAmI()


class Abstract(object):
    def abstractMethod(self):
        raise NotImplementedError('Method is pure virtual')

a = Abstract()
a.abstractMethod() # Exception !