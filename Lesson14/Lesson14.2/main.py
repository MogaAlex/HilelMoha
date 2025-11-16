import mod2
import mod3
import zipfile
import codecs

with zipfile.ZipFile('my_archive.zip', 'w') as myzip:
    with codecs.open("result_file.txt", 'w', 'utf-8') as result:
        st1 = mod2.Student('Male', 30, 'Steve', 'Jobs', 'AN142')
        st2 = mod2.Student('Female', 25, 'Liza', 'Taylor', 'AN145')
        gr = mod3.Group('PD1')
        gr.add_student(st1)
        gr.add_student(st2)
        result.write(str(gr))

        assert gr.find_student('Jobs') == st1  # 'Steve Jobs'
        assert gr.find_student('Jobs2') is None
        gr.delete_student('Taylor')

        result.write(str(gr))  # Only one student
    myzip.write('main.py')
    myzip.write('mod1.py')
    myzip.write('mod2.py')
    myzip.write('mod3.py')
    myzip.write('result_file.txt')
