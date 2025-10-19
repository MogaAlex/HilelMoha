import string

t= str(input())
e1= t[0]
e2= t[2]
lst = string.ascii_letters
ind1 = lst.find(e1)
ind2 = lst.find(e2)
print(lst[ind1:ind2+1])
