# 添加新测试
import unittest

from src.name_functionv2 import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """测试name_functionv2.py"""

    def test_first_last_name(self):
        # 输入的值
        formatted_name = get_formatted_name("janis", "joplin")
        # 期望得到的结果：
        self.assertEqual(formatted_name, "Janis Joplin")

    def test_first_last_middle_name(self):
        """能够正确地处理像Wolfgang Amadeus Mozart这样的姓名吗？"""
        formatted_name = get_formatted_name("wolfgang", "mozart", "amadeus")
        self.assertEqual(formatted_name, "Wolfgang Amadeus Mozart")


if __name__ == "__main__":
    unittest.main()
