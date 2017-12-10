import command_system

def merop(keyword=''):
   message = 'Приветствую!\nНа данный момент мероприятий не запланировано.'
   return message, ''

merop_command = command_system.Command()
merop_command.keys = [ 'мероприятия', 'vthjghbznbz', 'merop', 'мероп']
merop_command.description = 'Скажу Запланированные Мероприятия'
merop_command.process = merop