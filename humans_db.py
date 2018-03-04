from datetime import datetime
import csv

pupils_list = []
teachers_list = []
parents_list = []


class Human:
    def __init__(self, ln, fn, pn='', phone=None, bd=None):
        self.last_name = ln.title()   # Фамилия
        self.first_name = fn.title()  # Имя
        self.patronym = pn.title()    # Отчество
        self.__set_phone(phone)       # Телефон      
        self.__set_bd(bd)             # День рождения                      

    def __get_phone(self):
        if not self.__phone:
            return 'неизвестно'
        else:
            return '+7({}){}-{}-{}'.format(self.__phone[:3], self.__phone[3:6], self.__phone[6:8], self.__phone[8:])

    def __set_phone(self, phone):
        if len(phone) == 10 and phone[0] == '9':
            self.__phone = phone
        elif len(phone) == 11 and (phone[0] == '7' or phone[0] == '8'):
            self.__phone = phone[1:]
        elif len(phone) == 12 and phone[:2] == '+7':
            self.__phone = phone[2:]
        else:
            self.__phone = None

    def __get_bd(self):
        if self.__bd:
            return '{0:%d}.{0:%m}.{0:%Y}'.format(self.__bd)
        else:
            return 'неизвестно'

    def __set_bd(self, bd):
        if type(bd) == datetime:
            self.__bd = bd
        elif type(bd) == str:
            day, month, year = map(int, bd.split('.'))
            self.__bd = datetime(year, month, day)
        else:
            self.__bd = None

    def __get_name(self):
        return '{} {} {}'.format(self.last_name, self.first_name, self.patronym)

    bd = property(__get_bd, __set_bd)
    name = property(__get_name)
    phone = property(__get_phone, __set_phone)


class Pupil(Human):
    def __init__(self, ln, fn, pn, phone=None, bd=None):
        Human.__init__(self, ln, fn, pn, phone, bd)
        pupils_list.append(self)


class Teacher(Human):
    def __init__(self, ln, fn, pn, phone=None, bd=None, subject=None, post=None):
        Human.__init__(self, ln, fn, pn, phone, bd)
        if subject == ['']:
            self.subject = None
        else:
            self.subject = subject
        if post == ['']:
            self.post = None
        else:
            self.post = post
        teachers_list.append(self)


class Parent(Human):
    def __init__(self, ln, fn, pn, phone=None, bd=None, child=None):
        Human.__init__(self, ln, fn, pn, phone, bd)
        self.child = child
        parents_list.append(self)


def read_teachers(file_name='teachers.csv'):
    with open(file_name, encoding='utf-8') as csv_file:
        reader_dict = csv.DictReader(csv_file, delimiter=';')
        for line in reader_dict:
            if line['is_active'] == '1':
                teacher = Teacher(
                    ln=line['last_name'],
                    fn=line['first_name'],
                    pn=line['patronym'],
                    phone=line['phone'],
                    bd=line['bd'],
                    subject=line['subjects'].split(','),
                    post=line['post'].split(','))


def read_pupils(file_name='pupils.csv'):
    with open(file_name, encoding='utf-8') as csv_file:
        reader_dict = csv.DictReader(csv_file, delimiter=';')
        for line in reader_dict:
            pupil = Pupil(
                ln=line['last_name'],
                fn=line['first_name'],
                pn=line['patronym'],
                phone=line['phone'],
                bd=line['bd'])


read_teachers()
read_pupils()

for t in teachers_list:
    print(t.post)
