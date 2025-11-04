def is_even(number: int) -> bool:
    b = str(number)
    list=[]
    for i in b:
        list.append(i)
    if list[-1] == '0' or list[-1] == '2' or  list[-1]== '4' or list[-1]== '6' or list[-1]=='8':
        return True
    else:
        return False

assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'
print("OK")