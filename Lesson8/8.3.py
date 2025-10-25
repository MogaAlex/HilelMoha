def find_unique_value(args):
    b = list()
    for arg in args:
        b.append(args.count(arg))
        if b.count(1) == 1:
            k=1
        else:
            k=0
    for arg in args:
        if args.count(arg) == 1 and k==1:
            return arg

assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")