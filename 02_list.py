# bicycle = ['trek','cannondale','redline','specialized']
# #第一个元素的索引是 0
# print(bicycle[0].upper())
# #最后一个元素的索引是-1
# print(bicycle[-1].title())
# #使用 f 字符串拼接元素
# print(f"I want to buy a bike of {bicycle[1].upper()}")

# 将一些朋友的名字储存在列表中
names = ['Tim','Alice','Tom','Eddi']
# 在列表队尾插入一个元素
names.append('John')
# 在列表第 2 个位置插入一个元素
names.insert(1,'Jessica')
# 弹出姓名列表的最后一个元素,并打印
poped = names.pop()
#修改第 2 位的元素为 Wang
names[1] = 'Wang'
print(names)
#反转列表
# 方法 1
names.reverse()
print(names)
# 方法 2
print (names[::-1])
# 向这些人发出邀请
for name in names:
    mes = f"{name}, Would you like to attend the meeting?"
    print(mes)
#仅保留前两个人，再次邀请；删除其余人，并通知他们。
len = len(names)
for j in range(2,len):
    poped = names.pop()
    print(f"{poped},sorry")
for j in range (0,1):
    print(f"Welcome,{names[j]}")