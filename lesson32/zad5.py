x = 0
a = int(input())
for i in range(a):
    s = input()
    if s =="X++" or s=="++X":
        x += 1
    elif s == "X--" or s =="--X":
        x-=1
print(x)