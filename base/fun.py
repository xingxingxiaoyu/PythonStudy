def sum(n):
    result = 0
    for i in range(n):
        result += i
    return result


print(sum(10))


def sortList(list, isDesc=False):
    for i in range(len(list)):
        for j in range(1,len(list)-i):
            flag=list[j] < list[j - 1]
            if(isDesc):
                flag=not flag
            if (flag):
                list[j], list[j - 1] = list[j - 1], list[j]
    return list

L=sortList([12,32,13,123,76,453,23,96])
print(L)
L=sortList([12,32,13,123,76,453,23,96],True)
print(L)



