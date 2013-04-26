#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Reverse(object):
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def next(self):
        if self.index == 0:
            raise StopIteration
        self.index  = self.index - 1
        return self.data[self.index]

rev = Reverse("Test")
print rev.next()
print rev.next()


for x in Reverse("string"):
    print x
