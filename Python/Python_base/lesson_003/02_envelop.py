# -*- coding: utf-8 -*-

# (if/elif/else)

# Заданы размеры envelop_x, envelop_y - размеры конверта и paper_x, paper_y листа бумаги
#
# Определить, поместится ли бумага в конверте (стороны листа параллельны сторонам конверта,
# если размеры равны - лист входит в конверт впритирку)
# Не забывайте, что лист бумаги можно перевернуть и попробовать вставить в конверт другой стороной.
# Результат проверки вывести на консоль (ДА/НЕТ)
# Использовать только операторы if/elif/else, можно вложенные


def paper_in_envelop(envelop_x, envelop_y, paper_x, paper_y):
    if paper_x <= envelop_x and paper_y <= envelop_y:
        answer = 'ДА'
    elif paper_y <= envelop_x and paper_x <= envelop_y:
        answer = 'ДА'
    else:
        answer = 'НЕТ'
    return answer


# print('конверт:')
envelop_x, envelop_y = 10, 7
paper_x, paper_y = 8, 9
print(paper_in_envelop(envelop_x, envelop_y, paper_x, paper_y))
# проверить для
paper_x, paper_y = 9, 8
print(paper_in_envelop(envelop_x, envelop_y, paper_x, paper_y))
paper_x, paper_y = 6, 8
print(paper_in_envelop(envelop_x, envelop_y, paper_x, paper_y))
paper_x, paper_y = 8, 6
print(paper_in_envelop(envelop_x, envelop_y, paper_x, paper_y))
paper_x, paper_y = 3, 4
print(paper_in_envelop(envelop_x, envelop_y, paper_x, paper_y))
paper_x, paper_y = 11, 9
print(paper_in_envelop(envelop_x, envelop_y, paper_x, paper_y))
paper_x, paper_y = 9, 11
print(paper_in_envelop(envelop_x, envelop_y, paper_x, paper_y))

# зачёт! 🚀


# Усложненное задание, решать по желанию.
# Заданы размеры hole_x, hole_y прямоугольного отверстия и размеры brick_х, brick_у, brick_z кирпича (все размеры
# могут быть в диапазоне от 1 до 1000)
#
# Определить, пройдет ли кирпич через отверстие (грани кирпича параллельны сторонам отверстия)

def brick_in_hole(hole_x, hole_y, brick_x, brick_y, brick_z):
    if brick_x <= hole_x and (brick_y <= hole_y or brick_z <= hole_y):
        answer = 'ДА'
    elif brick_y <= hole_x and (brick_x <= hole_y or brick_z <= hole_y):
        answer = 'ДА'
    elif brick_z <= hole_x and (brick_y <= hole_y or brick_x <= hole_y):
        answer = 'ДА'
    else:
        answer = 'НЕТ'
    return answer


# print('кирпич:')
hole_x, hole_y = 8, 9
brick_x, brick_y, brick_z = 11, 10, 2
print(brick_in_hole(hole_x, hole_y, brick_x, brick_y, brick_z))
brick_x, brick_y, brick_z = 11, 2, 10
print(brick_in_hole(hole_x, hole_y, brick_x, brick_y, brick_z))
brick_x, brick_y, brick_z = 10, 11, 2
print(brick_in_hole(hole_x, hole_y, brick_x, brick_y, brick_z))
brick_x, brick_y, brick_z = 10, 2, 11
print(brick_in_hole(hole_x, hole_y, brick_x, brick_y, brick_z))
brick_x, brick_y, brick_z = 2, 10, 11
print(brick_in_hole(hole_x, hole_y, brick_x, brick_y, brick_z))
brick_x, brick_y, brick_z = 2, 11, 10
print(brick_in_hole(hole_x, hole_y, brick_x, brick_y, brick_z))
brick_x, brick_y, brick_z = 3, 5, 6
print(brick_in_hole(hole_x, hole_y, brick_x, brick_y, brick_z))
brick_x, brick_y, brick_z = 3, 6, 5
print(brick_in_hole(hole_x, hole_y, brick_x, brick_y, brick_z))
brick_x, brick_y, brick_z = 6, 3, 5
print(brick_in_hole(hole_x, hole_y, brick_x, brick_y, brick_z))
brick_x, brick_y, brick_z = 6, 5, 3
print(brick_in_hole(hole_x, hole_y, brick_x, brick_y, brick_z))
brick_x, brick_y, brick_z = 5, 6, 3
print(brick_in_hole(hole_x, hole_y, brick_x, brick_y, brick_z))
brick_x, brick_y, brick_z = 5, 3, 6
print(brick_in_hole(hole_x, hole_y, brick_x, brick_y, brick_z))
brick_x, brick_y, brick_z = 11, 3, 6
print(brick_in_hole(hole_x, hole_y, brick_x, brick_y, brick_z))
brick_x, brick_y, brick_z = 11, 6, 3
print(brick_in_hole(hole_x, hole_y, brick_x, brick_y, brick_z))
brick_x, brick_y, brick_z = 6, 11, 3
print(brick_in_hole(hole_x, hole_y, brick_x, brick_y, brick_z))
brick_x, brick_y, brick_z = 6, 3, 11
print(brick_in_hole(hole_x, hole_y, brick_x, brick_y, brick_z))
brick_x, brick_y, brick_z = 3, 6, 11
print(brick_in_hole(hole_x, hole_y, brick_x, brick_y, brick_z))
brick_x, brick_y, brick_z = 3, 11, 6
print(brick_in_hole(hole_x, hole_y, brick_x, brick_y, brick_z))

# зачёт! 🚀
