#!/usr/bin/env python
# coding:utf-8
def outer(fun):
    def wrapper(arg):
        print '这是附加验证功能'
        fun(arg)
    return wrapper   

@outer
def fun1(arg):
    print 'This is fun1.',arg
@outer
def fun2(arg):
    print 'This is fun2.',arg

fun1('Dylan')
fun2('Elaine')