# 在TestAnonymousSurvey中再添加一个方法
import unittest

from src.survey import AnonymousSurvey


# 类的命名方法是：Test+函数名
class TestAnonymousSurvey(unittest.TestCase):
    """针对AnonymousSurvey类的测试"""

    # 函数的命名方法：test_store_xxx_response
    def test_store_single_response(self):
        # 提出调查的问题
        question = "What language did you first learn to speak?"
        # 把调查问题传入函数
        my_survey = AnonymousSurvey(question)
        # 把答案存放到函数的答案库中
        my_survey.store_response("English")
        # 答案和答案库比对
        self.assertIn("English", my_survey.responses)

    def test_store_three_responses(self):
        """测试三个答案会被妥善地存储"""
        # 提出问题
        question = "What language did you first learn to speak?"
        # 把问题传入函数的问题参数中
        my_survey = AnonymousSurvey(question)
        # 把回答传入函数的答案库中
        my_responses = ["English", "Spanish", "Mandarin"]
        for response in my_responses:
            my_survey.store_response(response)
        # 答案和答案库进行对比
        for response in my_responses:
            self.assertIn(response, my_survey.responses)


if __name__ == "__main__":
    unittest.main()

# 有些测试有些重复，下面使用unittest的另一项功能来提高效率
