days=['Пн ','Вт ',"Ср ","Чт ","Пт ","Сб ","Вс "]
n=31
print(*days)
for i in range(1,n+1):
    if i<10:
        print(i, end='   ')
    else:
        print(i, end='  ')
    if i%7==0:
        print()