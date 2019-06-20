# coding:utf8
import time

def f(x,y):
    t1 = time.time()
    a = x+y
    t2 = time.time()
    print t2-t1
    return a

f(1,2)
