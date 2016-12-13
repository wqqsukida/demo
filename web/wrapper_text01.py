#!/usr/bin/env python
# coding:utf-8
#from wrapper01 import outer
from wrapper02 import outer02
#@outer
@outer02
def func01(arg):
    print 'This is func01!',arg
    return 'func01 return'
#func01('test')
report = func01('test')
print report