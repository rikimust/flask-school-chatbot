import csv
from flask import render_template
from collections import namedtuple

link = namedtuple('Link', ['name', 'addr'])

logo_name = 'чатбот АДА'
title = 'Ада - школьный чатбот'
group_10a = link("10А физ-мат", "https://vk.com/10schoolbot10")
group_10b = link("10Б соц-эконом", "https://vk.com/school10_soceconom")
developer = link("Чоп Александр", "https://vk.com/rikimust")
sci_adviser = link("Кузьмин Евгений", "https://vk.com/eakuzmin")
main_menu = (
    link('Главная', '\\'),
    link('Информация', '\info'),
    link('Логи', '\log'))
greetings = {
    "title": 'Привет, я АДА - чатбот помощник для школьника!',
    "msg": '''
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
                           the_greetings_title=greetings["title"],
                           the_greetings_msg=greetings["msg"],
                           the_group=group_10b,
                           the_developer=developer,
                           the_sci_advisor=sci_adviser)


def info_page() -> 'html':
    return render_template('info.html',
                           the_title='Это основная информация',
                           the_logo_name=logo_name,
                           the_main_menu=main_menu,
                           the_developer=developer,
                           the_sci_advisor=sci_adviser)


def log_page(filename: str='requests.log') -> 'html':
    with open(filename, encoding='utf-8') as log:
        reader = csv.DictReader(log, delimiter=';')
        log_req = []
        for n, line in enumerate(reader):
            log_req.append(line)
    return render_template('log.html',
                           the_data=log_req,
                           the_req_count=n,
                           the_title='Это лог',
                           the_logo_name=logo_name,
                           the_main_menu=main_menu,
                           the_developer=developer,
                           the_sci_advisor=sci_adviser)

