# 练习9-3
class User:
    def __init__(self, first_name, last_name) -> None:
        self.first = first_name
        self.last = last_name

    def describe_user(self):
        print(f"姓：{self.last}，名：{self.first}")
        print(f"中式叫法：{self.last+' '}{self.first}")

    def greet_user(self):
        fullName = self.last + ' ' + self.first
        print(f"你好{fullName.title()}，很高兴见到你！")


xiao_ming = User('xiao ming', 'li')
xiao_hua = User('xiao hua', 'zhang')

xiao_ming.describe_user()
xiao_ming.greet_user()

xiao_hua.describe_user()
xiao_hua.greet_user()
