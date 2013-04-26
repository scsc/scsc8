#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Dummy(object):
    """
    This is the class example
    """
    def __init__(self, arg):
        self._arg = arg

    def method1(self, x):
        pass
    def _method2(self, x):
        pass

    @staticmethod
    def method3(arg1, arg2, *args, **kwargs):
        pass

    @classmethod
    def method4(cls, arg1, arg2, *args, **kwargs):
        pass
