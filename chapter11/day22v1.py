import unittest

from src.name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    # 测试name_function.py
    def test_first_last_name(self):
        """能够正确地处理Janis Joplin"""
        formatted_name = get_formatted_name("janis", "joplin")
        self.assertEqual(formatted_name, "Janis Joplin")


if __name__ == "__main__":
    unittest.main()
