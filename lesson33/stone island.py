input()
a = input()
per = 0
uber = 0
while  per != len(a) - 1:
    if a[per] == a[per+1]:
        a = a[:per]+a[per+1:]
        uber+=1
    else:
        per+=1
print(uber)
