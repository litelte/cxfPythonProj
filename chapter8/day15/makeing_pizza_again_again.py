# 还有新的方式，使用as
from pizza import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green', 'extra cheese')
"""
还有使用as给函数指定别名
from pizza import make_pizza as mp
使用as给模块指定别名
import pizza as p
这就不一一列举了，形式都相同，其实就是方便使用，不容易混淆
导入模块中的所有函数
from pizza import *
 """