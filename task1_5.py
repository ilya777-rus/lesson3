#
# 1) Подсчет суммы всех четных чисел от 1 до n. Реализовать двумя видами циклов

n = 13
s=0
for i in range(1, n+1):
    if i%2==0:
        s+=i
s2=0
i=1
while i<=n:
    s2+=i
    i+=1


# 2) Найти самое длинное слово из массива. Реализовать двумя видами циклов
arr=['sddsd ', 'dsds s', 'dddddddddddd']
max=0
for x in arr:
    if len(x)>max:
        max=len(x)
        res = x
print(x)
i=0
max2=0
while i<len(arr):
    if len(arr[i])>max2:
        max=len(arr[i])
        res2=arr[i]
    i+=1
print(res2)
# 3) Расчет факториала числа с выводом каждого шага.
n = 5
f=1
for i in range(1,n+1):
    f*=i
    print(f)

# 4) Вывести каждый 3 элемент списка вместе с его индексом, используя enumerate()
print('---------------------------44444444444')
arr = [1,12,2,'3233',6,7,8]
count=2
for i,x in enumerate(arr):
    if i>=count and (i-count)%3==0:
        print(x,i)

# 5) Напечатать таблицу умножения для числа n, использовать f строки
n = 5
for i in range(1, 11):
    print(f"{n} * {i} = {n * i}")