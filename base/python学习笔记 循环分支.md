## if
条件判断
#### 简单判断
```
a=11
if a>10:
    print("big")
```
#### 带else分支
```
a=10
if a>10:
    print("big")
else:
    print("little")
```
#### 多分支if
```
if a>10:
    print("big")
elif a>5:
    print("middle")
else:
    print("little")
```

## for
```
result = 0
for i in range(101):
    result += i
print(result)
```
break和continue和常规的一样，多了一个else字段：
```
for i in range(100):
    if i % 5 == 0:
        print("i的值是", i, "能被5整除")
        continue
    print("i的值是", i, "不能被5整除")
else:
    print("最终的i：", i)
```
```
i的值是 94 不能被5整除
i的值是 95 能被5整除
i的值是 96 不能被5整除
i的值是 97 不能被5整除
i的值是 98 不能被5整除
i的值是 99 不能被5整除
最终的i： 99
```

## while
```
i=10
while(i>0):
    print(i)
    i-=1
else:
    print("最后的i:",i)
```
```
10
9
8
7
6
5
4
3
2
1
最后的i: 0
```

## 应用
python求0-999的水仙花数：
```
for i in range(10, 1000):
    # 个位
    a = i % 10
    # 十位
    b = i % 100 // 10
    # 百位
    c = i // 100
    if a * a * a + b * b * b + c * c * c == i:
        print(i)
        
153
370
371
407
```