#!/usr/bin/env python
# coding:utf-8

def outer02(fun):
    def wrapper(arg1):
        #fun(arg1)
        print '这是附加**功能'
        return fun(arg1)
    return wrapper

