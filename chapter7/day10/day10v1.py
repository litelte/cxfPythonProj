index = 1
active = True
while active:
    prompt = f"欢迎来到电影院，您是第{index}位观众，电影院根据观众的年龄推出了不同价位的票，"
    prompt += "您先说下您的年龄吧，我这里帮您查一下🤭，输入quit就可以退出查询了\n"
    age = input(prompt)
    if age.lower() == 'quit':
        print("欢迎您下次光临！")
        break
    else:
        age = int(age)
        if age < 3:
            price = 0
        elif age < 12:
            price = 10
        else:
            price = 12
        print(f"您好，帮您查询了，根据您输入的年龄，最后您需要支付{price}$，祝您观影愉快")
        index += 1
        continue
