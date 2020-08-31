#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Есть список песен группы Depeche Mode со временем звучания с точностью до долей минут
from typing import List, Union

violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]

# Распечатайте общее время звучания трех песен: 'Halo', 'Enjoy the Silence' и 'Clean' в формате
#   Три песни звучат ХХХ.XX минут
# Точность указывается в функции round(a, b)
# где a, это число которое надо округлить, а b количество знаков после запятой
# более подробно про функцию round смотрите в документации https://docs.python.org/3/search.html?q=round

duration_songs = 0
for i in violator_songs:
    if i[0] == 'Halo' or i[0] == 'Enjoy the Silence' or i[0] == 'Clean':  # ищем три заданные песни
        duration_songs = round(duration_songs + i[1], 2)
print('Три пени звучат', duration_songs, ' минут')

# Есть словарь песен группы Yellow со временем звучания с точностью до долей минут
pocket_universe_songs = {
    'Solar Driftwood': 1.85,
    'Celsius': 5.98,
    'More': 6.65,
    'On Track': 5.55,
    'Monolith': 6.35,
    'To the Sea': 5.77,
    'Magnetic': 5.88,
    'Liquid Mountain': 2.97,
    'Pan Blue': 5.52,
    'Resistor': 7.22,
    'Beyond Mirrors': 5.82,
}

# Распечатайте общее время звучания трех песен: 'On Track', 'To the Sea' и 'Beyond Mirrors'
#   А другие три песни звучат приблизительно ХХХ минут

duration_songs = 0
for key in pocket_universe_songs:  # ищем три другие заданные песни
    if key == 'On Track' or key == 'To the Sea' or key == 'Beyond Mirrors':
        duration_songs = duration_songs + pocket_universe_songs[key]
# NOTE округлять промежуточные ответы в процессе вычислений - терять точность в вычислениях
duration_three_songs = round(duration_songs)
print('А другие три песни звучат приблизительно', duration_three_songs, 'минут')
# NOTE обратите внимание на ответ теперь: было 18 стало 17. Верный ответ - 17.
# Обратите внимание, что делать много вычислений внутри print() - плохой стиль.
# Лучше заранее вычислить необходимое, а затем в print(xxx, yyy, zzz)

# зачёт! 🚀
