from datetime import datetime, timezone, timedelta
from data_base import TIMETABLE, SHIFT


class TimeNow:
    def __init__(self):
        datetime_now = datetime.now(tz=timezone(timedelta(hours=3)))
        #datetime_now = datetime(2017,11,11,12,45)
        self.week_day = datetime_now.weekday()
        self.time = datetime_now.time()
        self.td = timedelta(hours=self.time.hour, minutes=self.time.minute)


def translite(word, lang_to='eng'):
   table_rus = "ячсмитьбю.фывапролджэйцукенгшщзхъ"
   table_eng = "zxcvbnm,./asdfghjkl;'qwertyuiop[]"
   if lang_to == 'eng':
      table = str.maketrans(table_rus, table_eng)
   else:
      table = str.maketrans(table_eng, table_rus)
   return word.translate(table)



def keyword_gen(*keywords):
   for keyword in keywords:
      yield keyword.lower()
      yield translite(keyword.lower())


def get_lesson_number(time_now):
   for key_day in TIMETABLE:
      if time_now.week_day in key_day:
         key_day_now = key_day
         lesson_now = 'before'
         is_time_change = True
         for lesson_num in range(len(TIMETABLE[key_day_now][SHIFT])):
            lesson_temp = TIMETABLE[key_day_now][SHIFT][lesson_num]
            if time_now.time >= lesson_temp[1]:
               lesson_now = lesson_num
               if time_now.time < lesson_temp[2]:
                  is_time_change = False
                  break
               else:
                  is_time_change = True
            else:
               break
         else:
            lesson_now = 'after'
   return key_day_now, lesson_now, is_time_change