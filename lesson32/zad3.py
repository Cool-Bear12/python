# x = int(input())
# y = 0
# for i in range(x):
#     a = input()
#     n = a.split(" ")
#     n1 =int(n[0])
#     n2 = int(n[1])
#     n3 = int(n[2])
#     if n1 + n2 + n3 > 1:
#          y += 1
#print(y)
y = int(input())
u = 0
for i in range(y):
    a = input()
    if a.count("1") >= 2:
        u += 1
print(u)

