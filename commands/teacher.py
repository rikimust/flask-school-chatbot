import command_system
from common_func import keyword_gen

def teacher(keyword=''):
   message = 'Приветствую!\nРусский яз.; Литература  - Рожкова Елена Викторовна\nМатематика - Попова Светлана Вячеславовна\nФизика - Гасымова Анжелика Евгеньевна\nХимия - Кокорина Светлана Евгеньевна\nИнформатика - Кузьмин Евгений Александрович\nИстория; Обществознание - Канатова Ирина Ивановна\nБиология - Капитанчук Юлия Сергеевна\nГеогрфия - Пухлова Любовь Викторовна\nАнглийский яз. - Бородина Елена Валерьевна\nФизкультура - Картавова Альфия Вагизовна\nМузыка  - Петросян Алла Рафаеловна\nОБЖ - Колбеев Владимир Владимирович'
   return message, ''

teacher_command = command_system.Command()
teacher_command.keys = keyword_gen('учителя','преподаватели', 'преподы')
teacher_command.description = 'Покажу список учителей'
teacher_command.process = teacher