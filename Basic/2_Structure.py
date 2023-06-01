# T/I: Basic Review of Python
# Date: 2023.6.1
# Author: @KriUranus


# 3.程序的分支结构
# Tip:
# Python中没有switch语句！
# 注意缩进！

# 3.1 简单的if语句
age = 21
if age >= 18:
    print("You are certificated to vote.")

# 3.2 if-else语句
age = 16
if age >= 18:
    print("You are certificated to vote.")
else:
    print("Sorry, you are too young to vote.")

# 3.3 if-elif-else结构
day = 5
if day < 3 or day > 6:
    print("今天没有播。")
elif 2 < day < 5:
    print("今天有单播哦！")
else:
    print("今天有团播哦！")

# 蟒蛇书还列出了以下两种语句结构：
# ①使用多个elif，最后为else语句
# ②省略else语句

# 3.3 嵌套的分支结构
x = float(input('x = '))
if x > 1:
    y = 3 * x - 5
else:
    if x >= -1:
        y = x + 2
    else:
        y = 5 * x + 3
print(f'f({x}) = {y}')


# 4.程序的循环结构
