# 测试AnonymousSurvey类
import unittest

from src.survey import AnonymousSurvey


# 继承测试类
class TestAnonymousSurvey(unittest.TestCase):
    """针对AnonymousSurvey类的测试"""

    def test_store_single_response(self):
        """测试单个答案会被妥善地存储"""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        """
        需要创建其实例。使用问题"What language did you first learn to speak?" 创建一个名 为my_survey 的实例，然后使用方法store_response() 存储单 个答案English 。接下来，检查English 是否包含在列 表my_survey.responses 中，以核实这个答案是否被妥善地存储了。
         """
        my_survey.store_response("English")
        self.assertIn("English", my_survey.responses)


if __name__ == "__main__":
    unittest.main()
"""
当我们运行test_survey.py时，测试通过了：
 """
"""
这很好，但只能收集一个答案的调查用途不大。下面来核实当用户 ᨀ 供三个答案时，它们也将被妥善地存储。
 """
