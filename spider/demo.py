# Author: Lila Morgen
# ProjectName: test
# FileName: demo.py
# Date: 2020/11/25
# Description:

from urllib.request import urlopen, urlretrieve, Request
from urllib.parse import quote
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


def search_baidu(wd='千锋'):
    url = 'https://www.baidu.com/s?wd=%s'
    request = Request(url % quote(wd),
                      headers={
                          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                       AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
                      })
    response = urlopen(request)
    assert response.code == 200
    print('请求成功')

    # 读取响应数据
    _bytes = response.read()
    with open('%s.html' % wd, 'wb') as file:
        file.write(_bytes)


def download_img(url):
    filename = url[url.rfind('/')+1:]
    request = Request(url,
                      headers={
                          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                           AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
                      })
    response = urlopen(request)
    with open(filename, 'wb') as file:
        file.write(response.read())


if __name__ == '__main__':
    download_img('https://cdn.pixabay.com/photo/2020/05/12/11/32/azalea-5162510__340.jpg')
