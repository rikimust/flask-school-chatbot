import command_system
from common_func import keyword_gen
from humans_db import teachers_list


def teacher(keyword=''):
    message = ''
    for teacher in sorted(teachers_list, key=lambda t: t.last_name):
        if not teacher.subject:
            about = ', '.join(teacher.post)
        else:
            about = ', '.join(teacher.subject)
            other_post = [post for post in teacher.post if post != 'учитель']
            if other_post != []:
                about += ', ' + ', '.join(other_post)
        message += '{} - {}\n'.format(teacher.name, about)
    return message, ''


teacher_command = command_system.Command()
teacher_command.keys = keyword_gen('учителя')
teacher_command.aliases = keyword_gen('педагоги', 'преподаватели', 'преподы')
teacher_command.description = 'Покажу список учителей'
teacher_command.process = teacher
