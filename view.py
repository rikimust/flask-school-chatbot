from flask import render_template

group_10a = {"name": "10А физ-мат", "address": "https://vk.com/10schoolbot10"}
group_10b = {"name": "10Б соц-эконом", "address": "https://vk.com/school10_soceconom"}
developer = {"name": "Чоп Александр", "address": "https://vk.com/rikimust"}
sci_adviser = {"name": "Кузьмин Евгений", "address": "https://vk.com/eakuzmin"}
logo_name = 'чатбот АДА'
main_menu = ('Главная', 'Информация', 'Логи')
greetings = {
    "title":'Привет, я АДА - чатбот помощник для школьника!',
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
                           the_title="Ада - школьный чатбот",
                           the_logo_name=logo_name,
                           the_main_menu=main_menu,
                           the_greetings_title=greetings["title"],
                           the_greetings_msg=greetings["msg"],
                           the_group_name=group_10b["name"],
                           the_group_addr=group_10b["address"],
                           the_developer_name=developer["name"],
                           the_developer_addr=developer["address"],
                           the_sci_advisor_name=sci_adviser["name"],
                           the_sci_advisor_addr=sci_adviser["address"])
