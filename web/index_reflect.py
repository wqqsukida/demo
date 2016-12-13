#!/usr/bin/env python
# coding:utf-8
'''
from  web import account
urlstr = raw_input('input web_url:')
if urlstr == 'account/login':
    account.login()
elif urlstr == 'account/logout':
    account.logout() 
'''
import sys
while True:
    urlstr = raw_input("input web_url('account/login'or'account/logout'):")
    #if urlstr == 'account/login'or  'account/logout' :
    array = urlstr.split('/')
    try:    #将出现异常的字段放到try里
        module = __import__(array[0])#!!!一旦有异常就会跳到except,不会向下执行!!!
        func = getattr(module, array[1])
        func()
    except Exception,error: #捕捉异常，定义为 error对象
        print error
        print 'Please input account/login or account/logout'
    else:                   #不出现异常
        print 'successful'
        sys.exit()
    finally:                #无论是否出现异常都会输出
        print 'www.Dylan&Elaine.com'
