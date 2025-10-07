a=[1,2,3,4,5]
if len(a)!=0:
    x = a.pop(-1)
    a.insert(0,x)
    print(a)
else:
    print(a)