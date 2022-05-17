import requests


def implementAPIandStore():
    """执行API调用并存储响应，需要注意的是，返回的类型还未转换为json，需要主动转换
    本函数无法提供转json，转完之后就没法传值了
    """
    url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
    header = {"Accept": "application/vnd.github.v3+json"}
    r = requests.get(url=url, headers=header)
    # response_dict = r.json()
    return r
