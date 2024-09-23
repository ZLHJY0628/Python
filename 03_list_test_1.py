# 创建一个地名的列表，然后打印
location = ['Shanghai','Beijing','Guangzhou','Dalian']
print(location)
# 按照字母顺序排序，但是不修改列表数据
print(sorted(location))
# 验证顺序不变
print(location)
#反向排序，但是不修改列表数据
print(sorted(location,reverse=True))
#反转列表
location.reverse()
print(location)
#修改为正向排序
location.sort()
print(location[0:2])