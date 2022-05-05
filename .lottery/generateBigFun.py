# 生成大乐透彩票号码
"""
大乐透的规则是：
1.共有两个号码段：红区和蓝区
2.红区是5个数，蓝区两个数
3.两个区之中，单个数字是一个不超过100，且最小为1的数字
 """
import time
from random import randint

# 不直接使用random.random，这种随机性稍差一些
# 使用线性同余法
"""
https://blog.csdn.net/qq_39022311/article/details/83477469
线性同余法的公式： rNew=(a*rOld+b) % (end-start)
 其中：	rNew为新种子，a成为乘数，b称为增量，（end-start）称为模数，他们均为常数，然后设置rOld = rNew ，一般要求用户指定种子数rOld(也叫seed)，当然也可以自由选择a和b，但是这两个数字选的不好的话，会影响数字的随机性。
       经过数学家的计算，a,b 最好的值是： a=32310901  ,b=1729
 """


def myrandint(start, end, seed=999999999):
    a = 32310901
    b = 1729
    rOld = seed  # 将种子seed赋值给rOld
    m = end - start  # 得到m 模数
    while True:
        # 开始产生随机数
        rNew = int((a * rOld + b) % m)
        # 遇到yield关键字暂时挂起后面的代码，等带next(r)的调用并返回 rNew
        yield rNew
        rOld = rNew


# 模拟使用10个不同得时间种子来生成随机数
"""
获得时间戳，由于计算机运行较快，可能计算机在同一个时间内循环了多次，这会导致时间种子相同的问题。所以保险起见，我用一个随机函数产生的随机数与其相加，更好避免出现重复种子的现象
 """
# 开始生成红区的号码：
# 将生成的红区号码存到一个字典中
for i in range(10):
    now = time.time() + randint(0, 99999)  # 时间戳加一个随机数作为种子
    print(now)
    r = myrandint(1, 100, now)  # 把时间种子作为参数调用myrandint函数
    # 每个种子生成10个随机数
    print("种子", now, "生成的随机数:")
    # 每个种子生成一个对应的红区
    for j in range(10):
        # 使用next()函数循环遍历r生成器对象来得到五个随机数
        print(next(r), end=",")
    print()
