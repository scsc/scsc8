#!/usr/bin/env python
# -*- coding: utf-8 -*-

L1 = [1, 2, 3, 4, 5, 22, 2]
L2 = [-2, 1, 3, 3, -6, 2, 33]
L3 = [2, 3, 3, 4, 5, 6, 7]
print map(lambda x, y, z : x + y + z, L1, L2, L3)


L = [4 , 5, 5, 6, 8, 2, 1, 3]
print reduce(lambda acml, val: acml * val, L, 1)



listToFilter = [22, 55, 33, 2, 4, 12, 3, 4]
print filter(lambda x: x % 2 == 0, listToFilter)
