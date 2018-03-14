import command_system
from common_func import keyword_gen

def olimp(keyword=''):
   message = '''30.01.2018-31.01.2018 - География
31.01.2018-02.02.2018 - Математика
02.02.2018-03.02.2018, 05.02.2018 - История
05.02.2018-06.02.2018, 08.02.2018 - Обществознание
07.02.2018-08.02.2018, 09.02.2018 - Экология
09.02.2018-08.02.2018, 11.02.2018 - Физическая культура
12.02.2018-14.02.2018 - Английский язык
14.02.2018-16.02.2018 - Технология
16.02.2018-18.02.2018 - ОБЖ
19.02.2018-20.02.2018 - Немецкий язык
'''
   return message, ''

olimp_command = command_system.Command()
olimp_command.keys = keyword_gen('олимпиада', 'олимп', 'olipmpiada','olip')
olimp_command.description = 'Скажу запланированные олимпиады'
olimp_command.process = olimp
