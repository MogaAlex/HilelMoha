import string
import keyword

my_string = "-"

#Условие первой цифры
x= my_string[0]

#Условие пунтктуации
ind = string.punctuation.find('_')
new_string_punctuation = string.punctuation[0:26] + string.punctuation[27:]
for a in my_string:
    if a in new_string_punctuation:
        b=1
        break
    else:
        b=0

#Условие зарегестрированных слов.
lst = my_string.split()
for i in range (0, len(lst)):
    if (keyword.iskeyword(lst[i]) or (lst[i]=='get')) == True:
        c=1
        break
    else:
        c=0

#Условие большой буквы
for j in my_string:
    if (j.isupper()==True):
        d=1
        break
    else:
        d=0

# Проверка условий.
if d==1: #Условие большой буквы
    print(False)
# elif (my_string.islower()==False): #Условие большой буквы
#     print(False)
elif (x.isdigit() == True): #Условие первой цифры
    print(False)
elif c==1: #Условие зарегестрированных слов.
    print(False)
elif b==1: #Условие пунктуации
    print(False)
elif "__" in my_string: #Условие нижнего подчеркиванния
    print(False)
elif " " in my_string: #Условие пробелов
    print(False)
else:
    print(True)

