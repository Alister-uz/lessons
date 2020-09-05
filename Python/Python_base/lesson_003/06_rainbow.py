# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
# Подсказка: цикл нужно делать сразу по тьюплу с цветами радуги.

sd.caption = 'Lesson_002, 06_rainbow'

start_x, start_y = 50, 50
end_x, end_y = 350, 450
width = 5
step = 5

for color in reversed(rainbow_colors):
    start_point = sd.get_point(start_x, start_y)
    end_point = sd.get_point(end_x, end_y)
    sd.line(start_point, end_point, color=color, width=width)
    start_x -= step
    end_x -= step

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво

position_x, position_y = 400, -200
radius, width = 500, 20

for color in rainbow_colors:
    center_position = sd.get_point(position_x, position_y)
    sd.circle(center_position=center_position,
              radius=radius, color=color, width=width)
    radius += width
# радуга-дуга получилась вывернутой (порядок цветов неверный)
# для обратного порядка можно использовать reversed(), то есть "for color in reversed(rainbow_colors): ..."
# в радуге-дуге не стала изменять, так как порядок цветов такой же, как и в examples: https://i.imgur.com/5hqrbl6.png
# но поменяла в радуге-линии, так как в examples она как раз наоборот
# (прошу прощения, не обратила внимания)

sd.pause()

# зачёт! 🚀
