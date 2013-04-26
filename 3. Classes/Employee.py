#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Employee(object):
    """
    Common Employee
    """
    empCount = 0
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self._salary = salary
        Employee.empCount += 1

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        self._salary = value

    @staticmethod
    def getCount():
        return Employee.empCount

    def __str__(self):
        return u"id = " + unicode(self.id) + u", Name : " + unicode(self.name) +  u", Salary: " + unicode(self.salary)


emp1 = Employee(1, "Thomas Anderson", 250)
emp1.salary = 1000
emp2 = Employee(2, "John Smith", 2500)

print emp1
print emp2
print "Total Employee %d" % Employee.getCount()


class Manager(Employee):
    def __init__(self, id, name, salary, inferiorsCount = 0):
        super(Manager, self).__init__(id, name, salary)
        self.__inferiorsCount = inferiorsCount

    inferiors = property(lambda self: self.__inferiorsCount)

    @inferiors.setter
    def inferiors(self, value):
        self.__inferiorsCount = value

    def __str__(self):
        return u"id =  %d, Name : %s, Salary: %.2f and has %d inferiors" % (self.id, self.name, self.salary, self.inferiors)

manager = Manager(3, "Trinity Ololo", 1150)
manager.salary = 2000
manager.inferiors = 2

print manager
print "Total Employee %d" % Employee.getCount()