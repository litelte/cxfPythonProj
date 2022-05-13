from time import time

from day18v3 import Generate_lottery as gl

lottery = gl(10, 5)
# 大奖的序列
grand_prize = lottery.generate_list()
print(f"大奖序列：{grand_prize}")
# 中将标志位，没有中奖就继续买，直到中奖为止
no_win = True
# 用户购买的次数
purchases = 0
while no_win:
    # 生成用户的购买序列
    # 用户购买一次
    purchases += 1
    # 开始给抽号，号码初始化
    current_list = []
    current_list = lottery.generate_list()
    print(f"第{purchases}次购买，序列为：{current_list}")
    # 下来将用户的购买序列和大奖的序列进行对比，完全一样才算是中大奖
    # 使用循环对比
    conformCount = 0
    for i in grand_prize:
        for j in current_list:
            if j == i:
                conformCount += 1
                current_list.remove(j)
                break
    if conformCount == 4:
        no_win = False
# time(20)
print(f"买了{purchases}次彩票，终于获得一等奖。")
