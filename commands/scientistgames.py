import command_system

def scientistgames(keyword=''):
   message = 'Приветствую!\nСоздание мультиков - http://multa.ch/\nСудоку - http://scanvord.net/sudoku/\n2048 - http://2048game.com/ru/\nШахматы - https://www.chess.com/ru/play/computer\nШашки - http://www.shashky.ru/'
   return message, ''

scientistgames_command = command_system.Command()
scientistgames_command.keys = ['скучно', 'crexyj', 'skychno',]
scientistgames_command.description = 'Предложу Развивающие И Познавательные Игры'
scientistgames_command.process = scientistgames