import command_system
from common_func import keyword_gen

def proverka(keyword=''):
   message = '''Физика:
Учебник: https://goo.gl/ndFdPj
Рымкевич: https://goo.gl/M1DQHc

Английский язык: https://goo.gl/M1DQHc

Русский: https://goo.gl/xnd7pT

Химия: https://goo.gl/NDMKLF'''
   return message, ''

proverka_command = command_system.Command()
proverka_command.keys = keyword_gen('Помощь с дз','гдз','ulp','Gjvjom c lp','gdz')
proverka_command.description = 'Помогу с домашним заданием'
proverka_command.process = proverka
