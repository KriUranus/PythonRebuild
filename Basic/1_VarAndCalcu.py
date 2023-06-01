# T/I: Basic Review of Python
# Date: 2023.6.1
# Author: @KriUranus


# 0.Classic Begining
print("Hello World!")


# 1.变量
msg = "Hello PyCharm!"
print(msg)
msg = "Hello Project!"
print(msg)

# 1.1 四则远算
a = 16
b = 80
print(a + b)
print(a - b)
print(a * b)
print(a / b)

# 1.2 变量类型检查
a = 2001
b = 2.26
c = 'Bingo!'
d = True
print(type(a))    # <class 'int'>
print(type(b))    # <class 'float'>
print(type(c))    # <class 'str'>
print(type(d))    # <class 'bool'>

# 1.3 变量类型转换
print(float(a))    # 整数转换为浮点数
print(str(b))      # 浮点型转成字符串 (输出字符串时不会看到引号)
print(bool(c))     # 字符串转成布尔型 (有内容的字符串都会变成True)
print(int(d))      # 布尔型转成整数 (True会转成1，False会转成0)
print(chr(97))     # 将整数变成对应的字符 (97对应字符表中的字母a)
print(ord('a'))    # 将字符转成整数 (Python中字符和字符串表示法相同)


# 2.运算符
# 2.1 算术运算符
print(100 + 2)     # 加法运算
print(100 - 2)     # 减法运算
print(100 * 2)     # 乘法运算
print(100 / 2)     # 除法运算
print(100 % 2)     # 求模运算
print(100 // 2)    # 整除运算
print(100 ** 2)    # 求幂运算

# 2.2 赋值运算符
x = 10
y = 3
x += y        # 即为x = x + y
x *= x + 2    # 即为x = x * (x + 2)
print(a)      # 2001

# 2.3 比较运算符与逻辑运算符
flag0 = 1 == 1
flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not (1 != 2)
print('flag0 =', flag0)    # flag0 = True
print('flag1 =', flag1)    # flag1 = True
print('flag2 =', flag2)    # flag2 = False
print('flag3 =', flag3)    # flag3 = False
print('flag4 =', flag4)    # flag4 = True
print('flag5 =', flag5)    # flag5 = False


# Eg: 判断用户输入的年份是否为闰年
year = int(input('请输入年份: '))
is_leap = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
print(is_leap)