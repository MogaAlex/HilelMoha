import codecs

def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'w', 'utf-8') as file:
        file.write("hello <fsafas>  <fafa > \n"
                   "fsdgsdgio>>")
    with codecs.open(result_file, 'w', 'utf-8') as clean:
        with (open(html_file, 'r') as file):
            for line in file:
                while '<' in line and '>' in line and line.find('<') < line.find('>'):
                    a = line.find('<')
                    b = line.find('>')
                    line = line[0:a] + line[b+1:]
                clean.write(line)


delete_html_tags('basic.txt')



