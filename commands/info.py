import command_system
from common_func import keyword_gen

def info(keyword=''):
    message = ''
    if keyword in keyword_gen('все команды'):
        for command in command_system.command_list:
            message += '{}\n'.format(command.keys[0].upper())
            if command.keys[1:] is not []:
                for key in command.keys[1:]:
                    if key[0] not in "qwertyuiop[]asdfghjkl;\'zxcvbnm,./":
                        message += '{}, '.format(key)
                message = message[:-1] + '.\n'
    else:
        for command in command_system.command_list:
            message += '{} - {}\n'.format(command.keys[0].upper(), command.description.lower())
    return message, ''

info_command = command_system.Command()
info_command.keys = keyword_gen('помощь', 'помоги', 'help', 'Хелп', 'pomosh', 'все команды')
info_command.description = 'Покажу список команд'
info_command.process = info
