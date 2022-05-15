"""
下面使用setUp() 来创建一个调查对象和一组答案，供方法 test_store_single_response() 和 test_store_three_responses() 使用
 """
import unittest

from src.survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """针对AnonymousSurvey类的测试"""

    def setUp(self) -> None:
        """
        创建一个调查对象和一组答案，供使用的测试方法使用
        """
        my_question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(my_question)
        self.responses = ["English", "Spanish", "Mandarin"]

    def test_store_single_response(self):
        """测试单个答案会被妥善地存储"""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """测试三个答案会被妥善地存储"""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


if __name__ == "__main__":
    unittest.main()

"""
测试自己编写的类时，方法setUp() 让测试方法编写起来更容易： 可在setUp() 方法中创建一系列实例并设置其属性，再在测试方法 中直接使用这些实例。相比于在每个测试方法中都创建实例并设置 其属性，这要容易得多。
 """
