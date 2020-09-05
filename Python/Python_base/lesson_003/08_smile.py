# -*- coding: utf-8 -*-

# (определение функций)


import simple_draw as sd


# Написать функцию отрисовки смайлика по заданным координатам
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

sd.caption = 'drawing a smile'
sd.resolution = (800, 800)


def smile(position_x=300, position_y=300, radius=50, color=sd.COLOR_GREEN):
    ''' Функция отрисовки смайлика

    '''

    if radius < 10:
        radius = 10

    center = sd.get_point(position_x, position_y)
    mesh_size = radius//10

    right_eye_bottom = sd.get_point(
        position_x - mesh_size * 5, position_y + mesh_size * 2)
    right_eye_top = sd.get_point(
        position_x - mesh_size * 3, position_y + mesh_size * 6)
    right_eye_center = sd.get_point(
        position_x - mesh_size * 4, position_y + mesh_size * 4)
    left_eye_bottom = sd.get_point(
        position_x + mesh_size * 3, position_y + mesh_size * 2)
    left_eye_top = sd.get_point(
        position_x + mesh_size * 5, position_y + mesh_size * 6)
    left_eye_center = sd.get_point(
        position_x + mesh_size * 4, position_y + mesh_size * 4)
    eye_apple_radius = radius // 20 if radius // 20 > 0 else 1

    mouth = [
        sd.get_point(
            position_x - mesh_size * 6, position_y - mesh_size * 4),
        sd.get_point(
            position_x - mesh_size * 4, position_y - mesh_size * 5),
        sd.get_point(
            position_x - mesh_size * 2, position_y - mesh_size * 6),
        sd.get_point(
            position_x + mesh_size * 2, position_y - mesh_size * 6),
        sd.get_point(
            position_x + mesh_size * 4, position_y - mesh_size * 5),
        sd.get_point(
            position_x + mesh_size * 6, position_y - mesh_size * 4),
    ]

    sd.circle(center_position=center, radius=radius, color=color)
    sd.ellipse(left_bottom=right_eye_bottom,
               right_top=right_eye_top, color=color, width=1)
    sd.circle(center_position=right_eye_center,
              radius=eye_apple_radius, color=color, width=0)
    sd.ellipse(left_bottom=left_eye_bottom,
               right_top=left_eye_top, color=color, width=1)
    sd.circle(center_position=left_eye_center,
              radius=eye_apple_radius, color=color, width=0)
    sd.lines(point_list=mouth, color=color, closed=True)


for _ in range(10):
    position_x = sd.random_number(50, sd.resolution[0] - 50)
    position_y = sd.random_number(50, sd.resolution[1] - 50)
    radius = sd.random_number(20, 100)
    color = sd.random_color()
    # if color == sd.background_color:  # эти строки можно удалить
    #     color == sd.COLOR_BLACK       # Оставила закоменченными, что бы просто пояснить:
    # подумала, вдруг цвет смайлика будет такой-же, как цвет фона и смайлик потеряется ))
    smile(position_x=position_x, position_y=position_y,
          radius=radius, color=color)


sd.pause()

# зачёт! 🚀
