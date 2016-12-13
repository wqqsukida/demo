#!/usr/bin/env python
# coding:utf-8
#@Author Dylan
def outer(fun):
    def wrapper():
        print '这是附加验证功能'
        fun()
    return wrapper   
'''
@outer
def fun1():
    print 'This is fun1.'
@outer
def fun2():
    print 'This is fun2.'

fun1()
fun2()
'''