import command_system
from common_func import keyword_gen

def merop(keyword=''):
   message = '''На данный момент мероприятий не запланировано.'''
   return message, ''

merop_command = command_system.Command()
merop_command.keys = keyword_gen('мероприятия', 'vthjghbznbz', 'merop', 'мероп')
merop_command.description = 'Скажу Запланированные Мероприятия'
merop_command.process = merop
