#!/usr/bin/env python
# coding:utf-8

__author__ = 'Administrator'
import os;
import sys;
import time;

class DeleteLog:
    def __init__(self,filename,days):
        self.filename=filename;
        self.days=days;

    def delete(self):
        if os.path.exists(self.filename)==False:
            print(self.filename+ ' is not exists!!')
        elif os.path.isfile(self.filename):
            print(self.filename);
        elif os.path.isdir(self.filename):
            print(self.filename + ' is a path!');
            for i in [os.sep.join([self.filename,v]) for v in os.listdir(self.filename)]:
                if self.compare_file_time(i) and (os.path.isfile(i)):
                    os.remove(i);
                    print(i+' is removed!');

    def compare_file_time(self,file):
        time_of_last_mod=os.path.getatime(file);
        days_between=(time.time()-time_of_last_mod)/(24*60*60);
        if days_between>self.days:
            return True;
        return False;


if __name__=='__main__':
    path='/u01/app/diag/rdbms/orcl/orcl/trace';
    obj=DeleteLog(path,5);
    obj.delete();