a=[]
size = len(a)
z = int(size)//2
x = int(z)
if len(a)%2 == 0:
    b = [a[0:x]]+[a[x:int(size)]]
    print(b)
else:
    b = [a[0:x + 1]] + [a[x + 1:int(size)]]
    print(b)