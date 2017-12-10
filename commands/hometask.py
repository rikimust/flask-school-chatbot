import command_system

def hometask(keyword=''):
   message = 'Приветствую!\nДомашнее задание:\nСреда\nАнализ стихотворения Фета или Тютчева. Особенности поэзии Тютчева и Фета с 233, с 328 Гончаров с 135-138 Жизнь и творчество История создания, особенности композиции Обломов с 144-154 '
   return message, ''

hometask_command = command_system.Command()

hometask_command.keys = ['дз','Домашее задание','hometask', 'lp','DZ','Домашка']
hometask_command.description = 'Скажу Домашнее Задание'
hometask_command.process = hometask
