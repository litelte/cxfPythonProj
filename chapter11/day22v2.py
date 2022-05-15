# 三个实参版的测试
import unittest

from src.name_functionv1 import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """测试name_functionv1.py"""

    def test_first_middle_last_name(self):
        """能够正确地处理像Janis Ming Joplin这样的姓名吗"""
        # formatted_name = get_formatted_name("janis", "ming", "joplin")
        formatted_name = get_formatted_name("janis", "joplin")
        self.assertEqual(formatted_name, "Janis Ming Joplin")


if __name__ == "__main__":
    unittest.main()
"""
这个情况下，在没有补全函数内要求的字符串，就没法通过测试
那么该如何解决？见下次版本
 """
