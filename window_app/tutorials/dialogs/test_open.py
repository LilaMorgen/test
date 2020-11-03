# Version : python 3.7.4
# File : test_open.py
# Author : Lila Morgen
# Time : 2020/11/3 17:17
# description : 

with open('../../../images/eword.ico', 'rb') as f:
    content = f.read()
    print(content)
