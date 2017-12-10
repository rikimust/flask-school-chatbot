import command_system

def sos(keyword=''):
   message = 'Приветствую!\nМЧС России (пожарная охрана, спасатели) – 101\nПолиция – 102\nСкорая медицинская помощь – 103\nАварийная газовая служба - 104\nЕдиная служба спасения – 112\nСайт Школы - http://severschool10.ru/\nГосУслуги - https://51gosuslugi.ru/rpeu/'
   return message, ''

sos_command = command_system.Command()
sos_command.keys = [ 'сос', 'sos','Ыщы','cjc']
sos_command.description = 'Покажу Важные Ссылки'
sos_command.process = sos