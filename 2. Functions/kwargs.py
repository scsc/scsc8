#!/usr/bin/env python
# -*- coding: utf-8 -*-

def generateInsertStatement(table, **kwargs):
    cols = []
    vals = []

    for col, val in kwargs.items():
        cols.append(col.replace("'", r"\'"))
        vals.append("'%s'" % (str(val)).replace('"', r'\"'))
    cols = ", ".join(cols)
    vals = ", ".join(vals)

    return 'INSERT INTO %s(%s) VALUES(%s);' % (
        table, cols, vals)



print generateInsertStatement("Person", name="John", surname= "Smith", career = "agent")

params = {"name": "Thomas", "surname" :"Anderson", "career": "hacker",}
print generateInsertStatement("workers", **params)



