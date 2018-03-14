import command_system
from common_func import keyword_gen
def sos(keyword=''):
   message = '''Приветствую!
   МЧС России (пожарная охрана, спасатели) – 101
   Полиция – 102
   Скорая медицинская помощь – 103
   Аварийная газовая служба - 104
   Единая служба спасения – 112
   Сайт Школы - http://severschool10.ru/
   ГосУслуги - https://51gosuslugi.ru/rpeu/'''
   return message, ''

sos_command = command_system.Command()
sos_command.keys =  keyword_gen( 'сос', 'sos','Ыщы','cjc')
sos_command.description = 'Покажу Важные Ссылки'
sos_command.process = sos
