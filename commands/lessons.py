import command_system
from common_func import keyword_gen, TimeNow, get_lesson_number
from data_base import TIMETABLE, SCHEDULE, SHIFT


def get_subject_by_lesson(day, lesson_num):
   if not 0 <= day <= 6:
      raise Exception('Day index is not correct')
   if lesson_num > len(SCHEDULE[day])-1:
      subject = 'Уроки уже кончились'
   else:
      subject = SCHEDULE[day][lesson_num][1]
   return subject if subject != '' else 'ПУСТО'

def get_lesson(keyword=''):
   time_now = TimeNow()
   key_day, lesson_num, is_time_change = get_lesson_number(time_now)
   if lesson_num == 'before':
      message = 'Уроки ещё не начались, первый урок - {}'.format(
         get_subject_by_lesson(time_now.week_day, 0))
   elif lesson_num == 'after' or lesson_num > len(SCHEDULE[time_now.week_day]) - 1:
      message = 'Уроки уже прошли, последний урок - {}'.format(
         get_subject_by_lesson(time_now.week_day, -1))
   else:
      if keyword in keyword_gen('урок следующий','следующий урок','урокслед'):
         if len(SCHEDULE[time_now.week_day]) - 1 == lesson_num:
            message = '{} - {} последний'.format(
               TIMETABLE[key_day][SHIFT][lesson_num][0],
               get_subject_by_lesson(time_now.week_day, lesson_num))
         else:
            message = '{} - {}'.format(
               TIMETABLE[key_day][SHIFT][lesson_num+1][0],
               get_subject_by_lesson(time_now.week_day, lesson_num))
      elif keyword in keyword_gen('урок предыдущий','предыдущий урок','урокпред'):
         if lesson_num == 0:
            message = 'идёт {} - {}, занятия только начались'.format(
               TIMETABLE[key_day][SHIFT][lesson_num][0],
               get_subject_by_lesson(time_now.week_day, lesson_num))
         else:
            message = '{} - {}'.format(
               TIMETABLE[key_day][SHIFT][lesson_num-1][0],
               get_subject_by_lesson(time_now.week_day, lesson_num))
      else: # 'урок','урок текущий','текущий урок','уроктек'
         str_template = '{} - {} окночен, перемена' if is_time_change \
                        else '{} - {}'
         message = str_template.format(
            TIMETABLE[key_day][SHIFT][lesson_num][0],
            get_subject_by_lesson(time_now.week_day, lesson_num))
   return message, ''

lessons_command = command_system.Command()
lessons_command.keys = keyword_gen('урок','урок текущий','текущий урок','уроктек',
                                   'урок следующий','следующий урок','урокслед',
                                   'урок предыдущий','предыдущий урок','урокпред')
lessons_command.description = '''Скажу какой предыдущий/текущий/следующий урок'''
lessons_command.process = get_lesson