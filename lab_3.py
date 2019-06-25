def function (list1, list2):
    newlist=[]

    for i in list1:
        k = 0
        for j in list2:
            if (i==j):
                k=k+1
        if (k==0):
            newlist.append(i)
    return newlist
n=int(input("Введите число элементов для списка_1  : "))
print("Введите элементы списка_1  : ")
list1=[]
for i in range(n):
    list1.append(input())

n=int(input("Введите число элементов для списка_2  : "))
print("Введите элементы списка_2  : ")
list2=[]
for i in range(n):
    list2.append(input())
result=function(list1,list2)
print(list1)
print(list2)

print("Вывод : ")
print(result)
