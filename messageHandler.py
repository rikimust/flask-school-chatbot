import vkapi
import os
import importlib
from command_system import command_list


def damerau_levenshtein_distance(s1, s2):
    '''return 0 if s1 = s2, else return count of differences'''
    d = {}
    lenstr1 = len(s1)
    lenstr2 = len(s2)
    for i in range(-1, lenstr1 + 1):
        d[(i, -1)] = i + 1
    for j in range(-1, lenstr2 + 1):
        d[(-1, j)] = j + 1
    for i in range(lenstr1):
        for j in range(lenstr2):
            if s1[i] == s2[j]:
                cost = 0
            else:
                cost = 1
            d[(i, j)] = min(
                d[(i - 1, j)] + 1,  # deletion
                d[(i, j - 1)] + 1,  # insertion
                d[(i - 1, j - 1)] + cost,  # substitution
            )
            if i and j and s1[i] == s2[j - 1] and s1[i - 1] == s2[j]:
                d[(i, j)] = min(d[(i, j)], d[i - 2, j - 2] + cost)  # transposition
    return d[lenstr1 - 1, lenstr2 - 1]


def get_answer(request_body):
    message = "Прости, не понимаю тебя. Напиши 'помощь', чтобы узнать мои команды"
    attachment = ''
    distance = len(request_body)
    target_command = None
    target_key = ''
    for command in command_list:
        for command_key in command.keys:
            d = damerau_levenshtein_distance(request_body, command_key)
            if d < distance:
                distance = d
                target_command = command
                target_key = command_key
                if distance == 0:
                    message, attachment = target_command.process(target_key)
                    return message, attachment
    if distance < len(request_body)*0.4:
        message, attachment = target_command.process(target_key)
        message = 'Вы ошиблись с запросом! Наверное, вы хотели ввести: "%s"\n\n' % target_key + message
    return message, attachment


def load_modules():
   files = os.listdir(os.path.join(os.path.dirname(__file__), 'commands'))
   modules = filter(lambda x: x.endswith('.py'), files)
   for m in modules:
       importlib.import_module("commands." + m[0:-3])


def create_answer(data, token):
   load_modules()
   user_id = data['user_id']
   message, attachment = get_answer(data['body'].lower())
   vkapi.send_message(user_id, token, message, attachment)