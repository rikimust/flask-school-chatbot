import command_system

def ege(keyword=''):
   message = 'Приветствую!\nРешу ЕГЭ - https://ege.sdamgia.ru/\nЯндекс ЕГЭ - https://ege.yandex.ru/ege/\nПолезная Информация - http://www.ege.edu.ru/ru/main/'
   return message, ''

ege_command = command_system.Command()

ege_command.keys = ['егэ','ege']
ege_command.description = 'Выдам Информацию По ЕГЭ'
ege_command.process = ege