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

endValue=0
for i in range(10000):
    if i > 100:
        endValue=i
        break
    if i % 5 == 0:
        print("i的值是", i, "能被5整除")
        continue
    print("i的值是", i, "不能被5整除")
else:
    print("最终的i：", endValue)
