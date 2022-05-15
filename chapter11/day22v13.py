# 练习11-3 雇员


class Employee:
    def __init__(self, first_name, last_name, salary="") -> None:
        self.first = first_name
        self.last = last_name
        self.salary = salary

    def give_raise(self, risevalue=5000):
        # 默认增加年薪5000美元
        self.salary += risevalue


# 实例化一个对象
# worker = Employee("xiao ming", "li", 2000)
# print(worker.salary)
# worker.give_raise()
# print(worker.salary)
# worker.give_raise(3000)
# print(worker.salary)

# 下来给Employee写一个测试用例
