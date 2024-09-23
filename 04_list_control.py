# 列表内存储三种 pizza，用 for 循环打印每种披萨的数据,并在结尾输出一个总结性发言
pizzas = ['pizza a','pizza b','pizza c']
for pizza in pizzas:
    print(f"I like {pizza} pizza")
print('I really like pizza!')
# 使用一个 for 循环打印数字 1-20
for num in range(1,21):
    print(num)
# 创建一个列表，并求和
number = list(range(1,1000001))
print(sum(number))
# 创建一个 20 以内奇数的列表
singles = list(range(1,20,2))
for single in singles:
    print(single)
# 创建一个列表，存储前十个整数的立方，并打印
cubes = []
for num in range(1,11):
    cubes.append(num**3)
for cube in cubes:
    print(cube)
# 是用列表推导式实现
cubes = [cube**3 for cube in range(1,11)]
print(cubes)
#复制披萨列表，赋给 friend_pizzas
friend_pizzas = pizzas[:]
friend_pizzas.append('pizza d')
for pizza in pizzas:
    print(f"My favorite pizzas are {pizza}")
for friend_pizza in friend_pizzas:
    print(f"My friend's favorite pizzas are {friend_pizza}")