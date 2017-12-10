import command_system
from common_func import keyword_gen

def facult(keyword=''):
   message = 'Факультатив по Информатике:\nПонедельник - 5 урок\nСреда - 7 урок'
   return message, ''

facult_command = command_system.Command()

facult_command.keys = keyword_gen('факультатив','факульт','фак')
facult_command.description = 'Скажу запланированные факультативы'
facult_command.process = facult