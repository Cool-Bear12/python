from random import randint

a = int(input("Сколько бросков кинуть?: "))
d = {}
for i in range(a, 6*a+1):
    d[i]=0
for l in range(1_000_000):
    total = 0
    for _ in range(a):
        brosok =randint(1,6)
        total+-brosok
    d[total] +=1
print(d)