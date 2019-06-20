# coding:utf8
import os
import requests
import time
from PIL import Image, ImageFilter
from ZFCheckCode import recognizer, trainner


@profile
def discode():
     trainner.update_model() 
     code = recognizer.recognize_checkcode('/home/xiang/mygit/学习记录和随笔/代码性能调试/checkcode.gif')
     return code

if __name__=="__main__":
    #time_start = time.time()
    text = discode()
    print text
    #time_finish = time.time()
