import command_system
from common_func import keyword_gen
def hometask(keyword=''):
   message = '''Домашнее задание:

Понедельник:
География на 12 марта! Стр 115-123. Повторить союзные государства.

Вторник:
Химия на 13 марта! Пр 16 Номера 1, 3-6
на 20 марта! Пр 17 упр 1-5
Английский на 13 марта! Презентация о школьном меню.
Математика на 13 марта! 39.4, 39.6

Четверг:
Физика на 15 марта! Пр 84, стр 261 впросы - устно. А1-А4 письменно.

Суббота:
Литература на 17 марта! Подготовиться к работе с текстами.
География на 17 марта! Стр 115-123. Повторить союзные государства.

        '''
#   Среда
#   Ничего
#   Четверг
#   Ничего
   attachment = 'photo175396580_456242779' #, 'photo-116616497_456239069'
   #test = audios220918397
   return message, attachment

#   #attachment = "video-66678575_456251059"
hometask_command = command_system.Command()

hometask_command.keys =  keyword_gen('дз','Домашнее задание','hometask', 'lp','DZ','Домашка')
hometask_command.description = 'Скажу Домашнее Задание'
hometask_command.process = hometask
