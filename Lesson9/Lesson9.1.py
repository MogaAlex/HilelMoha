def popular_words (text, words):
    lst = text.lower().split()
    a = []
    b= []
    c = {}
    for word in words:
        a.append(word)
        b.append(lst.count(word))
    c = {a: b for a, b in zip(a, b)}
    return c

assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')

