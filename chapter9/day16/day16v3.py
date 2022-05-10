# 编写一个表示汽车的类
from operator import mod


class Car:
    """ 一次模拟汽车的简单尝试 """

    def __init__(self, make, model, year) -> None:
        """ 初始化描述汽车的属性 """
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """ 返回整洁的描述信息 """
        # 给返回值做了拼接，拼接字符中有空格，输出结果就有空格，这个需要注意
        long_name = f"{self.year} {self.make} {self.model}"
        # 返回首字母大写的返回值
        return long_name.title()


my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
