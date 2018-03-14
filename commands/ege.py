import command_system
from common_func import keyword_gen

def ege(keyword=''):
   message = '''Приветствую!
Решу ЕГЭ - https://ege.sdamgia.ru/
Яндекс ЕГЭ - https://ege.yandex.ru/ege/
Полезная Информация - http://www.ege.edu.ru/ru/main/'''
   return message, ''

ege_command = command_system.Command()

ege_command.keys = keyword_gen('егэ','ege')
ege_command.description = 'Выдам Информацию По ЕГЭ'
ege_command.process = ege
