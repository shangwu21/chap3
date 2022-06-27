# -*- codeing=utf-8 -*-
# @Time: 18:04
# @Author :liuwei
# @File:break和continue.py
#break
'''
i=eval(input('求1-n的累加和，请输入n的值：'))
s=0
while i<=100:
    if s>100:
        print('s值已超过100，累加停止')
        break #break会跳过while循环，包括else
    s=s+i
    i=i+1
else:
    print('s的值为：',s)

print('s的值为：',s)
'''
#continue
i=1
s=0
while i<=100:
    if i%2==1:
        i=i+1
        continue #如果满足，直接回到开头while，不执行s=s+i,i=i+1
    s=s+i
    i=i+1
print('1-100之间的偶数和为：',s)

i=1
s=0
for i in range(101): #i=1-100
    if i % 2 == 1:
        i = i + 1
        continue  # 如果满足，直接回到开头while，不执行s=s+i,i=i+1
    s = s + i
    i = i + 1
print('1-100之间的偶数和为：', s)