import codecs

def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'w', 'utf-8') as file:
        file.write("hello \n"
                   "<fsdgsdgio>>")
    with open(html_file, 'r') as file:
        for line in file:
            if ('<' and '>' in line) and (line.find('<') < line.find('>')):
                a = line.find('<')
                b = line.find('>')
                c = line[:a] + line[b+1:]
                print ("\n", c)
            else:
                print ("\n", line)

delete_html_tags('cleaned.txt')

