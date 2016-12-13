#!/usr/bin/env python
# coding:utf-8
'''
class car:
    cartype = '日系汽车'
    @staticmethod
    def gear():
        print '手动挡/自动挡'
    def __init__(self,brand,variety):
        self.arg1 = brand
        self.arg2 = variety
    def carstr(self):
        print self.arg2
            
        
car1 = car('本田','雅阁')   
car2 = car('丰田','凯美瑞')

print car2.arg1,car2.arg2,car.cartype
car1.carstr()
car.gear()
car1.gear()
'''
class car(object):
    cartype = '日系汽车'
    @staticmethod
    def gear():
        print '手动挡/自动挡'
    def __init__(self,brand,variety,num):
        self.arg1 = brand
        self.arg2 = variety
        self.__Num = num
    def carstr(self):
        print self.arg2
    '''
    @property
    def num(self):
        return self.__Num
    @num.setter
    def num(self,arg):
        self._Num = arg
    '''
            
        
car1 = car('本田','雅阁','京RWQ521')   
car2 = car('丰田','凯美瑞','京QWQ521')

#print car2.arg1,car2.arg2,car.cartype
#car1.carstr()
#car.gear()
#car1.gear()
#print car2.num
#car2.num = '京NWQ521'
#print car2.num
print car2._car__Num
car2._car__Num = '京NWQ521'
print car2._car__Num
'''
class Foo:
    def __init__(self):         #构造函数
        pass
    def __del__(self):          #析构函数
        print 'I will be destoried by IDE!'
    def __call__(self):
        print 'call'
#Foo() #对类直接加()相当于执行__init__函数
f1 = Foo()

f1() #对象直接加()相当于执行类里的__call__方法
'''

class Elaine:               #父类
    def __init__(self):
        pass
    def fun_Elaine(self):
        print 'I`m Elaine.'
        
class Dylan(Elaine):        #子类
    def __init__(self):
        pass
    def fun_Dylan(self):
        print 'I`m Dylan.'
    def fun_Elaine(self):   #子类继承并修改父类方法
        print 'I love Elaine!'
    '''
    def fun_Elaine(self):   #子类在父类基础上添加
        Elaine.fun_Elaine(self)
        print 'I love Dylan!'
    '''
#E = Elaine()
#E.fun_Elaine()
D = Dylan()         #子类生成对象
D.fun_Elaine()      #子类继承父类方法
'''
python 2.2之后产生新式类 object
修复经典类关于多重继承父类的bug
'''