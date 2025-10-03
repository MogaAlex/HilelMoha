num = int(input ())
a = num // 10000
b = num // 1000 % 10
c = num // 100 % 10
d = num // 10 % 10
e = num % 10
sum = e * 10000 + d * 1000 + c*100 + b*10 + a
print (sum)