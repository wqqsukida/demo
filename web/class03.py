#!/usr/bin/env python
# coding:utf-8
class test1:
    def __init__(self):
        self.__arg = 'Dylan'
    @property
    def show(self):
        return self.__arg

class test2(object):
    def __init__(self):
        self.__arg = 'Elaine'
    @property
    def show(self):
        return self.__arg
    @show.setter
    def show(self,value):
        self.__arg =value

t1 = test1()
print t1.show
t1.show = 'Dylan 1'
print t1.show

t2 = test2()
print t2.show
t2.show = 'Elaine 1'
print t2.show