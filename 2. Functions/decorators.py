#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
def timeLogger(function):
    def decor(*args, **kwargs):
        t = time.time()
        res = function(*args, **kwargs)
        print u'Returned %r elapsed time %f' % (res, time.time()-t)
        return res
    return decor

@timeLogger
def factorial(n):
    return reduce(lambda x,y:x*y,[1]+range(1,n+1))

factorial(38)


import threading

class Thread(threading.Thread):
    def __init__(self, f):
        threading.Thread.__init__(self)
        self.run = f

@Thread
def runOnOtherwiseThread():
    pass

runOnOtherwiseThread.start()