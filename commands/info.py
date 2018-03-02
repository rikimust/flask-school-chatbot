import command_system
from common_func import keyword_gen

def help(keyword=''):
    message = ''
    for command in command_system.command_list:
        message += '{} - {}\n'.format(command.keys[0].upper(),
                                      command.description.lower())
    return message, ''

help_command = command_system.Command()
help_command.keys = keyword_gen('помощь')
help_command.alias = keyword_gen('помоги', 'help', 'хелп', 'pomosh')
help_command.description = 'Покажу список команд'
help_command.process = help

def all_commands(keyword=''):
    message = ''
    for command in command_system.command_list:
        message += '{}\n'.format(command.keys[0].upper())
        if command.keys[1:] is not []:
            for key in command.keys[1:]:
                if key[0] not in "qwertyuiop[]asdfghjkl;\'zxcvbnm,./":
                    message += '{}, '.format(key)
            message = message[:-1] + '.\n'
    return message, ''

all_commands_command = command_system.Command()
all_commands_command.keys = keyword_gen('команды')
all_commands_command.alisas = keyword_gen('все команды', 'список команд')
all_commands_command.description = 'Покажу список всех команд'
all_commands_command.process = all_commands