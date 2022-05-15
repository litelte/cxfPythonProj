# 编写一个test_city_country_population()的测试，确认能通过测试
import unittest

from src.city_functionsV2 import get_formatted_city


class TestCityName(unittest.TestCase):
    def test_city_country_population(self):
        formatted_city = get_formatted_city("santiago", "chile", population=5000000)
        self.assertEqual(formatted_city, "Santiago , Chile- population 5000000")


if __name__ == "__main__":
    unittest.main()
