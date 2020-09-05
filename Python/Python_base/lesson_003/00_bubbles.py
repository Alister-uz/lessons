# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
sd.caption = 'Lesson_002, 00_bubles'  # здорово :)
point = sd.get_point(100, 100)
radius = 50
for _ in range(3):
    sd.circle(center_position=point, radius=radius, width=2)
    radius += 5


# Написать функцию рисования пузырька, принммающую 3 (или более) параметра: точка рисования, шаг и цвет
def draw_buble(point, radius=50, step=2, width=2, amt=3, color=sd.COLOR_ORANGE):
    '''Функция рисует пузырек

    Пузырек рисуется с центром в точке point,
    радиусом radius, шагом step,
    цветом color, количеством amt и толщиной width'''
    for _ in range(amt):
        sd.circle(center_position=point, radius=radius,
                  width=width, color=color)
        radius += step


# Нарисовать 10 пузырьков в ряд
sd.clear_screen()
radius = 50
for x in range(100, 900, 80):
    point = sd.get_point(x, 300)
    draw_buble(point=point, radius=radius, step=3, amt=4)

# Нарисовать три ряда по 10 пузырьков
sd.clear_screen()
radius = 30
for y in range(450, 551, 50):
    for x in range(100, 600, 50):
        point = sd.get_point(x, y)
        draw_buble(point=point, radius=radius, step=3, amt=4, color=sd.COLOR_GREEN)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
sd.clear_screen()
for _ in range(100):
    radius = sd.randint(50, 100)
    step = sd.randint(1, 5)
    point = sd.random_point()
    color = sd.random_color()
    draw_buble(point=point, radius=radius, step=step, color=color)

sd.pause()

# зачёт! 🚀
