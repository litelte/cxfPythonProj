# 练习9-1
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type) -> None:
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"欢迎光临，这里是{self.restaurant_name}")
        print(f"我们店的特点是{self.cuisine_type}")

    def open_restaurant(self):
        print(f"我宣布，这里是{self.restaurant_name}广场，大家尽管消费！野性消费！")


# 创建实例
my_restaurant = Restaurant('醉西安', '西北重口味油泼辣子')
# 打印属性
myresName = my_restaurant.restaurant_name
myrestype = my_restaurant.cuisine_type
print(myresName)
print(myrestype)
# 调用方法
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

print("---------------分割线---------------------")

# 创建三个实例
firstRes = Restaurant('醉洛阳', '特色古都洛阳菜')
secndRes = Restaurant('醉榆林', '特色陕北羊肉菜')
thirdRes = Restaurant('醉成都', '特色鲜香爆辣重油菜')

# 并对每个实例调用describe_restaurant()
firstRes.describe_restaurant()
secndRes.describe_restaurant()
thirdRes.describe_restaurant()
