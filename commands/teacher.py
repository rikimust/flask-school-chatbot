import command_system
from common_func import keyword_gen

def teacher(keyword=''):
   message = '''Приветствую!
   Русский яз.; Литература  - Рожкова Елена Викторовна
   Математика - Попова Светлана Вячеславовна
   Физика - Гасымова Анжелика Евгеньевна
   Химия - Кокорина Светлана Евгеньевна
   Информатика - Кузьмин Евгений Александрович
   История; Обществознание - Канатова Ирина Ивановна
   Биология - Капитанчук Юлия Сергеевна
   Геогрфия - Пухлова Любовь Викторовна
   Английский яз. - Бородина Елена Валерьевна
   Физкультура - Картавова Альфия Вагизовна
   Музыка  - Петросян Алла Рафаеловна\nОБЖ - Колбеев Владимир Владимирович'''
   return message, ''

teacher_command = command_system.Command()
teacher_command.keys = keyword_gen('учителя','преподаватели', 'преподы')
teacher_command.description = 'Покажу список учителей'
teacher_command.process = teacher
