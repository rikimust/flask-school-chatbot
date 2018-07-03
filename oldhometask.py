import command_system
from common_func import keyword_gen
def oldhometask(keyword = ''):
    message = '''Домашнее задание:

Понедельник
География на 5 марта! Стр 106-115 и выучить страны ЕС,ОПЕК,СНГ,НАФТА,ОТЕС,ЛАИ.
Математика на 5 марта! 36.12, 38.12, 38.13.
Физика на 5 марта! Смотрите фото.

Вторник
Химия на 6 марта! Физмат: пр 14, упр 1,3,4. пр15 упр 2,3,5
Обществознание на 6 марта! Стр 60-64. Написать в тетради "Как открыть своё дело"
Математика на 6 марта! 39.2, 39.8

Среда
Русский язык на 7 марта!: Пр 36-38. Номера 201, 202

Четверг
Физика на 8 марта! Кр 9 Вариант 4

Суббота
Литература на 10 марта! Читать по учебнику статью о жизни и творчестве Салтыкова-Щедрина. Почитать сказки "Коняга", "Пропала совесть", Премурый пискарь"."
'''
    attachment = 'photo-116616497_456239070'
    return message, attachment

oldhometask_command = command_system.Command()

oldhometask_command.keys = keyword_gen('Прошлое дз', 'Прошедшее дз', 'Старое дз', 'old hometask', 'last hometask')
oldhometask_command.description = 'Скажу прошлое домашнее задание'
oldhometask_command.process = oldhometask