# 接受两个形参，城市名和国家名
def get_formatted_city(city_name, country_name):
    full_city_name = f"{city_name}, {country_name}"
    return full_city_name.title()
