# -*- codeing=utf-8 -*-
# @Time: 18:21
# @Author :liuwei
# @File:判断闰年.py
year=eval(input('请输入年份（-1停止）：'))
while year!=-1:
    if year < 1000 or year >= 10000:
        print('重新输入')
        year=eval(input('请输入年份（-1停止）：'))
        continue
    if year//4==0 and year//100!=o or year//400==0:
        print(year,'是闰年')
    else:
        print(year,'不是闰年')
    year = eval(input('请输入年份（-1停止）：'))
print('停止输入')