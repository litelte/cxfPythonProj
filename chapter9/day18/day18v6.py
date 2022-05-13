# 一个检测的测试
grand_prize = [9, "b", "b", "a"]
current_list = [9, 7, "b", "a"]
conformCount = 0
for i in grand_prize:
    for j in current_list:
        if j == i:
            conformCount += 1
            break
if conformCount == 4:
    print("一样")
