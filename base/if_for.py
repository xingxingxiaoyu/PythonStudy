a = 10
if a > 10:
    print("big")
else:
    print("little")

if a > 10:
    print("big")
elif a > 5:
    print("middle")
else:
    print("little")

result = 0
for i in range(101):
    result += i
print(result)

for i in range(100):
    if i % 5 == 0:
        print("i的值是", i, "能被5整除")
        continue
    print("i的值是", i, "不能被5整除")
else:
    print("最终的i：", i)

i = 10
while (i > 0):
    print(i)
    i -= 1
else:
    print("最后的i:", i)

for i in range(10, 1000):
    # 个位
    a = i % 10
    # 十位
    b = i % 100 // 10
    # 百位
    c = i // 100
    if a * a * a + b * b * b + c * c * c == i:
        print(i)
