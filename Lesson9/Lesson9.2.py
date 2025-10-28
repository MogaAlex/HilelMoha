def difference(*number: int or float) -> int or float:
    if len(number) == 0:
        return 0
    else:
        num1 = max(number) - min(number)
        num2 = round(num1,2)
        return num2


assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print("OK")


