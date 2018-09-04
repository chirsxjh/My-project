# python代码性能及时间调试

### time模块

* 使用计时差法来计算代码所运行的时间

```
# coding:utf8
import time

def f(x,y):
    t1 = time.time()
    a = x+y
    t2 = time.time()
    print t2-t1
    return a

f(1,2)
```

运行结果

* 也可以使用 ```time python yourprogram.py```命令进行整个程序所运行的时间

* > real — 指的是实际耗时,user — 指的是内核之外的 CPU 耗时,ys — 指的是花费在内核特定函数的 CPU 耗时.

------

### 使用  profiler 逐行计时和分析执行的频率

使用pip进行安装```pip install line_profiler```

安装完成后，将获得一个新模块称为 ``` line_profiler ```和  ```kernprof.py ```可执行脚本

为了使用这个工具，首先在你想测量的函数上设置  @profile 修饰符。不需要引入任何东西。 kernprof.py 脚本会在运行时自动注入你的脚本。
其中```per hit```点击率可以看做是TPS的一种特定情况。点击率更能体现用户端对服务器的压力。TPS更能体现服务器对客户请求的处理能力。
每秒钟用户向web服务器提交的HTTP请求数。这个指标是web 应用特有的一个指标；web应用是“请求-响应”模式，用户发一个申请，服务器就要处理一次，所以点击是web应用能够处理的交易的最小单位。如果把每次点击定义为一个交易，点击率和TPS就是一个概念。容易看出，点击率越大。对服务器的压力也越大，点击率只是一个性能参考指标，重要的是分析点击时产生的影响。
需要注意的是，这里的点击不是指鼠标的一次“单击”操作，因为一次“单击”操作中，客户端可能向服务器发现多个HTTP请求
一旦你得到了你的设置了修饰符  @profile 的代码，使用  kernprof.py 运行这个脚本。
使用命令```kernprof -l -v fib.py```运行你的程序

```
# coding:utf8
import os
import requests
import time
from PIL import Image, ImageFilter
from ZFCheckCode import recognizer, trainner


'''
def getcode():
    os.mkdir('yanzhengma')
    img = requests.get('http://jwgl1.hbnu.edu.cn/(S(bwjxdsvyr3x3gs55v40kiy55))/CheckCode.aspx?').content
    with open('yanzhengma/mama.gif','wb') as imgfile:
        imgfile.write(img)
'''
#@profile
def discode():
     trainner.update_model() 
     #time_start = time.time()
     code = recognizer.recognize_checkcode('/home/xiang/mygit/学习记录和随笔/代码性能调试/checkcode.gif')
     #time_finish = time.time()
     return code

if __name__=="__main__":
    #time_start = time.time()
    text = discode()
    print text
    #time_finish = time.time()

```

运行结果：

```
Wrote profile results to primes.py.lprof
Timer unit: 1e-06 s

File: primes.py
Function: primes at line 2
Total time: 0.00019 s

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     2                                           @profile
     3                                           def primes(n): 
     4         1            2      2.0      1.1      if n==2:
     5                                                   return [2]
     6         1            1      1.0      0.5      elif n<2:
     7                                                   return []
     8         1            4      4.0      2.1      s=range(3,n+1,2)
     9         1           10     10.0      5.3      mroot = n ** 0.5
    10         1            2      2.0      1.1      half=(n+1)/2-1
    11         1            1      1.0      0.5      i=0
    12         1            1      1.0      0.5      m=3
    13         5            7      1.4      3.7      while m <= mroot:
    14         4            4      1.0      2.1          if s[i]:
    15         3            4      1.3      2.1              j=(m*m-3)/2
    16         3            4      1.3      2.1              s[j]=0
    17        31           31      1.0     16.3              while j<half:
    18        28           28      1.0     14.7                  s[j]=0
    19        28           29      1.0     15.3                  j+=m
    20         4            4      1.0      2.1          i=i+1
    21         4            4      1.0      2.1          m=2*i+3
    22        50           54      1.1     28.4      return [2]+[x for x
```

----

### 使用了多少内存？

memory_profiler模块用来基于逐行测量代码的内存使用。使用这个模块会让代码运行的更慢。

安装方法：```pip install memory_profiler```

与line_profiler相似，使用@profile装饰器来标识需要追踪的函数

其中```MemUsage```反应的是物理内存的使用状况

 ``increment``则是每步内存的增减情况 



运行命令：```python -m memory_profiler timing_functions.py```

输出结果如下图：

```
Line #    Mem usage    Increment   Line Contents
================================================
    16   71.426 MiB   71.426 MiB   @profile
    17                             def discode():
    18   73.441 MiB    2.016 MiB        trainner.update_model()
    19                                  #time_start = time.time()
    20   73.441 MiB    0.000 MiB        code = recognizer.recognize_checkcode('/home/xiang/mygit/学习记录和随笔/代码性能调试/checkcode.gif')
    21                                  #time_finish = time.time()
    22   73.441 MiB    0.000 MiB        return code

```

