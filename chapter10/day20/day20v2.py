# 另一种方式
import json

# python的文件路径还是有点问题的
# 相对路径还是不能用../ 这种的来表示
# 这次的改动，相较于上次来说，少做一次打开文件的操作
# 虽然也是只用一次try except

filename = "chapter10/src/usrname.json"


def already_exists_usr():
    try:
        with open(filename) as f:
            current_usr = json.load(f)
    except FileNotFoundError:
        return None
    else:
        # 返回值current_usr还是None
        return current_usr


def createNewUsrName():
    with open(filename, "w") as f:
        current_usr = input("请输入您的姓名：")
        print("正在登录，请稍等：")
        # 这里注意，json.dump()里面填的不是文件名，而是文件对象
        # 操作的是对象
        json.dump(current_usr, f)
        print("登录成功，请您继续使用！")


def greetUsr():
    # 有返回值的函数，别直接调用，先赋值变量，再使用变量
    # 不然不好把握
    current_usr = already_exists_usr()
    if current_usr:
        # 询问当前的用户是否为系统目前在线的用户
        ans = input(f"您是用户{current_usr}吗？请您仔细核对姓名后，确认登录！(y or n?)")
        if ans.lower() == "n":
            createNewUsrName()
        else:
            print(f"{current_usr}欢迎您的再次登录！")
    else:
        createNewUsrName()


greetUsr()
