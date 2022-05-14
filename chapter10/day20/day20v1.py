# 练习10-13 验证用户
"""
其实就是增加一个条件，让用户自己确认，用户如果觉得不对，那就让用户重新输入
综合前面的程序，就是说：一共分成三部分：
1.向用户打招呼
2.用户不在表单里，创建用户
3.确定用户的身份
 """
import json

# filename = "../src/usrname.json"
filename = "chapter10/src/usrname.json"


# 第一个函数，在json文件中创建新的用户，默认是输入的用户不在该文件中
def createNewUsrName():
    with open(filename, "w") as f:
        current_usr = input("请输入您的姓名：")
        print("正在为您注册，请稍等...")
        json.dump(current_usr, f)
        print("已注册完成，您目前为：登录状态！")


# 第二个函数，打印这个当前系统的用户，默认是该用户名已经在这个文件中
def already_exists_usr():
    with open(filename) as f:
        current_usr = json.load(f)
        return current_usr


def greetUsr():
    try:
        with open(filename) as f:
            json.load(f)
    except FileNotFoundError:
        createNewUsrName()
    else:
        stored_value = already_exists_usr()
        ans = input(f"您是{stored_value}用户吗？（输入y或者n）")
        if ans.lower() == "y":
            print(f"{stored_value}，欢迎您的再次登录！")
        else:
            createNewUsrName()


greetUsr()
