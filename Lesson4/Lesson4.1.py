a = []
i = 0
for i in range(0,len(a)):
    if a[i]==0:
        a.remove(0)
        a.append(0)
print(a)