import command_system

def proverka(keyword=''):
   message = 'Приветствую!\nМожешь проверить своё решение\nФизика - https://goo.gl/nsTeCT\nАнглийский - https://goo.gl/i1ehb4\nРусский - https://goo.gl/nFhV1k\nХимия - https://goo.gl/g4wW9f'
   return message, ''

proverka_command = command_system.Command()
proverka_command.keys = ['Помощь с дз','гдз','ulp','Gjvjom c lp','gdz']
proverka_command.description = 'Позволю Проверить Твоё Решение'
proverka_command.process = proverka