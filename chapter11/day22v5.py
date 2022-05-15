# 练习11-1
import unittest

from src.city_functions import get_formatted_city


# 继承了python库中的测试类
class TestCityName(unittest.TestCase):
    """
    测试city_functions.py
    """

    def test_city_country(self):
        # 执行函数得到的值和目标设定值对比，从而验证该函数有没有达到预期的效果
        formatted_city = get_formatted_city("santiago", "chile")
        self.assertEqual(formatted_city, "Santiago, Chile")


if __name__ == "__main__":
    unittest.main()
