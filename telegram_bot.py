#ПРОБНАЯ ВЕРСИЯ БОТА ДЛЯ ТЕЛЕГИ
#НАПОМИНАЛКА! Не забыть юзать вебхуки, настроить меню и команды со звонками.
import telebot
from telebot import types
TOKEN = '362352422:AAGKyG6HLhrYrDBe1MGDC3UKKHC_lfWWOUo'
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
# Добавляем команды
def start(m):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['Привет','Помощь', 'ДЗ', 'Олимпиады', 'Учителя', 'Мероприятия', 'ЕГЭ', 'СОС','Скучно','Факультатив','Парты','Столовая']])
    msg = bot.send_message(m.chat.id, 'Приветствую! Если хочешь узнать о работе со мной - выбери привет. Если желаешь узнать список команд - помощь.',
        reply_markup=keyboard)
    bot.register_next_step_handler(msg, name)
# НЕ ЗАБУДЬ ОТПРАВИТЬ НОВУЮ ВЕРСИЮ, А НЕ ЭТО!
# КОМАНДЫ - КНОПКАМИ
def name(m):
    if m.text == 'Привет':
        g = bot.send_message(m.chat.id, 'Приветствую!\nДорогой друг, меня зовут Ада и сейчас я кратко расскажу о себе.\nЯ специализированный чат-бот помощник для школьников, поэтому могу рассказать тебе самую актуальную и важную информацию по организации учебного процесса.\nКруглосуточно я могу тебе предоставить рассписание уроков,звонков и факультативов, домашнее задание и многое другое.\nЧтобы я тебе выдала информацию, то просто напиши ключевую команду мне в сообщении.\nЕсли ты хочешь узнать все мои команды - напиши "Помощь".\nА если ты узнаешь более актуальную информацию ( что мало вероятно ), то всегда жду твоего сообщения в группу - https://vk.com/10schoolbot10\nДо новых встреч!', parse_mode='Markdown') 
    elif m.text == 'СОС':
        g = bot.send_message(m.chat.id, 'Приветствую!\nМЧС России (пожарная охрана, спасатели) – 101\nПолиция – 102\nСкорая медицинская помощь – 103\nАварийная газовая служба - 104\nЕдиная служба спасения – 112\nСайт Школы - http://severschool10.ru/\nГосУслуги - https://51gosuslugi.ru/rpeu/', parse_mode='Markdown') 
    elif m.text == 'Столовая':
        g = bot.send_message(m.chat.id, 'Меню\nМУЧНЫЕ ИЗДЕЛИЯ\nПицца - 25 рублей\nПирожки с картофелем, капустой, луком и яйцом, мясом, шоколадом, печенью, яблоком - 15 рублей\nСосиска в тесте - 25 рублей\nСАЛАТЫ\nВинегрет; С картофелем, кукурузой и луком - 35 рублей\nС ветчиной, сыром и огурцом; Оливье - 45 рублей\nСУПЫ\nБорщ, Рассольник, Мясной и т.д. - 40 рублей(Зависит от дня недели)\nГОРЯЧЕЕ\nКотлеты мясные и рыбные, Голубцы и т.д - 60 рублей(Зависит от дня недели)\nНАПИТКИ\nЧай - 5 рублей\nЧай с лимоном - 7 рублей\nСок - 15 рублей\nКисель и Компот - 15 рублей\nКОМПЛЕКС\nСовмещает в себе порцию Горячего, Суп, Салат, Напиток - 70 рублей(Зависит от дня недели)', parse_mode='Markdown') 
    elif m.text == 'Парты':
        g = bot.send_message(m.chat.id, 'Приветствую!\nПервым пишется - 1 вариант, вторым - 2\n1 РЯД\n1 Парта\nЯровенко Н. , Кузнецов Д.\n2 Парта\nЗаболотникова Е. , Кагановский М.\n3 Парта\nКонстантинова С. , Паркин  М.\n4 Парта Мигрин Д. , Писанка Е.\n 5 Парта\nГладнева А. , Рубцов А.\n2 РЯД\n1 Парта\nЩурова Е. , Чоп А.\n2 Парта\nОрехова М. , Дробяско М.\n3 Парта\nБелый Я. , Мищенко Д.\n4 Парта\nВолобоев Р. , Воронина Е.\n5 Парта\nЗавершинский А. , Авраменко Е.\n6 Парта\nСамчук А. , Хецуриани М.\n3 РЯД\n1 Парта\nЛосева А. , Батин Е.\n2 Парта\nРакевич Ю. , Шендриков В.\n3 Парта\nШмелёва П. , Снеткова И.\n4 Парта\nЗнаменьщикова К. , Авоян А.\n6 Парта\nЖданова Ю. , Борисов В.' , parse_mode='Markdown') 
    elif m.text == 'Скучно':
        g = bot.send_message(m.chat.id, 'Приветствую!\nСоздание мультиков - http://multa.ch/\nСудоку - http://scanvord.net/sudoku/\n2048 - http://2048game.com/ru/\nШахматы - https://www.chess.com/ru/play/computer\nШашки - http://www.shashky.ru/', parse_mode='Markdown') 
    elif m.text == 'Факультатив':
        g = bot.send_message(m.chat.id, 'Факультатив по Информатике:\nПонедельник - 5 урок\nСреда - 7 урок', parse_mode='Markdown')    
    elif m.text == 'Помощь':
        g = bot.send_message(m.chat.id, 'СКУЧНО - предложу развивающие и познавательные игры\nОЛИМПИАДА - скажу запланированные олимпиады\nФАКУЛЬТАТИВ - скажу запланированные факультативы\nМЕНЮ - выдам цены на питание в школьной столовой.\nМЕСТА - скажу на какой парте и каком варианте сидит ученик.\nУЧИТЕЛЯ - покажу список учителей\nПОМОЩЬ - покажу список команд\nМЕРОПРИЯТИЯ - скажу запланированные мероприятия\nДЗ - скажу домашнее задание\nЕГЭ - выдам информацию по егэ\nПривет - информация о аде\nСОС - покажу важные ссылки', parse_mode='Markdown')
    elif m.text == 'ДЗ':
        g = bot.send_message(m.chat.id, 'НИЧЕГО', parse_mode='Markdown')
    elif m.text == 'Олимпиады':
        g = bot.send_message(m.chat.id, '20.11.2017 - Литература, Физика.\n21.11.2017 - Обществознание.\n22.11.2017 - Математика.\n23.11.2017 - Биология, Информатика и ИКТ.\n24.11.2017 - Русский язык.\n25.11.2017 - Французский язык, География.\n27.11.2017 - Английский язык(Теоретический тур).\n28.11.2017 - Английский язык(Практичесий тур).\n29.11.2017 - Астраномия, История.\n30.11.2017 - Немецкий язык, Право.\n01.12.2017 - МХК, Химия.\n07.12.2017 - Экология, Технология(Теоретические туры).\n08.12.2017 - Экология, Технология(Практические туры).', parse_mode='Markdown')
    elif m.text == 'Учителя':
        g = bot.send_message(m.chat.id, 'Русский яз.; Литература  - Рожкова Елена Викторовна\nМатематика - Попова Светлана Вячеславовна\nФизика - Гасымова Анжелика Евгеньевна\nХимия - Кокорина Светлана Евгеньевна\nИнформатика - Кузьмин Евгений Александрович\nИстория; Обществознание - Канатова Ирина Ивановна\nБиология - Капитанчук Юлия Сергеевна\nГеогрфия - Пухлова Любовь Викторовна\nАнглийский яз. - Бородина Елена Валерьевна\nФизкультура - Картавова Альфия Вагизовна\nМузыка  - Петросян Алла Рафаеловна\nОБЖ - Колбеев Владимир Владимирович', parse_mode='Markdown')
    elif m.text == 'Мероприятия':
        g = bot.send_message(m.chat.id, 'На данный момент мероприятий не запланировано', parse_mode='Markdown')
    elif m.text == 'ЕГЭ':
        g = bot.send_message(m.chat.id, 'Решу ЕГЭ - https://ege.sdamgia.ru/\nЯндекс ЕГЭ - https://ege.yandex.ru/ege/\nПолезная Информация - http://www.ege.edu.ru/ru/main/', parse_mode='Markdown')
    bot.register_next_step_handler(g, name)    
bot.polling()
# Напоминание!!! Не забыть вставить веб-хуки в конечную версию

#Попытка реализации звонков
#def get_time_before_ring(time_now):
    #key_day, lesson_now, is_time_change = get_lesson_number(time_now)
    #if lesson_now == 'before':
        #td_first_lesson = timedelta(
            #hours=TIMETABLE[key_day][SHIFT][0][1].hour,
            #minutes=TIMETABLE[key_day][SHIFT][0][1].minute)
        #minute_before = td_first_lesson - time_now.td
        #message = 'Уроки ещё не начались, до начала {0}:{1}'.\
                  #format(minute_before.seconds//3600,
                         #str(minute_before.seconds%3600//60).zfill(2))
    #elif lesson_now == 'after':
        #td_last_lesson = timedelta(
            #hours=TIMETABLE[key_day][SHIFT][-1][2].hour,
            #minutes=TIMETABLE[key_day][SHIFT][-1][2].minute)
        #minute_before = time_now.td - td_last_lesson
        #message = 'Уроки уже прошли. {0} закончился {1}:{2} назад'.\
                  #format(TIMETABLE[key_day][SHIFT][-1][0],
                         #minute_before.seconds//3600,
                         #str(minute_before.seconds%3600//60).zfill(2))
    #else:
        #if is_time_change:
            #next_lesson = TIMETABLE[key_day][SHIFT][lesson_now + 1]
            #td_next_lesson_beg = timedelta(
                #hours=next_lesson[1].hour,
                #minutes=next_lesson[1].minute)
            #minute_before = td_next_lesson_beg - time_now.td
            #message = '{} завершен. Перемена, до звонка {} минут'.\
                      #format(TIMETABLE[key_day][SHIFT][lesson_now][0],
                             #minute_before.seconds//60)
        #else:
            #td_lesson_end = timedelta(
                #hours=TIMETABLE[key_day][SHIFT][lesson_now][2].hour,
                #minutes=TIMETABLE[key_day][SHIFT][lesson_now][2].minute)
            #minute_before = td_lesson_end - time_now.td
            #message = 'Идёт "{}", до звонка {} минут'.\
                      #format(TIMETABLE[key_day][SHIFT][lesson_now][0].title(),
                             #minute_before.seconds//60)
    #return message


#def get_daily_timetable(time_now, day):
   #if day == time_now.week_day:
      #key_day, lesson_now, is_time_change = get_lesson_number(time_now)
   #else:
      #lesson_now = None
   #for key_day in TIMETABLE:
      #if day in key_day:
         #message = DAYS_NAME[day].upper() + '\n'
         #if lesson_now == 'before':
            #message += 'СЕЙЧАС {0:%H}:{0:%M}\n'.format(time_now.time)
         #for n, lesson in enumerate(TIMETABLE[key_day][SHIFT]):
             #message += '{0}: {1:%H}:{1:%M} - {2:%H}:{2:%M}\n'.\
                        #format(lesson[0], lesson[1], lesson[2])
             #if lesson_now == n:
                #if is_time_change:
                   #message += 'СЕЙЧАС {0:%H}:{0:%M}\n'.format(time_now.time)
                #else:
                   #message = message[:-1] + \
                             #', СЕЙЧАС {0:%H}:{0:%M}\n'.format(time_now.time)
         #if lesson_now == 'after':
            #message += 'СЕЙЧАС {0:%H}:{0:%M}\n'.format(time_now.time)
   #return message


#def get_timetable(keyword=''):
   #time_now = TimeNow()
   #if keyword in keyword_gen('звонки сегодня','звонки на сегодня','звнксгд'):
      #message = get_daily_timetable(time_now, time_now.week_day)
   #elif keyword in keyword_gen('звонки завтра','звонки на завтра','звнкзвт'):
      #message = get_daily_timetable(time_now, time_now.week_day+1)
   #elif keyword in keyword_gen('звонки вчера', 'звонки на вчера', 'звнквчр'):
      #message = get_daily_timetable(time_now, time_now.week_day-1)
   #elif keyword in keyword_gen('звонки понедельник','звонки на понедельник','звнкпн'):
      #message = get_daily_timetable(time_now, 0)
   #elif keyword in keyword_gen('звонки вторник','звонки на вторник','звнквт'):
      #message = get_daily_timetable(time_now, 1)
   #elif keyword in keyword_gen('звонки среда','звонки на среду','звнкср'):
      #message = get_daily_timetable(time_now, 2)
   #elif keyword in keyword_gen('звонки четверг','звонки на четверг','звнкчт'):
      #message = get_daily_timetable(time_now, 3)
   #elif keyword in keyword_gen('звонки пятница','звонки на пятницу','звнкпт'):
      #message = get_daily_timetable(time_now, 4)
   #elif keyword in keyword_gen('звонки суббота','звонки на субботу','звнксб'):
      #message = get_daily_timetable(time_now, 5)
   #elif keyword in keyword_gen('звонки воскресенье','звонки на восткресенье','звнквс'):
      #message = get_daily_timetable(time_now, 6)
   #else:
      #message = get_time_before_ring(time_now)
   #return message, ''


#timetable_command = command_system.Command()
#timetable_command.keys =  keyword_gen('звонок','до звонка','звнк', 'pdjyjr',
                                     #'звонки сегодня','звонки на сегодня','звнксгд','pdjyrb yf ctujlyz',
                                     #'звонки завтра','звонки на завтра','звнксгд', 'pdjyrb yf pfdnhf',
                                     #'звонки вчера', 'звонки на вчера', 'звнквчр', 'pdjyrb yf dxthf',
                                     #'звонки понедельник','звонки на понедельник','звнкпн', 'pdjyrb yf gjytltkmybr',
                                     #'звонки вторник','звонки на вторник','звнквт', 'pdjyrb yf dnjhybr',
                                     #'звонки среда','звонки на среду','звнкср', 'pdjyrb yf chtle',
                                     #'звонки четверг','звонки на четверг','звнкчт', 'pdjyrb yf xtndthu',
                                     #'звонки пятница','звонки на пятницу','звнкпт', 'pdjyrb yf gznybwe',
                                     #'звонки суббота','звонки на субботу','звнксб', 'pdjyrb yf ce,,jne',
                                     #'звонки воскресенье','звонки на восткресенье','звнквс','pdjyrb yf pfdnhf')
#timetable_command.description = '''Скажу расписание звонков на вчера/сегодня/завтра/пн/вт/ср/чт/пт/сб/вс, либо сколько осталось до звонка'''
#timetable_command.process = get_timetable
#Расписание
#def get_daily_schedule(week_day):
    #lessons = DAYS_NAME[week_day].upper() + ':\n'
    #for lesson in SCHEDULE[week_day]:
        #subject = "ПУСТО" if lesson[1] == '' else lesson[1]
        #lessons += '{}. {}\n'.format(lesson[0], subject)
    #return lessons

#def get_schedule(keyword=''):
    #time_now = TimeNow()
    #if keyword in keyword_gen('расписание','расп'):
        #message = '\n\n'.join([get_daily_schedule(week_day) for week_day in range(7)])
    #elif keyword in keyword_gen('расписание на сегодня', 'расписание сегодня', 'распсгд'):
        #message = get_daily_schedule(time_now.week_day)
    #elif keyword in keyword_gen('расписание на завтра','расписание завтра','распзвт'):
        #message = get_daily_schedule((time_now.week_day + 1) % 7)
    #elif keyword in keyword_gen('расписание на вчера','расписание вчера','распвчр'):
        #message = get_daily_schedule((time_now.week_day - 1) % 7)
    #elif keyword in keyword_gen('расписание на понедельник','расписание понедельник','расппн'):
        #message = get_daily_schedule(0)
    #elif keyword in keyword_gen('расписание на вторник','расписание вторник','распвт'):
        #message = get_daily_schedule(1)
    #elif keyword in keyword_gen('расписание на среду','расписание среда','распср'):
        #message = get_daily_schedule(2)
    #elif keyword in keyword_gen('расписание на четверг','расписание четверг','распчт'):
        #message = get_daily_schedule(3)
    #elif keyword in keyword_gen('расписание на пятницу','расписание пятница','расппт'):
        #message = get_daily_schedule(4)
    #elif keyword in keyword_gen('расписание на субботу','расписание суббота','распсб'):
        #message = get_daily_schedule(5)
    #elif keyword in keyword_gen('расписание на воскресенье','расписание воскресенье','распвс'):
        #message = get_daily_schedule(6)
    #else:
        #message = ' sorry...'
    #return message, ''


#schedule_command = command_system.Command()
#schedule_command.keys = keyword_gen('расписание','расп', 'hfcgbcfybt', 'hfcg',
                                    #'расписание на сегодня', 'расписание сегодня', 'распсгд', 'hfcgbcfybt yf ctujlyz', 'hfcg yf ctujlyz',
                                    #'расписание на завтра','расписание завтра','распзвт', 'hfcgbcfybt yf pfdnhf', 'hfcg yf pfdnhf',
                                    #'расписание на вчера','расписание вчера','распвчр', 'hfcgbcfybt yf dxthf', 'hfcg yf dxthf',
                                    #'расписание на понедельник','расписание понедельник','расппн', 'hfcgbcfybt yf gjytltkmybr', 'hfcg yf gjytltkmybr',
                                    #'расписание на вторник','расписание вторник','распвт', 'hfcgbcfybt yf dnjhybr', 'hfcg yf dnjhybr',
                                    #'расписание на среду','расписание среда','распср', 'hfcgbcfybt yf chtle', 'hfcg yf chtle',
                                    #'расписание на четверг','расписание четверг','распчт', 'hfcgbcfybt yf xtndthu', 'hfcg yf xtndthu',
                                    #'расписание на пятницу','расписание пятница','расппт', 'hfcgbcfybt yf gznybwe', 'hfcg yf gznybwe',
                                    #'расписание на субботу','расписание суббота','распсб', 'hfcgbcfybt yf ce,,jne', 'hfcg yf ce,,jne',
                                    #'расписание на воскресенье','расписание воскресенье','распвс','hfcgbcfybt yf djcrhtctymt', 'hfcg yf djcrhtctymt',)
#schedule_command.description = 'Скажу расписание уроков на вчера/сегодня/завтра/пн/вт/ср/чт/пт/сб/вс, либо на всю неделю'
#schedule_command.process = get_schedule