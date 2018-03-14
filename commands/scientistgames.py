import command_system
from common_func import keyword_gen

def scientistgames(keyword=''):
   message = '''Приветствую!
   Создание мультиков - http://multa.ch/
   Судоку - http://scanvord.net/sudoku/
   2048 - http://2048game.com/ru/
   Шахматы - https://www.chess.com/ru/play/computer
   Шашки - http://www.shashky.ru/'''
   return message, ''

scientistgames_command = command_system.Command()
scientistgames_command.keys = keyword_gen('скучно', 'crexyj', 'skychno')
scientistgames_command.description = 'Предложу Развивающие И Познавательные Игры'
scientistgames_command.process = scientistgames
