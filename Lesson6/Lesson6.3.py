num =1
while num>9:
    string_num = str(num)
    t=tuple(string_num)
    c=1
    for i in range(0,len(t)):
        c = c*int(t[i])
    num=c
print(num)



