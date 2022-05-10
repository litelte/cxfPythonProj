class Car:
    # 给属性指定默认值
    def __init__(self, make, model, year) -> None:
        """ 初始化描述汽车的属性 """
        self.make = make
        self.model = model
        self.year = year
        # 设置默认值
        self.odometer_reading = 0

    def get_descriptive(self):
        """ 返回整洁的描述信息 """
        # 给返回值做了拼接，拼接字符中有空格，输出结果就有空格，这个需要注意
        long_name = f"{self.year} {self.make} {self.model}"
        # 返回首字母大写的返回值
        return long_name.title()

    def read_odometer(self):
        """ 打印一条指出汽车里程的消息 """
        # self已经绑定了odometer
        print(f"This car has {self.odometer_reading} miles on it.")


my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive())
my_new_car.read_odometer()
