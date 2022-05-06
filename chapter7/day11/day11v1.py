# 练习7-10 梦想的度假胜地
# 定义一个空列表，列表总再放字典

from multiprocessing.sharedctypes import Value


everyone_dream_Places = []
active = True
# 标志位默认为true，循环一直运行，除非用户输入no，然后系统将标志位换成false
# 或者程序内使用break，也可终止循环
while active:
    visitPlace = {}
    name_prompt = "What's your name?(If you want to quit,please input 'q')\n"
    visitPlace['name'] = input(name_prompt)
    if visitPlace['name'].lower() == 'q':
        break
    """     place_prompt = "If you could visit one place in the world, where would you go?"
    visitPlace['place'] = input(place_prompt)
    """
    visitPlace['place'] = input(
        "If you could visit one place in the world, where would you go?\n"
    )
    if visitPlace['place'].lower() == 'q':
        break
    else:
        everyone_dream_Places.append(visitPlace)
    # 问题不在input的形式

    # 前面的代码就避免了用户在前期就想退出的情况
    # 下来询问用户是否继续
    is_To_Continue = input(
        "Is there anyone else to say next?(Please enter [yes or no])\n"
    )
    if is_To_Continue.lower() == 'no':
        active = False

# 测试
everyone_dream_Places = [
    {'name': 'xf', 'place': 'hua shan'},
    {'name': 'xiao li', 'place': 'song shan'},
]

for everyone_dream_Place in everyone_dream_Places:
    # 主要问题是，对多键值对的字典的遍历理解有错误
    # for key, value in everyone_dream_Place.items():
    #     print(f"{key}想要去{value}")
    """  因为这里的字典不是单个的二元关系，而是多个二元关系，所以上面遍历的方法是错误的 """
    # print(f"{everyone_dream_Place['name']}想去{everyone_dream_Place['place']}")

    """ 那么，假如说，这里的二元关系的数量不是两个，而是多个的话，就该这样解决了： """
    for key, value in everyone_dream_Place.items():
        # 下面的运行结果：
        # print(f"\nKey: {key}")
        # print(f"Value: {value}")
        """
        Key: name
        Value: xf

        Key: place
        Value: hua shan

        Key: name
        Value: xiao li

        Key: place
        Value: song shan
         """
        # 所以我们要取的是值，key没有任何用处
        if key == 'name':
            name = value
        elif key == 'place':
            place = value
    print(name, "想去", place)

