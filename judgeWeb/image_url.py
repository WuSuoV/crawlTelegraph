import random
import re

import requests

a_requests = requests.session()
a_requests.keep_alive = False


user_agent = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
    ]

def get_headers():
    return {
        "User-Agent": random.choice(user_agent),
        "Referer": 'https://telegra.ph/'
    }

def get_html_text(url):
    headers = {
        "User-Agent": random.choice(user_agent),
        "Referer": 'https://telegra.ph/'
    }

    return a_requests.get(url=url, headers=headers).text

def get_image_src(html_text):
    return re.findall(r'img src="(\S+)"', html_text)

def get_image_url_name(img_info):
    info = []
    for i in img_info:
        name = i.replace('/file/', '')
        url = 'https://telegra.ph' + i
        info.append({"name":name, "url":url})
    return info

def get_image_content(url):
    headers = {
        "User-Agent": random.choice(user_agent),
        "Referer": 'https://telegra.ph/'
    }
    return a_requests.get(url=url, headers=headers).content

def get_image_info(url):
    return get_image_url_name(get_image_src(get_html_text(url)))



# if __name__ == '__main__':
#     url = "https://telegra.ph/NO001-%E6%98%AF%E4%B8%80%E5%8F%AA%E5%BA%9F%E5%96%B5%E4%BA%86-%E5%A5%B6%E7%89%9B-10-01-2"
#     print(get_image_info(url))
