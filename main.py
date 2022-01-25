import pygame
import os
import sys
import datetime
import time
import random


# Функция загрузки изображений
def load_image(name, colorkey=None):
    fullname = os.path.join('img', name)  # Обработка названия файла
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()  # Выход из системы
    image = pygame.image.load(fullname)  # Объявление перменной, в которой содержится изоюбражение
    return image  # возврат изображения в переменную 'img_...'


pygame.init()  # Инициализация библиотеки pygame
pygame.font.init()  # Инициализация шрифтов

window = pygame.display.set_mode((1280, 720), pygame.NOFRAME)  # Создаём окно без верхних рамок
pygame.display.set_caption("MIHALIN")  # Устанавливаем название окна

screen = pygame.Surface((1280, 720))  # Создаём поверхность экрана

curs = pygame.Surface((72, 84))  # Создаём поверхность курсора

banana = pygame.Surface((476, 322))  # Создаём поверхность банана

arrow = pygame.Surface((150, 150))  # Создаём поверхность стрелки назад

order = pygame.Surface((50, 70))  # Создаём поверхность чека с заказом

bgorder = pygame.Surface((350, 490))  # Создаём поверхность чека в его полном размере

img_curs = load_image("cursor22.png")  # Загружаем изображение курсора через функцию load_image

# В следующих 5 строчках создаётся поверхность перцев

pp1 = pygame.Surface((86, 90))
pp2 = pygame.Surface((86, 90))
pp3 = pygame.Surface((86, 90))
pp4 = pygame.Surface((86, 90))
pp5 = pygame.Surface((86, 90))

beef1 = pygame.Surface((86, 60))  # Создаём поверхность сырого мяса
pasta1 = pygame.Surface((63, 100))  # Создаём поверхность упаковки пасты
soda_bottle = pygame.Surface((41, 120))  # Создаём поверхность бутылки газировки

crest = pygame.Surface((64, 64))  # Создаём поверхность крестика

pan = pygame.Surface((128, 128))  # Создаём поверхность кастрюли
skovoroda = pygame.Surface((256, 256))  # Создаём поверхность сковороды

plate1 = pygame.Surface((256, 256))  # Создаём поверхность тарелки

r_pasta = pygame.Surface((256, 256))  # Создаём поверхность готовой пасты
r_beef = pygame.Surface((128, 128))  # Создаём поверхность готового мяса

od = 0

done = False  # Флаг, работающий, пока работает программа

# В следующих строках добавляются изображения через функцию load_image (строка 10)
img_order1 = load_image("order1.png")  # Загрузка изображения заказа_1
img_order2 = load_image("order2.png")  # Загрузка изображения заказа_2
img_order3 = load_image("order3.png")  # Загрузка изображения заказа_3
img_order4 = load_image("order4.png")  # Загрузка изображения заказа_4
img_order5 = load_image("order5.png")  # Загрузка изображения заказа_5
img_bgorder = load_image("bg_order.png")  # Загрузка изображения большого заказа
img_screen = load_image("start-screen11.png")  # Загрузка изображения стартового экрана
img_days = load_image("days_fon.png")  # Загрузка изображения фона второго экрана
img_banana = load_image("banana.png")  # Загрузка изображения банана
img_arrow = load_image("arrow.png")  # Загрузка изображения стрелки назад
img_pap = load_image("red_papper.png")  # Загрузка изображения перца
img_kitch = load_image("table.png")  # Загрузка изображения экрана кухни
# img_empt_pap = load_image("empty_papper.png")
img_freege = load_image("freege2.png")  # Загрузка изображения холодильника
img_beef1 = load_image("beef_notfry.png")  # Загрузка изображения сырого мяса
img_pasta1 = load_image("pasta.png")  # Загрузка изображения упаковки пасты
img_bottle = load_image("soda.png")  # Загрузка изображения бутылки газировки
img_crest = load_image("crest.png")  # Загрузка изображения крестика
img_pan = load_image("pan.png")  # Загрузка изображения кастрюли
img_plate = load_image("plate.png")  # Загрузка изображения тарелки
img_skovoroda = load_image("skovoroda.png")  # Загрузка изображения сковородки
img_rpasta = load_image("r_pasta.png")  # Загружаем изображение готовой пасты
img_rbeef = load_image("r_beef.png")
img_cong = load_image('cong.png')

myfont = pygame.font.SysFont('SW Crawl Title', 60)  # Загрузка шрифта "SW Crawl Title" в разм мере 60
myfont2 = pygame.font.SysFont('SW Crawl Title', 30)  # Загрузка шрифта "SW Crawl Title" в размере 30
notefont = pygame.font.SysFont('Segoe Script', 20)  # Загрузка шрифта "Segoe Script" в размере 20
bnotefont = pygame.font.SysFont('Segoe Script', 150)  # Загрузка шрифта "Segoe Script" в размере 150

st_sc = True  # Флаг срабатывания стартового экрана (По умолчанию равен истине)
d_sc = False  # Флаг срабатывания экрана выбора дня
k_sc = False  # Флаг срабатывания экрана кухни
f_sc = False  # Флаг срабатывания экрана холодильника
ord_flag = False  # Флаг срабатывания заказа
bg_ord_flag = False  # Флаг срабатывания большого заказа
ch_obj = ''  # Выбранный объект
readiness = myfont.render('', False, (0, 255, 0))  # Текст готовности заказа
in_pan = None  # Предмет в кастрюли (По умолчанию - пусто)
in_skv = None
in_plate = ''

score = 0

lvl = 1  # Уровень игры (По умолчанию - 1)

ch_d = 1  # Выбранный день

sp = []  # Список. По умолчанию - пустой. Используется для подсчёта времени
sp2 = []  # Список_2. По умолчанию - пустой. Используется для подсчёта времени
random_sp = []  # Список, в который добавляется случайное число от 1 до 5. Используется для создания чеков.

ordr = 1  # Выполняемый заказ. По умолчанию равен 1

x_p = 5  # Координата курсора по оси x
y_p = 360  # Координата курсора по оси y

x_rpasta = 100000  # Координата готовой пасты по оси x
y_rpasta = 100000  # Координата готовой пасты по оси y

x_rbeef = 10000
y_rbeef = 10000

x_plate = 550
y_plate = 380

plate_pos = 'DOWN'

days = 1  # Количество "открытых" дней. По умолчанию равно 1.

plates_count = 3  # Количество тарелок в текущий момент на столе.

# В следующих строках (___ - ___) мы избавляемся от фона изображения
curs.set_colorkey((0, 255, 0))  # Обработка фона курсора
banana.set_colorkey((0, 0, 255))  # Обработка фона банана
arrow.set_colorkey((0, 0, 0))  # Обработка фона стрелки
pp1.set_colorkey((0, 0, 0))  # Обработка фона перца
order.set_colorkey((0, 255, 0))  # Обработка фона заказа
bgorder.set_colorkey((0, 255, 0))  # Обработка фона большого заказа
beef1.set_colorkey((0, 255, 0))  # Обработка фона сырого мяса
pasta1.set_colorkey((0, 255, 0))  # Обработка фона пасты
soda_bottle.set_colorkey((0, 255, 0))  # Обработка фона бутылки газировки
crest.set_colorkey((255, 255, 255))  # Обработка фона крестика
pan.set_colorkey((0, 255, 0))  # Обработка фона кастрюли
plate1.set_colorkey((0, 255, 0))  # Обработка фона тарелки_1
skovoroda.set_colorkey((0, 255, 0))  # Обработка фона сковородки
r_pasta.set_colorkey((0, 255, 0))
r_beef.set_colorkey((0, 255, 0))

bg_x = 1000000  # Расположение большого заказа по оси x. По умолчанию находится за границами программы.
bg_y = 1000000  # Расположение большого заказа по оси y. По умолчанию находится за границами программы.

while done == False:  # Пока программа работает:
    for e in pygame.event.get():  # Обработка каждого события
        if e.type == pygame.QUIT:  # Если событие - выйти
            done = True  # Флаг, работающий, пока работает программа, меняет значение => программа перестаёт работать

        if pygame.mouse.get_focused():  # Если курсор находится в пределах окна:
            x_p, y_p = pygame.mouse.get_pos()  # 1 - Координата курсора по оси x. 2 - Координата курсора по оси y
        else:  # В ином случае
            x_p, y_p = -1000, -1000  # Курсор будет распологаться за пределами окна

        if e.type == pygame.MOUSEBUTTONUP and e.button == 1:  # При нажатии левой кнопки мыши:
            pos = pygame.mouse.get_pos()  # "pos" - это позиция мыши по оси x; y
            if pos > (507, 297) and pos < (708, 391) and st_sc:  # Если нажата кнопка "start":
                d_sc = True  # Активирование экрана выбора дня
                st_sc = False  # Закрытие стартового экрана
            if pos > (1040, 641) and pos < (1124, 686) and st_sc:  # Если нажата кнопка "Выключить":
                done = True  # Флаг, работающий, пока работает программа, меняет значение => программа перестаёт работать

            if pos > (10, 10) and pos < (160, 160) and d_sc:  # Если нажата кнопка "назад" (стрелочка)
                st_sc = True  # Активирование стартового экрана
                d_sc = False  # Закрытие экрана выбора дня

            if pos[0] >= 555 and pos[1] >= 598 and pos[0] <= 686 and pos[1] <= 638:  # Если нажать кнопку старт_2:
                k_sc = True  # Активирование экрана кухни
                d_sc = False  # Закрытие экрана выбора дня

            if pos[0] >= 205 and pos[1] >= 96 and pos[0] <= 374 and pos[1] <= 141:  # Если выбрать "День 1"
                ch_d = 1  # Выбранный день - 1

            if pos[0] >= 407 and pos[1] >= 92 and pos[0] <= 576 and pos[1] <= 131:  # Если выбрать "День 2"
                if days >= 2:  # Если возможно выбрать 2 дня:
                    ch_d = 2  # Выбранный день - 2

            if pos[0] >= 612 and pos[1] >= 98 and pos[0] <= 774 and pos[1] <= 128:  # Если выбрать "День 3"
                if days >= 3:  # Если возможно выбрать 3 дня:
                    ch_d = 3  # Выбранный день - 3

            if pos[0] >= 814 and pos[1] >= 98 and pos[0] <= 971 and pos[1] <= 130:  # Если выбрать "День 4"
                if days >= 4:  # Если возможно выбрать 4 дня:
                    days = 4  # Выбранный день - 4

            if pos[0] >= 1013 and pos[1] >= 97 and pos[0] <= 1176 and pos[1] <= 132:  # Если выбрать "День 5"
                if days >= 5:  # Если возможно выбрать 5 дня:
                    days = 5  # Выбранный день - 5

            # Если нажать на кнопку заказа:
            if pos[0] >= 602 and pos[1] >= 96 and pos[0] <= 666 and pos[1] <= 162 and ord_flag and not bg_ord_flag:
                bg_x = 465  # Координата заказа в полном размере по оси x
                bg_y = 105  # Координата заказа в полном размере по оси y

            if (pos[0] >= 495 and pos[1] >= 72 and pos[0] <= 601 and pos[1] <= 177) \
                    or pos[0] >= 664 and pos[1] >= 68 and pos[0] <= 757 and pos[1] <= 177:
                if k_sc and ch_obj == 'Газировка':
                    ch_obj = ''
                    od += 30_001

            # Если убрать большой заказ
            if pos[0] >= 655 and pos[1] >= 163 and pos[0] <= 710 and pos[1] <= 206 and ord_flag and not bg_ord_flag:
                bg_x = 1000000  # Координата заказа в полном размере по оси x
                bg_y = 1000000  # Координата заказа в полном размере по оси y

            print(pos)
            if pos[0] >= 1 and pos[1] >= 1 and pos[0] <= 298 and pos[1] <= 419 and k_sc:  # Если нажать на холодильник
                f_sc = True  # Активирование экрана холодильника
                k_sc = False  # Закрытие экрана кухни

            # Если закрыть экран холодильника
            if pos[0] >= 1157 and pos[1] >= 8 and pos[0] <= 1229 and pos[1] <= 75 and f_sc:
                k_sc = True  # Активирование экрана кухни
                f_sc = False  # Закрытие экрана холодильника

            if pos[0] >= 460 and pos[1] >= 246 and pos[0] <= 552 and pos[1] <= 307 and f_sc:  # Если нажать на мясо
                ch_obj = "Мясо"  # Выбранный объект - мясо
                print(ch_obj)

            if pos[0] >= 549 and pos[1] >= 407 and pos[0] <= 611 and pos[1] <= 543 and f_sc:  # Если нажать на бутылку
                ch_obj = "Газировка"  # Выбранный объект - газировка
                print(ch_obj)

            if pos[0] >= 654 and pos[1] >= 438 and pos[0] <= 735 and pos[1] <= 547 and f_sc:  # Если нажать на пасту
                ch_obj = "Паста"  # Выбранный объект - паста
                print(ch_obj)

            if pos[0] >= 668 and pos[1] >= 214 and pos[0] <= 788 and pos[1] <= 313 and k_sc:  # Если нажать на кастрюлю
                if ch_obj == 'Паста':  # Если выбранный объект - паста
                    readiness = myfont.render('ЗАБИРАЙТЕ', False, (255, 255, 0))  # В переменную готовности заказа ...
                    # ... вносится значение "ЗАБИРАЙТЕ"
                    time.sleep(3)  # Приостановка программы на 3 секунды (Приготовление блюда)
                    ch_obj = ''  # В руках предмет пропадает
                    in_pan = "Гот. Паста"  # В кастрюле появляется готовая паста
                elif ch_obj == '':  # Если предмет не выбран, ничего не происходит
                    if in_pan != '':  # Если кастрюля не пустая
                        ch_obj, in_pan = in_pan, ch_obj  # Выбранный объект и объект в кастрюле меняются местами
                        readiness = myfont.render('', False, (255, 255, 0))  # Текст меняется, т.к мы взяли объект
                    else:
                        print('выберите предмет')

            if pos[0] >= 510 and pos[1] >= 456 and pos[0] <= 763 and pos[1] <= 539 and k_sc:
                if ch_obj == "Гот. Паста":
                    in_plate = "Гот. Паста"
                    ch_obj = ''
                    x_rpasta = 550
                    y_rpasta = 380

                if ch_obj == 'Стейк':
                    in_plate = 'Стейк'
                    ch_obj = ''
                    x_rbeef = 630
                    y_rbeef = 430

            if pos[0] >= 372 and pos[1] >= 251 and pos[0] <= 621 and pos[1] <= 322 and k_sc:
                if ch_obj == 'Мясо':
                    readiness = myfont.render('ЗАБИРАЙТЕ', False, (255, 255, 0))  # В переменную готовности заказа ...
                    # ... вносится значение "ЗАБИРАЙТЕ"
                    time.sleep(5)  # Приостановка программы на 3 секунды (Приготовление блюда)
                    ch_obj = ''  # В руках предмет пропадает
                    in_skv = "Стейк"  # В сковороде появляется готовое мясо

                elif ch_obj == '':  # Если предмет не выбран, ничего не происходит
                    if in_skv != '':  # Если кастрюля не пустая
                        ch_obj, in_skv = in_skv, ch_obj  # Выбранный объект и объект в сковородке меняются местами
                        readiness = myfont.render('', False, (255, 255, 0))  # Текст меняется, т.к мы взяли объект
                    else:
                        print('выберите предмет')

        if e.type == pygame.MOUSEBUTTONUP and e.button == 3:
            pos = pygame.mouse.get_pos()  # "pos" - это позиция мыши по оси x; y
            if pos[0] >= 523 and pos[1] >= 451 and pos[0] <= 771 and pos[
                1] <= 543 and k_sc and in_plate == 'Гот. Паста':
                if plate_pos == 'DOWN':
                    plate_pos = 'UP'
                    y_plate = 75
                    y_rpasta = 75
                    od += 10_001

            if pos[0] >= 514 and pos[1] >= 150 and pos[0] <= 767 and pos[
                1] <= 230 and k_sc and in_plate == 'Гот. Паста':
                if plate_pos == 'UP':
                    plate_pos = 'DOWN'
                    y_plate = 380
                    y_rpasta = 10000

            if pos[0] >= 523 and pos[1] >= 451 and pos[0] <= 771 and pos[1] <= 543 and k_sc and in_plate == 'Стейк':
                if plate_pos == 'DOWN':
                    plate_pos = 'UP'
                    y_plate = 75
                    y_rbeef = 100
                    od += 20_001

            if pos[0] >= 514 and pos[1] >= 150 and pos[0] <= 767 and pos[1] <= 230 and k_sc and in_plate == 'Стейк':
                if plate_pos == 'UP':
                    plate_pos = 'DOWN'
                    y_plate = 380
                    y_rbeef = 10000

    pygame.mouse.set_visible(False)  # Скрыть курсор, пока он находится в пределах окна
    if k_sc:  # Если активен экран кухни
        if ch_d == 1:  # Если выбран первый день
            target = myfont.render('ЦЕЛЬ:  1000$', False, (0, 255, 0))  # Цель - 1000$
            have = myfont.render(f'НАБРАНО: {score}', False, (0, 255, 0))
            num = time.time()  # Сохранение текущего времени в переменную
            sp.append(num)  # Добавление этой переменной в список
            newnum = time.time()  # Сохранение нового времени в переменную
            if newnum - sp[0] >= 1:  # Если проходит 10 секунд
                ord_flag = True  # Новый заказ

        screen.blit(img_kitch, (0, 0))  # Обработка изображения кухни на экране
        skovoroda.blit(img_skovoroda, (0, 0))  # Обработка изображения сковородки на поверхности сковородки
        screen.blit(skovoroda, (400, 150))  # Обработка поверхности сковородки на экране
        pan.blit(img_pan, (0, 0))  # Обработка изображения кастрюли на поверхности кастрюли
        screen.blit(pan, (700, 200))  # Обработка поверхности кастрюли на экране
        # screen.blit(target, (950, 30))  # Обработка текста цели на экране
        screen.blit(have, (950, 70))
        screen.blit(readiness, (950, 200))  # Обработка текста готовности на экране

        plate1.blit(img_plate, (0, 0))  # Обработка изображения тарелки на поверхности тарелки
        screen.blit(plate1, (x_plate, y_plate))  # Обработка поверхности тарелки на экране
        hands = myfont2.render(f'В руках: {ch_obj}', False, (220, 20, 10))  # Записываем текст о том, что у нас в руках
        screen.blit(hands, (1000, 650))  # Обработка текста на поверхности экрана

        if ord_flag:  # Если активен заказ
            r_num = random.randint(1, 5)  # Создание случайного числа
            random_sp.append(r_num)  # Добавление в список случайного числа
            if random_sp[0] == 1:  # Если случайное число - 1
                order.blit(img_order1, (0, 0))  # Обработка изображения закза_1 на поверхности заказа
                ttl4 = bnotefont.render('28', False, (4, 10, 8))  # "Номер" заказа - 28
            if random_sp[0] == 2:  # Если случайное число - 2
                order.blit(img_order2, (0, 0))  # Обработка изображения закза_2 на поверхности заказа
                ttl4 = bnotefont.render('71', False, (4, 10, 8))  # "Номер" заказа - 71
            if random_sp[0] == 3:  # Если случайное число - 3
                order.blit(img_order3, (0, 0))  # Обработка изображения закза_3 на поверхности заказа
                ttl4 = bnotefont.render('11', False, (4, 10, 8))  # "Номер" заказа - 11
            if random_sp[0] == 4:  # Если случайное число - 4
                order.blit(img_order4, (0, 0))  # Обработка изображения закза_4 на поверхности заказа
                ttl4 = bnotefont.render('50', False, (4, 10, 8))  # "Номер" заказа - 50
            if random_sp[0] == 5:  # Если случайное число - 5
                order.blit(img_order5, (0, 0))  # Обработка изображения закза_5 на поверхности заказа
                ttl4 = bnotefont.render('8', False, (4, 10, 8))  # "Номер" заказа - 8

            bgorder.blit(img_bgorder, (0, 0))  # Обработка изображения заказа в полном размере
            if ordr == 1 and od == 70_004:
                od = 0
                ordr = 2
                score = 500
                txt1 = "Два стейка.        X"  # Строка 1
                txt2 = 'Две газировки.'  # Строка 2
                txt3 = ""  # Строка 3

                ttl1 = notefont.render(txt1, False, (4, 10, 8))  # Рендер первой строки
                ttl2 = notefont.render(txt2, False, (4, 10, 8))  # Рендер второй строки
                ttl3 = notefont.render(txt3, False, (4, 10, 8))  # Рендер третьей строки
            elif ordr == 1 and od < 70_004:  # Если идёт первый заказ
                # Идёт текст заказа
                txt1 = "Две пасты.        X"  # Строка 1
                txt2 = ' Один стейк.'  # Строка 2
                txt3 = "Газировка"  # Строка 3
                ttl1 = notefont.render(txt1, False, (4, 10, 8))  # Рендер первой строки
                ttl2 = notefont.render(txt2, False, (4, 10, 8))  # Рендер второй строки
                ttl3 = notefont.render(txt3, False, (4, 10, 8))  # Рендер третьей строки

            elif ordr == 2 and od == 100_004:
                od = 0
                ordr = 3
                score = 1000
                txt1 = "Три газировки.        X"  # Строка 1
                txt2 = 'Паста.'  # Строка 2
                txt3 = ""  # Строка 3

                ttl1 = notefont.render(txt1, False, (4, 10, 8))  # Рендер первой строки
                ttl2 = notefont.render(txt2, False, (4, 10, 8))  # Рендер второй строки
                ttl3 = notefont.render(txt3, False, (4, 10, 8))  # Рендер третьей строки

            elif ordr == 3 and od == 100_004:
                od = 0
                ordr = 4
                score = 1500
                txt1 = "Паста.             X"  # Строка 1
                txt2 = ''  # Строка 2
                txt3 = ""  # Строка 3

                ttl1 = notefont.render(txt1, False, (4, 10, 8))  # Рендер первой строки
                ttl2 = notefont.render(txt2, False, (4, 10, 8))  # Рендер второй строки
                ttl3 = notefont.render(txt3, False, (4, 10, 8))  # Рендер третьей строки

            bgorder.blit(ttl1, (70, 70))  # Обработка первой строки на поверхности заказа в полном размере
            bgorder.blit(ttl2, (70, 110))  # Обработка второй строки на поверхности заказа в полном размере
            bgorder.blit(ttl3, (80, 150))  # Обработка третьей строки на поверхности заказа в полном размере
            bgorder.blit(ttl4, (110, 250))  # Обработка четвёртой строки на поверхности заказа в полном размере
            screen.blit(bgorder, (bg_x, bg_y))  # Обработка заказа в полном размере на поверхности экрана
            screen.blit(order, (650, 100))  # Обработка заказа на поверхности экрана
            r_pasta.blit(img_rpasta, (0, 0))
            screen.blit(r_pasta, (x_rpasta, y_rpasta))
            r_beef.blit(img_rbeef, (0, 0))
            screen.blit(r_beef, (x_rbeef, y_rbeef))

        # if bg_ord_flag:


    if f_sc:  # Если активен экран холодильника
        screen.blit(img_freege, (0, 0))  # Обработка изображения холодильника на поверхности экрана
        arrow.blit(img_arrow, (0, 0))  # Обработка изображения стрелки на поверхности стрелки
        beef1.blit(img_beef1, (0, 0))  # Обработка изображения мяса на поверхности мяса
        screen.blit(beef1, (500, 255))  # Обработка поверхности мяса на поверхности экрана
        pasta1.blit(img_pasta1, (0, 0))  # Обработка изображения пасты на поверхности пасты
        screen.blit(pasta1, (700, 450))  # Обработка поверхности пасты на поверхности экрана
        soda_bottle.blit(img_bottle, (0, 0))  # Обработка изображения бутылки на поверхности бутылки
        screen.blit(soda_bottle, (600, 420))  # Обработка поверхности бутылки на поверхности экрана
        crest.blit(img_crest, (0, 0))  # Обработка изображения крестика на поверхности крестика
        screen.blit(crest, (1200, 10))  # Обработка поверхности креста на поверхности креста
        hands = myfont2.render(f'В руках: {ch_obj}', False, (220, 20, 10))  # Записываем текст о том, что у нас в руках
        screen.blit(hands, (1000, 650))  # Обработка текста на поверхности экрана

    if st_sc:  # Если активен стартовый экран
        screen.blit(img_screen, (0, 0))  # Обработка изображения холодильника на поверхности экрана
    arrow.blit(img_arrow, (0, 0))  # Обработка изображения cтрелки на поверхности стрелки
    pp1.blit(img_pap, (0, 0))  # Обработка изображения перца на поверхности перца
    # pp2.blit(img_empt_pap, (0, 0))
    if d_sc:  # Если активен экран выбора дня
        # В следующих строках идёт рендер всех возможных для выбора дней. Если день достпуен - зелёный, нет - сервый.
        day1 = myfont.render(f'ДЕНЬ 1', False, (198, 124, 28))
        if days >= 2:
            day2 = myfont.render(f'ДЕНЬ 2', False, (198, 124, 28))
        else:
            day2 = myfont.render(f'ДЕНЬ 2', False, (139, 139, 139))
        if days >= 3:
            day3 = myfont.render(f'ДЕНЬ 3', False, (198, 124, 28))
        else:
            day3 = myfont.render(f'ДЕНЬ 3', False, (139, 139, 139))
        if days >= 4:
            day4 = myfont.render(f'ДЕНЬ 4', False, (198, 124, 28))
        else:
            day4 = myfont.render(f'ДЕНЬ 4', False, (139, 139, 139))
        if days >= 5:
            day5 = myfont.render(f'ДЕНЬ 5', False, (198, 124, 28))
        else:
            day5 = myfont.render(f'ДЕНЬ 5', False, (139, 139, 139))

        start_button = myfont.render('Старт', False, (250, 100, 100))  # Рендер кнопки старт

        screen.blit(img_days, (0, 0))  # Обработка изображения выбора дней на поверхности экрана
        screen.blit(arrow, (10, 10))  # Обработка изображения стрелки на поверхности экрана
        screen.blit(start_button, (600, 600))  # Обработка изображения кнопки старта на поверхности экрана
        screen.blit(day1, (250, 100))  # Обработка текста день_1 на поверхности экрана
        screen.blit(day2, (450, 100))  # Обработка текста день_2 на поверхности экрана
        screen.blit(day3, (650, 100))  # Обработка текста день_3 на поверхности экрана
        screen.blit(day4, (850, 100))  # Обработка текста день_4 на поверхности экрана
        screen.blit(day5, (1050, 100))  # Обработка текста день_5 на поверхности экрана
        if lvl == 1:  # Если уровень - 1
            hardness = myfont.render('Сложность: ', False, (15, 240, 15))  # Рендер текста сложности
            screen.blit(hardness, (25, 325))  # Обработка текста сложности на поверхности экрана
            screen.blit(pp1, (300, 300))  # Обработка изображения перца на поверхности экрана
    curs.blit(img_curs, (0, 0))  # Обработка изображения курсора на поверхности курсора
    banana.blit(img_banana, (0, 0))  # Обработка изображения банана на поверхности банана
    if st_sc:  # Если активен стартовый экран
        screen.blit(banana, (800, 450))  # Обработка изображения банана на поверхности экрана
    screen.blit(curs, (x_p, y_p))  # Обработка изображения курсора на поверхности экрана
    window.blit(screen, (0, 0))  # Обработка изображения экрана в окне
    print(od)
    pygame.display.update()  # Обновление дисплея

pygame.quit()  # Выход из программы.

'''
   Copyright [yyyy] [name of copyright owner]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
'''
