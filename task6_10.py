
# 6) Подсчитать количество цифр в числе. Реализовать двумя видами циклов
n = 0
k=2332
for i in str(n):
    k+=1
print(k)

k2=0
n2=32
while n2>=0:
    k2+=1
    n2=n2//10
    if n2==0:
        break
print(k2)

# 7) Проверить, является ли строка палиндромом (зеркальная)
str='на доме чемодан'
str1='город дорог'
def palin(str):
    start = ''.join(str.split())
    r=''
    for x in str[::-1]:
        if x !=' ':
            r+=x
    return r==start

print(palin(str1))

# 8) Определить, содержит ли список дубликаты
arr = [1,2,3,4,6,3,3,7]
def dubl(arr):
    arr_un=[]
    for x in arr:
        if x in arr_un:
            return 'Есть дубликат'
        else:
            arr_un.append(x)
    return 'Дубликатов нет'
print(dubl(arr))
# 9) Удалить все дубликаты из списка без использования дополнительных структур. Реализовать двумя видами циклов, для удаления можно использовать pop() либо del
arr1 = [1,2,3,4,6,3,3,7]
arr2 = [1,2,3,4,6,3,3,7]
def dub(arr):

    for i in range(len(arr)):
        j=i+1
        while j<len(arr):
            if arr[i]==arr[j]:
                arr.pop(j)
            else:
                j+=1
    return arr

def dub2(arr):
    i=0
    arr_un = []
    while i<len(arr):
        if arr[i] in arr_un:
            arr.pop(i)
            # i-=1
        else:
            arr_un.append(arr[i])
            i+=1

    return arr

print(dub(arr1))
print(dub2(arr2))
# 10) Вывести каждую букву строки в обратном порядке без использования reversed() или [::-1]
str='abcdefffrre'
for i in range(len(str)-1,-1,-1):
    print(str[i], end='')



