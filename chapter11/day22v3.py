import unittest

from src.name_functionv2 import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """测试name_functionv2.py"""

    def test_first_last_name(self):
        """能够正确地处理像Janis Joplin这样的名字吗？在函数内要求三个参数的输入情况下"""
        formatted_name = get_formatted_name("janis", "joplin")
        self.assertEqual(formatted_name, "Janis Joplin")


if __name__ == "__main__":
    unittest.main()

# 现在就可以通过测试了
