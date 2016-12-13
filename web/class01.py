#!/usr/bin/env python
# coding:utf-8
'''
class Person:
    detail = 'Dylan love Elaine forever!'
    def __init__(self,name,age,profession):
        self.Name = name
        self.Age = age
        self.Profession = profession
Dylan = Person('Dylan','29','pdev&it')
Elaine = Person('Elaine','30','CTOSA')

print Dylan.Name,Elaine.Name
print Person.detail
'''


class  Person():                               #创建类
    detail = 'Dylan love Elaine forever!'    #静态字段（属于类的字段）
    def __init__(self,name,age,profession,secret):  #__init__实例化，动态字段（属于对象）
        self.Name = name 
        self.Age = age
        self.Profession =profession
        self.__Secret = secret               #----私有字段
    def showyourself(self):                  #----在类里定义显示私有字段的函数
        print self.__Secret                  
    @property                                #----利用特性可以直接调用私有字段
    def Secret(self):
        return self.__Secret
    @Secret.setter                           #----利用特性对私有字段做更改
    def Secret(self,arg):
        self.__Secret == arg
    def __happyalllife(self):                      #----私有方法
        return True
    def study(self):                         #动态方法（属于对象）
        print self.Name + ' is study hard now.'
    @staticmethod
    def love():
        print 'Elaine love Dylan forever!'   #静态方法（属于类)
    @property                                #特性
    def pro(self):
        print 'Elaine and Dylan happy all life together.'
Elaine = Person('Elaine','30','CTOSA',False)
Dylan = Person('Dylan','29','IT/Pydev',False)
'''
print Elaine.Name,Dylan.Name #对象访问动态字段
print Person.detail #类访问静态字段

Elaine.study() #对象访问动态方法
Dylan.study()

Person.love() #类访问静态方法

Elaine.love() #对象还可以访问静态方法
print Elaine.detail #对象访问静态字段

Elaine.pro#对象访问特性

#print Elaine.Secret #直接无法显示私有字段
Elaine.showyourself()
print Elaine.Secret  #利用特性直接访问私有字段
print Elaine._Person__Secret #直接调用私有字段

print Elaine._Person__happyalllife()
'''
print Elaine.Secret    #利用特性调用私有字段，只读
Elaine.Secret = 'none' #更改私有字段
print Elaine.Secret    #重新调用私有字段

'''
类里三种结构：
 1.字段： 如:
        def __init__(self):     #动态字段 
        detail    #静态字段
 2.方法: 如:
        def  study(self):    #动态方法 
        @staticmethod
        def love():    #静态方法
 3.特性：如:
        @property
        def pro(self):    
'''
