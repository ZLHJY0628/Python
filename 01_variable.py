#将消息赋给变量，并打印出来
message = "the first day of learining python"
print(message)
#将变量的值修改为一条新消息，在打印出来
message = "the second day of learining python"
print(message)
#用变量展示一个人的名字，并展示一条消息
first_name = "zhang"
last_name = "haoyang"
full_name = f"{first_name} {last_name}"
#名字首字母大写
message = f"Hello {full_name.title()}, would you like to learn some python today?"
print(message)
#去除左侧、右侧空格
full_name = " zhang haoyang "
print(full_name.lstrip(),f"\n\t{full_name.rstrip()}")
#去除文件名
file_name = "python.txt"
print(file_name.removesuffix(".txt"))
num=0.2+0.2
print(num)