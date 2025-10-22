def second_index(text, some_str):
    if some_str in text:
        a = text.find(some_str)
        if (text.find(some_str, a + 1)) != -1:
            return text.find(some_str, a + 1)
        else:
            return None
    else:
        return None


assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')
