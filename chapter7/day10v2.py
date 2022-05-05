# 练习7-6
# 使用不同的方式再完成练习7-4，简单点也好，思想都是相通的
"""
在原来的练习7-4，使用了标志位，并且用标志的反转来终止循环，那么下来要做的是：
1.在循环中使用条件来结束循环
2.使用变量active来控制循环结束的时机（✅）
3.使用break语句在用户输入'quit'时退出循环
"""
# 循环中使用条件控制结束
prompt = "请输入披萨要加的料，输入quit结束加料"
isover = ''
while isover != 'quit':
    isover = input(prompt)
    # 不能让quit输出
    if isover.lower() == 'quit':
        continue
    else:
        print(f"您加了一份{isover}，还需要加其他的料吗？输入quit退出哦！😄")
