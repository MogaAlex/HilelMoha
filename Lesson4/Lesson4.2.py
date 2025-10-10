a = [0, 1, 7, 2, 4, 8]
if len(a)==0:
    print(a)
else:
    x = a[-1]
    b = 0
    for i in range(0, len(a), 2):
        b = b + a[i]
    print(b * a[-1])

