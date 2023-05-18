a = input().split(" ")
n1 = int(a[0])
n2 = int(a[1])
b = 0
while n1 <= n2:
    n1 *= 3
    n2 *= 2
    b += 1
print(b)