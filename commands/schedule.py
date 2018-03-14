import command_system
from data_base import SCHEDULE, DAYS_NAME
from common_func import keyword_gen, TimeNow


def get_daily_schedule(week_day):
    lessons = DAYS_NAME[week_day].upper() + ':\n'
    for lesson in SCHEDULE[week_day]:
        subject = "ПУСТО" if lesson[1] == '' else lesson[1]
        lessons += '{}. {}\n'.format(lesson[0], subject)
    return lessons

def get_schedule(keyword=''):
    time_now = TimeNow()
    if keyword in keyword_gen('расписание','расп'):
        message = '\n\n'.join([get_daily_schedule(week_day) for week_day in range(7)])
    elif keyword in keyword_gen('расписание на сегодня', 'расписание сегодня', 'распсгд', 'расп на сегодня'):
        message = get_daily_schedule(time_now.week_day)
    elif keyword in keyword_gen('расписание на завтра','расписание завтра','распзвт', 'расп на завтра'):
        message = get_daily_schedule((time_now.week_day + 1) % 7)
    elif keyword in keyword_gen('расписание на вчера','расписание вчера','распвчр', 'расп на вчера'):
        message = get_daily_schedule((time_now.week_day - 1) % 7)
    elif keyword in keyword_gen('расписание на понедельник','расписание понедельник','расппн', 'расп на понедельник'):
        message = get_daily_schedule(0)
    elif keyword in keyword_gen('расписание на вторник','расписание вторник','распвт', 'расп на вторник'):
        message = get_daily_schedule(1)
    elif keyword in keyword_gen('расписание на среду','расписание среда','распср', 'расп на среду'):
        message = get_daily_schedule(2)
    elif keyword in keyword_gen('расписание на четверг','расписание четверг','распчт', 'расп на четверг'):
        message = get_daily_schedule(3)
    elif keyword in keyword_gen('расписание на пятницу','расписание пятница','расппт', 'расп на пятницу'):
        message = get_daily_schedule(4)
    elif keyword in keyword_gen('расписание на субботу','расписание суббота','распсб', 'расп на субботу'):
        message = get_daily_schedule(5)
    elif keyword in keyword_gen('расписание на воскресенье','расписание воскресенье','распвс', 'расп на воскресенье'):
        message = get_daily_schedule(6)
    else:
        message = '¯\_(ツ)_/¯ sorry...'
    return message, ''


schedule_command = command_system.Command()
schedule_command.keys = keyword_gen('расписание','расп', 'hfcgbcfybt', 'hfcg',
                                    'расписание на сегодня', 'расписание сегодня', 'распсгд', 'hfcgbcfybt yf ctujlyz', 'hfcg yf ctujlyz',
                                    'расписание на завтра','расписание завтра','распзвт', 'hfcgbcfybt yf pfdnhf', 'hfcg yf pfdnhf',
                                    'расписание на вчера','расписание вчера','распвчр', 'hfcgbcfybt yf dxthf', 'hfcg yf dxthf',
                                    'расписание на понедельник','расписание понедельник','расппн', 'hfcgbcfybt yf gjytltkmybr', 'hfcg yf gjytltkmybr',
                                    'расписание на вторник','расписание вторник','распвт', 'hfcgbcfybt yf dnjhybr', 'hfcg yf dnjhybr',
                                    'расписание на среду','расписание среда','распср', 'hfcgbcfybt yf chtle', 'hfcg yf chtle',
                                    'расписание на четверг','расписание четверг','распчт', 'hfcgbcfybt yf xtndthu', 'hfcg yf xtndthu',
                                    'расписание на пятницу','расписание пятница','расппт', 'hfcgbcfybt yf gznybwe', 'hfcg yf gznybwe',
                                    'расписание на субботу','расписание суббота','распсб', 'hfcgbcfybt yf ce,,jne', 'hfcg yf ce,,jne',
                                    'расписание на воскресенье','расписание воскресенье','распвс','hfcgbcfybt yf djcrhtctymt', 'hfcg yf djcrhtctymt',)
schedule_command.description = 'Скажу расписание уроков на вчера/сегодня/завтра/пн/вт/ср/чт/пт/сб/вс, либо на всю неделю'
schedule_command.process = get_schedule
