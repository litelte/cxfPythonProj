"""
使用继承的方法重写上面的那个例子
 """
from day18v3 import Generate_lottery as gl


# 直接写类，太麻烦了，不如写个函数
def compareResult():
    lottery = gl(10, 5)
    # 大奖的序列
    grand_prize = lottery.generate_list()
    print(f"大奖序列：{grand_prize}")
    # 中奖标志位，灭有中奖就继续买，直到中奖为止
    no_win = True
    # 用户的购买次数
    purchases = 0
    while no_win:
        # 用户购买一次，生成一次用户的购买序列
        purchases += 1
        # 开始给抽号，号码初始化
        current_user_list = lottery.generate_list()
        print(f"第{purchases}次购买，序列为：{current_user_list}")
        # 下来将用户的购买序列和大奖的序列号进行对比，完全一样才是一等奖
        # 循环对比
        conformCount = 0
        for i in grand_prize:
            for j in current_user_list:
                if j == i:
                    # 有一个和大奖中的序列相同，记录相同次数加一，然后删掉这个用户序列中的一个元素
                    # 继续让用户序列中的其他元素和大奖中的其他序列对比，避免了次序不相同，但是位数和值是相同的情况
                    conformCount += 1
                    current_user_list.remove(j)
        if conformCount == 4:
            no_win = False
            print(f"买了{purchases}次彩票，终于获得了一等奖。")


# 实例化对象，开始进行
compareResult()
