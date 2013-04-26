#!/usr/bin/env python
# -*- coding: utf-8 -*-




try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except IOError as e:
    print u"Ошибка ввод/вывода", e
except ValueError:
    print u"Не удается преобразовать данные к целому типу"
except:
    print u"Внезапная неизвестная ошибка "
    raise