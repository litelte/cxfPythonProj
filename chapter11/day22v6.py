# 人口数量的测试
import unittest

# from src.city_functionsV1 import get_formatted_city
from src.city_functionsV2 import get_formatted_city


# 继承unittest的父类
class TestCityName(unittest.TestCase):
    """验证city_functions.py文件"""

    def test_city_country(self):
        formatted_city = get_formatted_city("santiago", "chile")
        self.assertEqual(formatted_city, "Santiago , Chile")


if __name__ == "__main__":
    unittest.main()

"""
运行day22v6.py，确认测试city_functionsV1的test_city_country() 未通过。
而city_functionsV2的test_city_country()通过
 """
