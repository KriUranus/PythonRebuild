# T/I: Basic Review of Python - Program Structure
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
# 4.1 for-in循环
# 1~100求和
sum1 = 0
for num1 in range(1, 101):
    sum1 += num1
print(num1)
# 1~100间的偶数求和
sum2 = 0
for num2 in range(2, 101, 2):
    sum2 += num2
print(sum2)

# 4.2 while循环
# 猜数字游戏
import random
ans = random.randint(1, 100)
count = 0
while True:
    count += 1
    guess = int(input("Enter your number:"))
    if guess < ans:
        print("Guess again, bigger.")
    elif guess > ans:
        print("Guess again, smaller.")
    else:
        print("Congrats! You get it.")
        break
print(f"You guessed for {count} times.")

# 4.3 嵌套的循环结构
# 输出乘法口诀表
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{i}*{j}={i * j}', end='\t')
    print()



# Eg1: 查找水仙花数
# Narcissistic number, 其每个位上数的3次幂和等于该数本身。
for NarNum in range(100, 1000):
    low = NarNum % 10
    mid = NarNum // 10 % 10
    high = NarNum // 100
    if NarNum == low ** 3 + mid ** 3 + high ** 3:
        print(NarNum)

# Eg2: 反转正整数
num3 = int(input('num = '))
reversed_num = 0
while num3 > 0:
    reversed_num = reversed_num * 10 + num3 % 10
    num3 //= 10
print(reversed_num)

# Eg3: 斐波那契数列
# 输出前20个数
var1, var2 = 0, 1
for _ in range(20):
    var1, var2 = var2, var1 + var2
    print(var1)

# Eg4: 查找100以内素数
for num4 in range(2, 100):
    # 假设num4为素数
    is_prime = True
    # 在2到num-1之间找num4的因子
    for factor in range(2, num4):
        # 若找到了num4的因子，num就不是素数
        if num4 % factor == 0:
            is_prime = False
            break
    # 如果布尔值为True则num4是素数
    if is_prime:
        print(num4)

# Eg5: CRAPS赌博游戏
# 规则：玩家第一次摇骰子如果摇出了7点或11点，玩家胜；
# 玩家第一次如果摇出2点、3点或12点，庄家胜；玩家如果摇出
# 其他点数则玩家继续摇骰子，如果玩家摇出了7点，庄家胜；
# 如果玩家摇出了第一次摇的点数，玩家胜；
# 其他点数玩家继续摇骰子，直到分出胜负。
# 前文已经import random
money = 1000
while money > 0:
    print(f'你的总资产为: {money}元')
    go_on = False
    # 下注金额必须大于0小于等于玩家总资产
    while True:
        debt = int(input('请下注: '))
        if 0 < debt <= money:
            break
    # 第一次摇色子
    # 用1到6均匀分布的随机数模拟摇色子得到的点数
    first = random.randint(1, 6) + random.randint(1, 6)
    print(f'\n玩家摇出了{first}点')
    if first == 7 or first == 11:
        print('玩家胜!\n')
        money += debt
    elif first == 2 or first == 3 or first == 12:
        print('庄家胜!\n')
        money -= debt
    else:
        go_on = True
    # 第一次摇色子没有分出胜负游戏继续
    while go_on:
        go_on = False
        current = randint(1, 6) + randint(1, 6)
        print(f'玩家摇出了{current}点')
        if current == 7:
            print('庄家胜!\n')
            money -= debt
        elif current == first:
            print('玩家胜!\n')
            money += debt
        else:
            go_on = True
print('你破产了, 游戏结束!')