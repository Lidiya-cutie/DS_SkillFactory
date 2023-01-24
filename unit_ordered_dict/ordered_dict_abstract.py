# Напоминаем способ создания словаря через список кортежей
# (ключ, значение)
data = [('Ivan', 19),('Mark', 25),('Andrey', 23),('Maria', 20)]
client_ages = dict(data)
print(client_ages)
# По результатам 3 повторов более ранних, чем 3.7 версий python получились вот такие результаты:
# {'Maria': 20, 'Mark': 25, 'Ivan': 19, 'Andrey': 23}
# {'Ivan': 19, 'Andrey': 23, 'Mark': 25, 'Maria': 20}
# {'Andrey': 23, 'Mark': 25, 'Maria': 20, 'Ivan': 19}

from collections import OrderedDict
data = [('Ivan', 19),('Mark', 25),('Andrey', 23),('Maria', 20)]
ordered_client_ages = OrderedDict(data)
print(ordered_client_ages)
# По результатам 3 повторов вне зависимости от версии python получились вот такие результаты:
# OrderedDict([('Ivan', 19), ('Mark', 25), ('Andrey', 23), ('Maria', 20)])
# OrderedDict([('Ivan', 19), ('Mark', 25), ('Andrey', 23), ('Maria', 20)])
# OrderedDict([('Ivan', 19), ('Mark', 25), ('Andrey', 23), ('Maria', 20)])

data = [('Ivan', 19),('Mark', 25),('Andrey', 23),('Maria', 20)]
# Сортируем по второму значению из кортежа, то есть по возрасту
ordered_client_ages = OrderedDict(sorted(data, key=lambda x: x[1]))
print(ordered_client_ages)
# OrderedDict([('Ivan', 19), ('Maria', 20), ('Andrey', 23), ('Mark', 25)])

ordered_client_ages['Nikita'] = 18
print(ordered_client_ages)
# OrderedDict([('Ivan', 19), ('Maria', 20), ('Andrey', 23), ('Mark', 25), ('Nikita', 18)])

# Если удалить элемент, а затем добавить его снова, он также окажется в конце:

del ordered_client_ages['Andrey']
print(ordered_client_ages)
# OrderedDict([('Ivan', 19), ('Mark', 25), ('Maria', 20), ('Nikita', 18)])
ordered_client_ages['Andrey'] = 23
print(ordered_client_ages)
# OrderedDict([('Ivan', 19), ('Mark', 25), ('Maria', 20), ('Nikita', 18), ('Andrey', 23)])

# Узнать версию Python в коде можно из переменной version из модуля sys.
# Пример с Codeboard:

import sys
print(sys.version)
# 3.4.3 (default, Nov 12 2018, 22:25:49)
# [GCC 4.8.4]
# Версия Python в Codeboard —  3.4.3, следовательно, ключи хранятся в словаре в случайном порядке.

ratings = [('Old York', 3.3), ('New Age', 4.6), ('Old Gold', 3.3), ('General Foods', 4.8),
          ('Belissimo', 4.5), ('CakeAndCoffee', 4.2), ('CakeOClock', 4.2), ('CakeTime', 4.1),
          ('WokToWork', 4.9), ('WokAndRice', 4.9), ('Old Wine Cellar', 3.3), ('Nice Cakes', 3.9)]
# Отсортируйте список ratings по убыванию рейтинга. Для кафе
# с одинаковым рейтингом отсортируйте кортежи по названию.
ratings.sort(key=lambda x: (-x[1], x[0]))
# Сохраните данные с рейтингом в словарь cafes, где ключами являются
# названия кафе, а значениями - их рейтинг.
from collections import OrderedDict
cafes = OrderedDict(ratings)

