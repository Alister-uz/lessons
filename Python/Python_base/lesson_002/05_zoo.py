#!/usr/bin/env python
# -*- coding: utf-8 -*-

# есть список животных в зоопарке

zoo = ['lion', 'kangaroo', 'elephant', 'monkey']

# посадите медведя (bear) между львом и кенгуру
#  и выведите список на консоль
zoo.insert(1, 'bear')
print(', '.join(zoo))

# добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark']
#  и выведите список на консоль
zoo += birds
print(', '.join(zoo))

# уберите слона
#  и выведите список на консоль
if 'elephant' in zoo:
    zoo.remove('elephant')
print(', '.join(zoo))

# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.
print('лев сидит в клетке номер ' + str(zoo.index('lion')+1))
print('жаворонок сидит в клетке номер ' + str(zoo.index('lark')+1))