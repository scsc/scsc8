#!/usr/bin/env python
# -*- coding: utf-8 -*-

def IsMappingType(obj, require_set=False):

    if require_set and not hasattr(obj, '__setitem__'):
        return False
    if hasattr(obj, 'keys') and hasattr(obj, '__getitem__'):
        return True
    else:
        return False

def IsSequenceType(obj, require_set=False):

    if require_set and not hasattr(obj, '__setitem__'):
        return False
    if (not hasattr(obj, 'keys')) and hasattr(obj, '__getitem__'):
        return True
    else:
        return False

list = [2,2,2,2,3]
string = "Hello, i'm a simple strring"
dict = {'a':1,'b':2,'c':3}

print IsMappingType(dict, require_set=True)
print IsSequenceType(list, require_set=True)
print IsSequenceType(string,require_set=False)