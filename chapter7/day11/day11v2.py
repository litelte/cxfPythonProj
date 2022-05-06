# 上一个版本，我们使用了非主流的方式，可以说是小事整成了大事，确实有点得不偿失
# 然鹅我却深层次理解了字典
# 下来就是一种简单的做法了，利用本题的条件：单二元关系，即：name:place
everyone_dream_places = {}
# 只有单二元关系，非常简单的字典了
active = True
# while循环的标志位，先给个无限循环，直到用户想主动退出
while active:
    name = input("你叫啥名字？(不想输入的话，按q键退出哦！\n")
    if name.lower() == 'q':
        break
    response = input("如果有一天，我可以满足你去一个地方，你愿意去哪里？\n")
    if response.lower() == 'q':
        break
    else:
        everyone_dream_places[name] = response
    # 接下来询问用户是否继续输入：
    is_to_continue = input("你要继续输入其他人的信息吗？输入任意字符继续，输入q退出！\n")
    if is_to_continue.lower() == 'q':
        active = False

# 下来遍历字典中的数据，规范化输出
for name, place in everyone_dream_places.items():
    print(name, "想去看", place)
