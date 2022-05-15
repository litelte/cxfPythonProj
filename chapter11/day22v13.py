# 练习11-3 雇员
import unittest

# from src.give_raise_function import give_raise


class Employee:
    def __init__(self, first_name, last_name, annual_salary) -> None:
        self.first = first_name
        self.last = last_name
        self.salary = annual_salary

    def give_raise(self, risevalue=5000):
        self.salary += risevalue


# 实例化一个对象
worker = Employee("xiao ming", "li", 2000)
print(worker.salary)
worker.give_raise()
print(worker.salary)
