import os.path
import re
import time

from urllib import parse

from judgeWeb.image_url import get_image_info, get_image_content, get_headers

def download_image(url):
    path = re.findall(r'telegra.ph/(.+)', parse.unquote(url))[0]
    info = get_image_info(url)

    if not os.path.exists(path):
        os.mkdir(path)

    for i in info:
        name = i['name']
        url = i['url']
        filename = path + '/' + name
        if not os.path.exists(filename):
            with open(filename, 'wb') as f:
                f.write(get_image_content(url))
            print(f'>>> 已完成：{filename}')
            time.sleep(1)
        else:
            print(f'>>> {filename} 已存在，跳过。')

if __name__ == '__main__':
    url = 'https://telegra.ph/NO001-%E6%98%AF%E4%B8%80%E5%8F%AA%E5%BA%9F%E5%96%B5%E4%BA%86-%E5%A5%B6%E7%89%9B-10-01-2'
    download_image(url)
    print('>>> 任务结束！')