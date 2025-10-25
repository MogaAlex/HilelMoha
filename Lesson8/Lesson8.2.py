import string
def is_palindrome(text):
    c = ""
    for i in text:
        if i not in string.punctuation and i not in " ":
            c = c + i
    new_text = c.lower()
    inverse_text = new_text[::-1]
    return (inverse_text == new_text)

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")

