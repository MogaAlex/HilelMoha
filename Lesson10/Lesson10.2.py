import string

def first_word(text: str) -> str:
    # print(string.punctuation.find("'")) # №6
    new_string_punctuation = string.punctuation[:6] + string.punctuation[7:]
    for i in new_string_punctuation:
        if (i in text) == True:
            new_my_string = text.replace(i, ' ')
            break
        else:
            new_my_string = text
    final_string = ""
    for i in new_my_string:
        if (i in new_string_punctuation) == False:
            final_string += i
    return final_string.split()[0]

assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')
