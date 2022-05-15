# get_formatted_name()的新版本，它要求通过一个实参指定中间名
def get_formatted_name(first, middle, last):
    """生成整洁的姓名"""
    full_name = f"{first} {middle} {last}"
    return full_name.title()


# 下面的测试重新进行，会发现无法通过测试
