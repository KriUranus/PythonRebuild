# T/I: Data Structure - List
# Date: 2023.6.2
# Author: @KriUranus


# 6.数据结构之列表
# 列表是由一系元素按特定顺序构成的数据序列，允许有重复数据。
items1 = [37, 88, 717, 612]
items2 = ['Diana', 'Eileen', 'Bella', 'Ava']
items3 = [24, 22, 18, 18]
# 也可通过list将其他序列变成列表，list是创建列表对象的构造器。
# 列表是可变数据类型，允许增删改元素。
items4 = list('A-SOUL')
print(items4)       # ['A', '-', 'S', 'O', 'U', 'L']
items4 = list(range(1, 10))
print(items4)

# 6.1 列表的运算符
# 列表的拼接
res1 = items1 + items3
print(res1)
# 列表的重复
res1 = ['A-SOUL'] * 4
print(res1)

# 列表的成员运算
print(26 in items3)         # False
print('Diana' in items2)    # True

# 获取列表长度（元素个数）
size = len(items2)
print(size)                 # 4

# 列表的索引
# list[-1]是list[len(list)-1]的简称，即倒数第一个元素，
# 同理-2是倒数第二个元素，以此类推。
print(items2[0], items2[-size])     # Diana Diana
items4[-1] = 100
print(items4[size-1], items4[-1])   # 4 100

# 列表的切片
# 现在item4 = [1, 2, 3, 4, 5, 6, 7, 8, 100]
print(items4[:5])           # [1, 2, 3, 4, 5]
print(items4[4:])           # [5, 6, 7, 8, 100]
print(items4[-5:-7:-1])     # [5, 4]
print(items4[::-2])         # [100, 7, 5, 3, 1]

# 列表的比较运算
items5 = [1, 2, 3, 4]
items6 = list(range(1, 5))
# 比较相等性比的是对应索引位置上的元素是否相等
print(items5 == items6)     # True
items7 = [3, 2, 1]
# 两个列表比较大小比的是对应索引位置上的元素的大小
print(items5 <= items7)     # True


# 6.2 遍历列表元素
# 方法一
for index in range(len(items1)):
    print(items1[index])
# 方法二
for items2 in items2:
    print(items2)


# 6.3 列表的方法
# 6.3.1 添加和删除元素
skill = ['C', 'Java', 'Python']
# 使用append方法在列表尾部添加元素
skill.append('SQL')
# 用insert方法在列表指定索引位置插入元素
skill.insert(3, 'Go')
# 删除指定元素
skill.remove('SQL')
# 删除指定索引位置的元素
skill.pop(0)
skill.pop(len(skill)-1)
print(skill)        # ['Java', 'Python']
# 清空列表元素
skill.clear()

# 6.3.2 元素的位置和次数


# 6.3.3 元素的排序和反转


# 6.4 列表的生成式

# 6.5 嵌套的列表


# Eg: 统计掷500次骰子每个点数出现的次数
import random
count = [0] * 6
for _ in range(500):
    point = random.randint(1, 6)
    count[point-1] += 1
for point in range(1, 7):
    print(f'{point}点出现了{count[point-1]}次。')







