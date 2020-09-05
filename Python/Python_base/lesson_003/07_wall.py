# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
# Подсказки:
#  Для отрисовки кирпича использовать функцию rectangle
#  Алгоритм должен получиться приблизительно такой:
#
#   цикл по координате Y
#       вычисляем сдвиг ряда кирпичей
#       цикл координате X
#           вычисляем правый нижний и левый верхний углы кирпича
#           рисуем кирпич

# В решении можно нарисовать стену не на весь экран, а заданного размера
# Размер задается начальной (нижний левый угол) и конечной (верхний правый угол) точками

sd.caption = 'drawing a wall'
sd.resolution = (800, 600)
# размер кирпича:
brick_length, brick_height = 100, 50
# нижний левый угол стены (с крайнего нижнего угла экрана = 0, 0):
start_position_x, start_position_y = 100, 100
# правый верхний угол стены (до верхнего правого угла экрана = sd.resolution[0], sd.resolution[1]):
end_position_x, end_position_y = 700, 500
# задаем размер межрядного шва (шов кладки):
seam = 3
# задаем цвет:
color = sd.COLOR_DARK_ORANGE

left_bottom = sd.get_point(start_position_x, start_position_y)
right_top = sd.get_point(start_position_x + brick_length,
                         start_position_y + brick_height)
wall_top = sd.get_point(end_position_x, end_position_y)
sd.rectangle(left_bottom=left_bottom, right_top=wall_top,
             width=seam, color=color)
row = 'odd'
position_x = start_position_x

for y in range(start_position_y, end_position_y, brick_height):
    for x in range(position_x, end_position_x, brick_length):
        if x + brick_length <= end_position_x:
            shift_x = x + brick_length
        else:
            shift_x = end_position_x
        if y + brick_height <= end_position_y:
            shift_y = y + brick_height
        else:
            shift_y = end_position_y
        left_bottom = sd.get_point(x, y)
        right_top = sd.get_point(shift_x, shift_y)
        sd.rectangle(left_bottom=left_bottom,
                     right_top=right_top, width=seam, color=color)
    if row == 'odd':
        position_x = start_position_x + brick_length // 2
        row = 'even'
    else:
        position_x = start_position_x
        row = 'odd'

sd.pause()

# требуется оптимизировать код в блоке if-else: сейчас в обоих ветках есть дубликаты (практически идентичный код)
# для этого вынесите значение в отдельную переменную shift, которое изменяется в зависимости от условия
# Спасибо большое! Код реально стал легче ))

# зачёт! 🚀
