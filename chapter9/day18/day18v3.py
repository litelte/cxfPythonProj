# 彩票分析：
from random import choice, randint


class Generate_lottery:
    def __init__(self, numberCount, alphabetCount):
        """
        奖号要求：
        numberCount为奖项中数字的数量
        alphabetCount为奖项中字母的数量
        这些都可以自己调整的
        """
        self.numberCount = numberCount
        self.alphabetCount = alphabetCount

    # 生成一个中奖的票号
    def generate_list(self, choiceCount=4):
        self.alphabetCount = 5
        self.numberCount = 10
        # 生成数字序列
        self.numberCount += 1
        numbers = list(range(1, self.numberCount))
        # 生成字母序列
        current_alphabets = [chr(i) for i in range(97, 130)]
        alphabets = []
        # 进行第二轮循环的时候，alphabetCount得初始化一下
        for alpha in current_alphabets:
            if self.alphabetCount:
                alphabets.append(alpha)
                self.alphabetCount -= 1
            else:
                break

        # 确定奖项的细则
        """
        从上面两个列表中选择的数字或者字母的数量：choiceCount
        默认是4个，如有需要可以自行修改，注意这是一个实参，修改的话，需要加=
         """
        # 选择的数字位数
        chooseNumber = randint(1, choiceCount)
        # 选择的字母位数
        choosealph = choiceCount - chooseNumber
        # print(f"选择数字的位数为：{chooseNumber}次,字母的位数为：{choosealph}次")

        # 开始选数字和字母，所选的字母和数字均不能重复
        numbers_choice = []
        while chooseNumber:
            current_number = choice(numbers)
            numbers_choice.append(current_number)
            numbers.remove(current_number)
            chooseNumber -= 1
        while choosealph:
            current_alpha = choice(alphabets)
            numbers_choice.append(current_alpha)
            alphabets.remove(current_alpha)
            choosealph -= 1
        # 遍历随机选择的四个号码：
        # print("大奖的号码是：")
        """ for value in grand_prize_choice:
            print(value, end="\t") """
        # 返回大奖序列
        return numbers_choice


"""     def show_grand_prize_list(self):
    # 这样子是调用类中的其他函数,就是再运行一下生成的函数
    # self.generate_list()
    # 但是我们的目的不是再调用一下生成的函数，而是把拿到上次函数运行的返回值
    # 还是搞不懂，先暂时不整了，以后会了再传值
 """

# 实例化验证
# generate_grand_prize = Generate_lottery(10, 4)
# grand_prize = generate_grand_prize.generate_list()
# print(grand_prize)
