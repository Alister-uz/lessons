#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп

# lamps_cost = store[goods['Лампа']][0]['quantity'] * \
#     store[goods['Лампа']][0]['price']
# или проще (/сложнее ?)

# Вывести стоимость каждого вида товара на складе:
# один раз распечать сколько всего столов и их общая стоимость,
# один раз распечать сколько всего стульев и их общая стоимость,
#   и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

# WARNING для знающих циклы: БЕЗ циклов. Да, с переменными; да, неэффективно; да, копипаста.
# Это задание на ручное вычисление - что бы потом понять как работают циклы и насколько с ними проще жить.

lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price

table_code = goods['Стол']
tables_item1 = store[table_code][0]
tables_item2 = store[table_code][1]
tables_quantity1 = tables_item1['quantity']
tables_quantity2 = tables_item2['quantity']
tables_quantity = tables_quantity1 + tables_quantity2
tables_price1 = tables_item1['price']
tables_price2 = tables_item2['price']
tables_cost = tables_quantity1 * tables_price1 + tables_quantity2 * tables_price2

sofa_code = goods['Диван']
sofas_item1 = store[sofa_code][0]
sofas_item2 = store[sofa_code][1]
sofas_quantity1 = sofas_item1['quantity']
sofas_quantity2 = sofas_item2['quantity']
sofas_quantity = sofas_quantity1 + sofas_quantity2
sofas_price1 = sofas_item1['price']
sofas_price2 = sofas_item2['price']
sofas_cost = sofas_quantity1 * sofas_price1 + sofas_quantity2 * sofas_price2

chair_code = goods['Стул']
chairs_item1 = store[chair_code][0]
chairs_item2 = store[chair_code][1]
chairs_item3 = store[chair_code][2]
chairs_quantity1 = chairs_item1['quantity']
chairs_quantity2 = chairs_item2['quantity']
chairs_quantity3 = chairs_item3['quantity']
chairs_quantity = chairs_quantity1 + chairs_quantity2 + chairs_quantity3
chairs_price1 = chairs_item1['price']
chairs_price2 = chairs_item2['price']
chairs_price3 = chairs_item3['price']
chairs_cost = chairs_quantity1 * chairs_price1 + chairs_quantity2 * \
    chairs_price2 + chairs_quantity3 * chairs_price3


print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')
print('Стол -', tables_quantity, 'шт, стоимость', tables_cost, 'руб')
print('Диван -', sofas_quantity, 'шт, стоимость', sofas_cost, 'руб')
print('Стул -', chairs_quantity, 'шт, стоимость', chairs_cost, 'руб')

# Complited
# зачёт! 🚀
