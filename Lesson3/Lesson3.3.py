a=[1,2,3]
size = len(a)
z = size//2
x = z
if len(a)%2 == 0:
    b = [a[0:x]]+[a[x:size]]
    print(b)
else:
    b = [a[0:x + 1]] + [a[x + 1:size]]
    print(b)