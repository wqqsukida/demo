#!/usr/bin/env python
# coding:utf-8
def outer(fun):
    def wapper():
        print '这是附加验证功能'
        result = fun()
        return result
    return wapper   

@outer
def fun1():
    print 'This is fun1.'
    return 'fun1 return.'
@outer
def fun2():
    print 'This is fun2.'
    return 'fun2 return.'
response1 = fun1()
print response1
response2 = fun2()
print response2