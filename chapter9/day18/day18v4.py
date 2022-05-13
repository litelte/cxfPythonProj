# 调用上一个文件中的类文件，继承它的方法，生成一个自己序列
# 一致的时候，才表明中将
from day18v3 import Generate_lottery as gl


class My_ticket(gl):
    def __init__(self, numberCount, alphabetCount):
        # 初始化父类的属性
        super().__init__(numberCount, alphabetCount)

    def generate_my_ticket(self):
        """
        这个函数的作用就是生成自己的彩票序列，并判断自己的序列和大奖的序列多少次后可以一致
        """
        # 生成大奖序列
        # 彩票的序列位数默认为4个
        grand_prize = self.generate_list()
        print(f"大奖序列：{grand_prize}")
        # 中将标志位，没有中奖就继续买，直到中奖为止
        no_win = True
        # 用户购买的次数
        purchases = 0
        while no_win:
            # 生成用户的购买序列
            # 用户购买一次
            purchases += 1
            # 开始给奖
            current_list = self.generate_list()
            print(f"第{purchases}次购买，序列为：{current_list}")
            # 下来将用户的购买序列和大奖的序列进行对比，完全一样才算是中大奖
            # 使用循环对比
            conformCount = 0
            for i in grand_prize:
                for j in current_list:
                    if j == i:
                        conformCount += 1
                        break
                    else:
                        continue
            if conformCount == 4:
                no_win = False
        return purchases


# 实例化对象
my_ticket = My_ticket(10, 5)
my_ticket.generate_my_ticket()
"""
这样子写的容易出问题，分开来写
 """
