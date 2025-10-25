def add_one(some_list):
    str_some_list = ""
    for arg in some_list:
        str_some_list += str(arg)
    int_some_list = int(str_some_list) + 1
    str_some_list = str(int_some_list)
    _string = " ".join(str_some_list)
    a = _string.split()
    a = [int(x) for x in a]
    return a


assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")