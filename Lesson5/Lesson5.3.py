import string
my_str = "Should, I. subscribe? Yes!"
my_str = my_str.title() #Условие большой буквы
#Условие пунктуации
c=""
for a in my_str:
    if (a in string.punctuation) == False:
        c=c+a
#Условие слития
lst = c.split()
b="#"
for i in range(0,len(lst)):
    b = b+lst[i]
#Условие длины
if len(b)>=140:
    d= b[0:140]
    print(d)
else:
    print(b)