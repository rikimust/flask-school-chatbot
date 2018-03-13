import command_system
from common_func import keyword_gen


def subscribe(keyword='', user_id=''):
    message = 'Молодец'

    return message, ''


subscribe_command = command_system.Command()
subscribe_command.keys = keyword_gen('подписка')
subscribe_command.aliases = keyword_gen('подписываюсь', 'рассылка')
subscribe_command.description = 'Подпишу тебя на рассылку'
subscribe_command.process = subscribe
