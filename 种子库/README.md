# 这个爬虫是用来干好事的

爬取的网站是一个~~[种子库](http://www.sugarfh.vip)~~[种子库](http://www.sugarnb.vip)，里面有成千上万的种子。
<br />
![人不好色好什么？how are you 吗](人不好色好什么.jpeg)
------
这是第一次写多线程爬虫，对锁的运用还是存在问题。

## Python3多线程——threading库
调用threading库中Thread类可建立一个线程
```python
import threading

threading.Thread(target = FuncName, [*args, **kwargs], name = ThreadName)
```
建立线程后调用start()方法运行线程，调用join()方法设置线程结束位置
```python
import time
import threading

th = threading.Thread()

th.start()
time.sleep(3)
th.join()
```
调用start()方法实质上是调用了线程对象的run()方法，由此可知有两种常用的调用线程的方法
1. 直接将函数作为参数传入Thread对象
2. 继承Thread类，重写run方法，再调用start方法
```python
import time
import threading

# 方法一
def sayHello(objectName):
  print('Hello',objectName)
  
threading.Thread(target = sayHello, ('World',)).start()

#方法二
class MyThread(threading.Thread):
  def __init__(self, objName):
    super().__init__()
    self.objName = objName
    
  def run(self):
    print('Hello', self.objName)

myth = Mythread('World')
myth.start()

```
