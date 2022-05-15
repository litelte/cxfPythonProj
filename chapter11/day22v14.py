# 编写一个测试用例
import unittest

import day22v13 as emp


class TestEmployeeRaiseSalary(unittest.TestCase):
    # 针对day22v13中的方法进行测试
    def setUp(self):
        # 创建实例化对象
        first_name = "xiao ming"
        last_name = "li"
        salary = 2000
        self.my_employee = emp.Employee(first_name, last_name, salary)

    def test_give_default_raise(self):
        # 比对涨薪前后，是否一样
        self.my_employee.give_raise()
        current_salary = self.my_employee.salary
        self.assertEqual(current_salary, 7000)

    def test_give_custom_raise(self):
        self.my_employee.give_raise(3000)
        current_salary = self.my_employee.salary
        self.assertEqual(current_salary, 5000)


if __name__ == "__main__":
    unittest.main()

"""
这里已经算是基本了解了测试类
还学到了：在子类中如何调用父类的函数 调用上层类的函数
就是self.实例名.函数()
这样子
 """
