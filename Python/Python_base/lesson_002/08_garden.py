#!/usr/bin/env python
# -*- coding: utf-8 -*-

# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка',
          'гладиолус', 'подсолнух', 'роза')

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка',
          'клевер', 'мак', 'одуванчик', 'ромашка')

# создайте множество цветов, произрастающих в саду и на лугу
garden_set = set(garden)
meadow_set = set(meadow)

# выведите на консоль все виды цветов
all_flowers = garden_set.union(meadow_set)
print(all_flowers)

# выведите на консоль те, которые растут и там и там
here_and_there = garden_set.intersection(meadow_set)
print(here_and_there)


# выведите на консоль те, которые растут в саду, но не растут на лугу
only_garden = garden_set.difference(meadow_set)
print(only_garden)

# выведите на консоль те, которые растут на лугу, но не растут в саду
only_meadow = meadow_set.difference(garden_set)
print(only_meadow)
