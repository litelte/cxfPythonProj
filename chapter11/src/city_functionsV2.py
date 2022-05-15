# 把形参population变成可选的
def get_formatted_city(city_name, country_name, population=""):
    if population:
        formatted_city = (
            f"{city_name.title()} , {country_name.title()}- population {population}"
        )
    else:
        formatted_city = f"{city_name} , {country_name}"
    return formatted_city
