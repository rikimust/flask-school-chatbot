import command_system
from datetime import timedelta
from common_func import keyword_gen, TimeNow, get_lesson_number
from data_base import TIMETABLE, SHIFT, DAYS_NAME


def get_time_before_ring(time_now):
    key_day, lesson_now, is_time_change = get_lesson_number(time_now)
    if lesson_now == 'before':
        td_first_lesson = timedelta(
            hours=TIMETABLE[key_day][SHIFT][0][1].hour,
            minutes=TIMETABLE[key_day][SHIFT][0][1].minute)
        minute_before = td_first_lesson - time_now.td
        message = 'Уроки ещё не начались, до начала {0}:{1}'.\
                  format(minute_before.seconds//3600,
                         str(minute_before.seconds%3600//60).zfill(2))
    elif lesson_now == 'after':
        td_last_lesson = timedelta(
            hours=TIMETABLE[key_day][SHIFT][-1][2].hour,
            minutes=TIMETABLE[key_day][SHIFT][-1][2].minute)
        minute_before = time_now.td - td_last_lesson
        message = 'Уроки уже прошли. {0} закончился {1}:{2} назад'.\
                  format(TIMETABLE[key_day][SHIFT][-1][0],
                         minute_before.seconds//3600,
                         str(minute_before.seconds%3600//60).zfill(2))
    else:
        if is_time_change:
            next_lesson = TIMETABLE[key_day][SHIFT][lesson_now + 1]
            td_next_lesson_beg = timedelta(
                hours=next_lesson[1].hour,
                minutes=next_lesson[1].minute)
            minute_before = td_next_lesson_beg - time_now.td
            message = '{} завершен. Перемена, до звонка {} минут'.\
                      format(TIMETABLE[key_day][SHIFT][lesson_now][0],
                             minute_before.seconds//60)
        else:
            td_lesson_end = timedelta(
                hours=TIMETABLE[key_day][SHIFT][lesson_now][2].hour,
                minutes=TIMETABLE[key_day][SHIFT][lesson_now][2].minute)
            minute_before = td_lesson_end - time_now.td
            message = 'Идёт "{}", до звонка {} минут'.\
                      format(TIMETABLE[key_day][SHIFT][lesson_now][0].title(),
                             minute_before.seconds//60)
    return message


def get_daily_timetable(time_now, day):
   if day == time_now.week_day:
      key_day, lesson_now, is_time_change = get_lesson_number(time_now)
   else:
      lesson_now = None
   for key_day in TIMETABLE:
      if day in key_day:
         message = DAYS_NAME[day].upper() + '\n'
         if lesson_now == 'before':
            message += 'СЕЙЧАС {0:%H}:{0:%M}\n'.format(time_now.time)
         for n, lesson in enumerate(TIMETABLE[key_day][SHIFT]):
             message += '{0}: {1:%H}:{1:%M} - {2:%H}:{2:%M}\n'.\
                        format(lesson[0], lesson[1], lesson[2])
             if lesson_now == n:
                if is_time_change:
                   message += 'СЕЙЧАС {0:%H}:{0:%M}\n'.format(time_now.time)
                else:
                   message = message[:-1] + \
                             ', СЕЙЧАС {0:%H}:{0:%M}\n'.format(time_now.time)
         if lesson_now == 'after':
            message += 'СЕЙЧАС {0:%H}:{0:%M}\n'.format(time_now.time)
   return message


def get_timetable(keyword=''):
   time_now = TimeNow()
   if keyword in keyword_gen('звонки сегодня','звонки на сегодня','звнксгд'):
      message = get_daily_timetable(time_now, time_now.week_day)
   elif keyword in keyword_gen('звонки завтра','звонки на завтра','звнкзвт'):
      message = get_daily_timetable(time_now, time_now.week_day+1)
   elif keyword in keyword_gen('звонки вчера', 'звонки на вчера', 'звнквчр'):
      message = get_daily_timetable(time_now, time_now.week_day-1)
   elif keyword in keyword_gen('звонки понедельник','звонки на понедельник','звнкпн'):
      message = get_daily_timetable(time_now, 0)
   elif keyword in keyword_gen('звонки вторник','звонки на вторник','звнквт'):
      message = get_daily_timetable(time_now, 1)
   elif keyword in keyword_gen('звонки среда','звонки на среду','звнкср'):
      message = get_daily_timetable(time_now, 2)
   elif keyword in keyword_gen('звонки четверг','звонки на четверг','звнкчт'):
      message = get_daily_timetable(time_now, 3)
   elif keyword in keyword_gen('звонки пятница','звонки на пятницу','звнкпт'):
      message = get_daily_timetable(time_now, 4)
   elif keyword in keyword_gen('звонки суббота','звонки на субботу','звнксб'):
      message = get_daily_timetable(time_now, 5)
   elif keyword in keyword_gen('звонки воскресенье','звонки на восткресенье','звнквс'):
      message = get_daily_timetable(time_now, 6)
   else:
      message = get_time_before_ring(time_now)
   return message, ''


timetable_command = command_system.Command()
timetable_command.keys =  keyword_gen('звонок','до звонка','звнк', 'pdjyjr',
                                     'звонки сегодня','звонки на сегодня','звнксгд','pdjyrb yf ctujlyz',
                                     'звонки завтра','звонки на завтра','звнксгд', 'pdjyrb yf pfdnhf',
                                     'звонки вчера', 'звонки на вчера', 'звнквчр', 'pdjyrb yf dxthf',
                                     'звонки понедельник','звонки на понедельник','звнкпн', 'pdjyrb yf gjytltkmybr',
                                     'звонки вторник','звонки на вторник','звнквт', 'pdjyrb yf dnjhybr',
                                     'звонки среда','звонки на среду','звнкср', 'pdjyrb yf chtle',
                                     'звонки четверг','звонки на четверг','звнкчт', 'pdjyrb yf xtndthu',
                                     'звонки пятница','звонки на пятницу','звнкпт', 'pdjyrb yf gznybwe',
                                     'звонки суббота','звонки на субботу','звнксб', 'pdjyrb yf ce,,jne',
                                     'звонки воскресенье','звонки на воскресенье','звнквс','pdjyrb yf pfdnhf')
timetable_command.description = '''Скажу расписание звонков на вчера/сегодня/завтра/пн/вт/ср/чт/пт/сб/вс, либо сколько осталось до звонка'''
timetable_command.process = get_timetable
