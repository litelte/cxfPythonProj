# 使用break结束条件，那么这里就需要使用到标志位了
prompt = "您要给披萨中添加什么小料，请直接输入哦！如果输入quit就结束了哦！O(∩_∩)O"
while True:
    material = input(prompt)
    if material.lower() == 'quit':
        print("祝您用餐愉快！")
        break
    else:
        print(f"您加的小料为：{material}，还要其他的什么吗？退出的话，输入quit哦！")
