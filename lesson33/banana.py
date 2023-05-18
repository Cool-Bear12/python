b1 = input().split(" ")
b = int(b1[0])
c = int(b1[1])
d = int(b1[2])
cena = 0
for i in range(1, d+1):
    cena += i * b
if c - cena >= 0:
    print(0)
else:
    print(cena - c)