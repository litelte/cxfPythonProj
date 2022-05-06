# 练习7-10 梦想的度假胜地
# 定义一个空列表，列表总再放字典
from operator import truediv


everyone_dream_Places = []

# 标志位默认为true，循环一直运行，除非用户输入no，然后系统将标志位换成false
# 或者程序内使用break，也可终止循环
while True:
    visitPlace = {}
    name_prompt = "What's your name?(If you want to quit,please input 'q')\n"
    visitPlace['name'] = input(name_prompt)
    if visitPlace['name'].lower() == 'q':
        break
    visitPlace['place'] = input(
        "If you could visit one place in the world, where would you go?\n"
    )
    if visitPlace['place'].lower() == 'q':
        break
    else:
        everyone_dream_Places.append(visitPlace)
    # 前面的代码就避免了用户在前期就想退出的情况
    # 下来询问用户是否继续
    is_To_Continue = input(
        "Is there anyone else to say next?(Please enter [yes or no])\n"
    )
    if is_To_Continue.lower == 'no':
        break

