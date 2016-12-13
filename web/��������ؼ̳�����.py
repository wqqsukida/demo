#!/usr/bin/env python
# coding:utf-8
'''
python 2.2之前经典类的多重继承问题:
子类D按照深度优先的顺序继承父类的方法,所以导致从类B->A->C->顺序
python2.2之后增加新式类(object),利用广度优先,继承父类方法的顺序变为B->C->A

https://docs.python.org/release/2.2.3/whatsnew/sect-rellinks.html#SECTION000310000000000000000

    class A:
                  ^ ^  def save(self): ...
                 /   \
                /     \
               /       \
              /         \
          class B     class C:
              ^         ^  def save(self): ...
               \       /
                \     /
                 \   /
                  \ /
                class D
'''                
class A:#(object):
    def __init__(self):
        print 'This is A.'
    def save(self):
        print 'save method from A.'

class B(A):                 #继承A
    def __init__(self):
        print 'This is B.'
    
class C(A):                 #继承A
    def __init__(self):
        print 'This is C.'
    def save(self):
        print 'save method from C.'
class D(B,C):               #继承B，C
    def __init__(self):
        print 'This is D.'
arg = D()
arg.save()


    