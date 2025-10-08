a=[1]
size = len(a)
z = size//2
if len(a)%2 == 0:
    b = [a[0:z]]+[a[z:size]]
    print(b)
else:
    b = [a[0:z + 1]] + [a[z + 1:size]]
    print(b)