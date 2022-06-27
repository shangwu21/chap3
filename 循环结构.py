# -*- codeing=utf-8 -*-
# @Time: 22:07
# @Author :liuwei
# @File:循环结构.py
for i in 'hello':
    print(i,end='')#end可以使print不换行
print()

#range（）函数，产生一个【n,m)的整数序列，含头不含尾
for i in range(1,11): #1到10
    print(i, end=' ')
print()

#累加操作
s=0
for i in range(1,11):
    s=s+i
print('1-10累加的和为：',s)

s=0
i=1
while i<=100:
    s=s+i
    i=i+1
print('1-100累加的和为：',s)

#嵌套循环
for i in range (1,4):
    for j in range(1,5):
        print('*',end='')
    #换行
    print()
print('-------直角三角形------------')
for i in range(1,6):
    for j in range(1,i+1):
        print('*',end='')
    print()
print('-------倒直角三角形------------')
for i in range(1,6):
    for j in range(1,7-i):
        print('*',end='')
    print()
print('-------等腰三角形------------')
for i in range(1,6):
    for j in range(1, 7-i):
        print(' ', end='')
    for k in range(1,2*i):
        print('*',end='')
    print()
print('-------菱形------------')
row=eval(input('输入菱形的行数：'))
#上半部分
top_row=(row+1)//2
for i in range(1,top_row+1):
    for j in range(1, top_row+2-i):
        print(' ', end='')
    for k in range(1,2*i):
        print('*',end='')
    print()
#下半部分
bot_row=row-top_row #4
for i in range(1,bot_row+1): #i的值1-4
    for j in range(1,i+2):
        print(' ',end='')
    for k in range(1,2*bot_row-2*i+2): #7 5 3 1 range尾数为 8 6 4 2
        print('*', end='')
    print()

#break和continue
