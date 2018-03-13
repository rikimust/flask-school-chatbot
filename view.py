import csv, os
from flask import render_template
from collections import namedtuple

cur_dir = os.path.dirname(os.path.abspath(__file__))
link = namedtuple('Link', ['name', 'addr'])

logo_name = 'школьный чатбот'
title = 'Ада - школьный чатбот'
group_10a = link("10А физ-мат", "https://vk.com/10schoolbot10")
group_10b = link("10Б соц-эконом", "https://vk.com/school10_soceconom")
developer = link("Чоп Александр", "https://vk.com/rikimust")
sci_adviser = link("Кузьмин Евгений", "https://vk.com/eakuzmin")
main_menu = (
    link('Главная', '\\'),
    link('Информация', '\info'),
    link('Команды', '\commands'),
    link('Логи', '\log'))
greetings = {
    "title": 'Привет, я АДА - чатбот помощник для школьника!',
    "msg": r'''
С моей помощью ты можешь узнать актуальную информацию об
обучении, а именно расписание уроков, звонки, сведения об учителях
и многое другое. Я обработую твое сообщение мгновенно, предоставив
ответ, относительно текущего времени. Со мной ты всегда будешь в курсе
того, сколько времени осталось до звонка, какой следующий урок,
расписания на завтра (или на любой день недели).
'''}


def index_page() -> 'html':
    return render_template('index.html',
                           the_title=title,
                           the_logo_name=logo_name,
                           the_main_menu=main_menu,
                           the_active_page=1,
                           the_greetings_title=greetings["title"],
                           the_greetings_msg=greetings["msg"],
                           the_group=group_10b,
                           the_developer=developer,
                           the_sci_advisor=sci_adviser)


def info_page() -> 'html':
    return render_template('info.html',
                           the_title='''
                           Здесь будет информация, которой владеет чатбот
                           (расписание уроков, расписание звонков, учителя, ...)
                           ''',
                           the_logo_name=logo_name,
                           the_main_menu=main_menu,
                           the_active_page=2,
                           the_developer=developer,
                           the_sci_advisor=sci_adviser)


def commands_page() -> 'html':
    return render_template('info.html',
                           the_title='Здесь будет описание команд',
                           the_logo_name=logo_name,
                           the_main_menu=main_menu,
                           the_active_page=3,
                           the_developer=developer,
                           the_sci_advisor=sci_adviser)


def log_page(page, filename: str=os.path.join(cur_dir, 'requests.log')) -> 'html':
    with open(filename, encoding='utf-8') as log:
        reader_dict = csv.DictReader(log, delimiter=';')
        log_req = []
        act_usr_dict = dict()
        pop_req_dict = dict()
        for line in reader_dict:
            pop_req_dict[line['body']] = \
                pop_req_dict.get(line['body'], 0) + 1
            act_usr_dict[line['name']] = \
                act_usr_dict.get(line['name'], 0) + 1
            log_req.append(line)
    log_req.reverse()
    active_users = []
    for user, count in sorted(act_usr_dict.items(),
                              key=lambda x: x[1],
                              reverse=True):
        active_users.append((user, count))
        if len(active_users) >= 15:
            break
    popular_requests = []
    for request, count in sorted(pop_req_dict.items(),
                              key=lambda x: x[1],
                              reverse=True):
        popular_requests.append((request, count))
        if len(popular_requests) >= 15:
            break
    page = len(log_req) // 25 if page == 'last' else int(page)
    begin = (len(log_req) // 25 - page) * 25
    end = (len(log_req) // 25 - page + 1) * 25
    if page == 1:
        end = len(log_req)
    return render_template('log.html',
                           the_page=page,
                           the_data=log_req[begin:end],
                           the_row_on_page=25,
                           the_req_count=len(log_req),
                           the_active_users=active_users,
                           the_popular_requests=popular_requests,
                           the_title='Это лог',
                           the_logo_name=logo_name,
                           the_main_menu=main_menu,
                           the_active_page=4,
                           the_developer=developer,
                           the_sci_advisor=sci_adviser)
