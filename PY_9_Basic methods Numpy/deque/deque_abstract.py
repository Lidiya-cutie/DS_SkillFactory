```Очередь — это упорядоченный тип данных, который обладает двумя ключевыми функциями: добавление элемента в конец очереди и извлечение самого первого элемента из очереди. То есть очередь подразумевает, что тот элемент, который первым добавлен в очередь, будет первым потом и обработан. Всё как в обычной очереди! Этот принцип сокращённо также называется FIFO (от англ. First In — First Out, «первым пришёл — первым ушёл»).```
```Стек (от англ. stack — стопка) — это упорядоченный тип данных, который обладает двумя основными функциями: добавление элемента в конец стека и извлечение элемента из конца стека. Эта структура данных также называется рюкзаком. Действительно, представьте себе, что вы набили вещами рюкзак. Теперь, когда вы решите достать из него самую верхнюю вещь, что это будет за вещь? Верно — та самая, которую вы убрали в рюкзак последней. Поэтому принцип стека (рюкзака) также сокращённо называется LIFO (Last In — First Out, «последним пришёл — первым ушёл»).```
```Наконец, существует структура данных deque (читается как «дек», англ. double-ended queue — двухконцевая очередь). Она объединяет в себе возможности и стека, и очереди: содержит функции, которые позволяют добавлять элементы в начало или в конец очереди, а также извлекать первый или последний элемент из неё. ```
# Создадим пустой дек (deque). Для этого сначала импортируем эту структуру данных из модуля collections, а затем создадим её пустой экземпляр:

from collections import deque
dq = deque()
print(dq)
# deque([])


# У deque есть четыре ключевые функции:

# append (добавить элемент в конец дека);
# appendleft (добавить элемент в начало дека);
# pop (удалить и вернуть элемент из конца дека);
# popleft (удалить и вернуть элемент из начала дека).

clients = deque()
clients.append('Ivanov')
clients.append('Petrov')
clients.append('Smirnov')
clients.append('Tikhonova')
print(clients)
# deque(['Ivanov', 'Petrov', 'Smirnov', 'Tikhonova'])

# Объект deque поддерживает индексацию по элементам:

print(clients[2])
# Smirnov

# Освободилось два оператора — заберём двоих человек из начала очереди с помощью popleft:

first_client = clients.popleft()
second_client = clients.popleft()
 
print("First client:", first_client)
print("Second client:", second_client)
print(clients)
# First client: Ivanov
# Second client: Petrov
# deque(['Smirnov', 'Tikhonova'])

# Вдруг появился VIP-клиент. Для него тоже нет свободного оператора, но добавить его нужно в начало очереди с помощью appendleft:

clients.appendleft('Vip-client')
 
print(clients)
# deque(['Vip-client', 'Smirnov', 'Tikhonova'])

# Последний клиент в очереди устал ждать и отменил вызов. Удалим его с помощью pop:

tired_client = clients.pop()
print(tired_client, "left the queue")
print(clients)
# Tikhonova left the queue
# deque(['Vip-client', 'Smirnov'])

clients = deque(['Ivanov', 'Petrov', 'Smirnov', 'Tikhonova'])
print(clients)
# deque(['Ivanov', 'Petrov', 'Smirnov', 'Tikhonova'])
del clients[2]
print(clients)
# deque(['Ivanov', 'Petrov', 'Tikhonova'])

```Также в очередь возможно добавить сразу несколько элементов из итерируемого объекта в дек. 
Для этого используют функции extend (добавить в конец дека) и extendleft (добавить в начало дека).````

# В скобках передаём список при создании deque,
# чтобы сразу добавить все его элементы в очередь
shop = deque([1, 2, 3, 4, 5])
print(shop)
# deque([1, 2, 3, 4, 5])
shop.extend([11, 12, 13, 14, 15, 16, 17])
print(shop)
# deque([1, 2, 3, 4, 5, 11, 12, 13, 14, 15, 16, 17])

shop = deque([1, 2, 3, 4, 5])
print(shop)
# deque([1, 2, 3, 4, 5])
shop.extendleft([11, 12, 13, 14, 15, 16, 17])
print(shop)
# deque([17, 16, 15, 14, 13, 12, 11, 1, 2, 3, 4, 5])
# Добавление слева происходит в обратном порядке

limited = deque(maxlen=3)
print(limited)
# deque([], maxlen=3)
 
# очередь с ограниченной максимальной длиной
limited_from_list = deque([1,3,4,5,6,7], maxlen=3)
print(limited_from_list)
# deque([5, 6, 7], maxlen=3)

limited.extend([1,2,3])
print(limited)
# deque([1, 2, 3], maxlen=3)
 
print(limited.append(8))
# None
print(limited)
# deque([2, 3, 8], maxlen=3)

# Ниже приведены средние дневные температуры в Москве за июль:

temps = [20.6, 19.4, 19.0, 19.0, 22.1,
        22.5, 22.8, 24.1, 25.6, 27.0,
        27.0, 25.6, 26.8, 27.3, 22.5,
        25.4, 24.4, 23.7, 23.6, 22.6,
        20.4, 17.9, 17.3, 17.3, 18.1,
        20.1, 22.2, 19.8, 21.3, 21.3,
        21.9]

# Посчитаем динамику с усреднением за каждые последние 7 дней для каждого рассматриваемого дня.
days = deque(maxlen=7)
 
for temp in temps:
    # Добавляем температуру в очередь
    days.append(temp)
    # Если длина очереди оказалась равной максимальной длине очереди (7),
    # печатаем среднюю температуру за последние 7 дней
    if len(days) == days.maxlen:
        print(round(sum(days) / len(days), 2), end='; ')
# Напечатаем пустую строку, чтобы завершить действие параметра
# end. Иначе следующая строка окажется напечатанной на предыдущей
print("")
# Результат:
# 20.77; 21.27; 22.16; 23.3; 24.44; 24.94; 25.56; 26.2; 25.97;
# 25.94; 25.57; 25.1; 24.81; 24.21; 23.23; 22.57; 21.41; 20.4;
# 19.6; 19.1; 19.04; 18.96; 19.44; 20.01; 20.67;

# reverse позволяет поменять порядок элементов в очереди на обратный:

dq = deque([1,2,3,4,5])
print(dq)
# deque([1, 2, 3, 4, 5])
 
dq.reverse()
print(dq)
# deque([5, 4, 3, 2, 1])

# rotate переносит  заданных элементов из конца очереди в начало:

dq = deque([1,2,3,4,5])
print(dq)
# deque([1, 2, 3, 4, 5])
 
dq.rotate(2)
print(dq)
# deque([4, 5, 1, 2, 3])

# Элементы можно переносить и из начала в конец:

dq = deque([1,2,3,4,5])
print(dq)
# deque([1, 2, 3, 4, 5])
 
# Отрицательное значение аргумента переносит
# n элементов из начала в конец
dq.rotate(-2)
print(dq)
# deque([3, 4, 5, 1, 2])

# Функция index позволяет найти первый индекс искомого элемента
# count позволяет подсчитать, сколько раз элемент встретился в очереди

dq = [1,2,4,2,3,1,5,4,4,4,4,4,3]
print(dq.index(4))
# 2
print(dq.count(4))
# 6

# Обратите внимание, что при попытке узнать индекс несуществующего элемента возникнет ValueError:

dq = deque([1,2,4,2,3,1,5,4,4,4,4,4,3])
print(dq.index(25))
# ValueError: 25 is not in deque

# А вот посчитать несуществующий элемент можно (получится просто 0):

dq = deque([1,2,4,2,3,1,5,4,4,4,4,4,3])
print(dq.count(25))
# 0

# Наконец, функция clear позволяет очистить очередь:

dq = deque([1,2,4,2,3,1,5,4,4,4,4,4,3])
print(dq)
# deque([1, 2, 4, 2, 3, 1, 5, 4, 4, 4, 4, 4, 3])
dq.clear()
print(dq)
# deque([])

```Необходимо напечатать словарь, в котором ключи — годы, а значения — показатели температуры.
Ключи необходимо отсортировать в порядке убывания соответствующих им температур```

# 1 var
temps = [('2000', -4.4), ('2001', -2.5), ('2002', -4.4), ('2003', -9.5)]

from collections import OrderedDict

def check(temps):
    temps.sort(key=lambda x: x[1], reverse=True)
    od = OrderedDict(temps)
    od = str(od)
    print(od)
    
    
# 2 var
temps = [('2000', -4.4), ('2001', -2.5), ('2002', -4.4), ('2003', -9.5)]

from collections import OrderedDict

def check(temps):
    needed_dict = OrderedDict(reversed(sorted(temps, key=lambda x: x[1])))
    print(needed_dict)
    
# Извлеките элемент из начала очереди. Запишите полученное значение элемента в качестве ответа.
    
from hidden import users
from collections import deque

users = [6, 18, 4, 7, 8, 8, 5, 18, 12, 17, 13, 15, 6, 7, 9, 17, 18, 8, 4, 11, 10, 8, 2, 10, 6, 10, 10, 9]

users = deque(users)
user_id = users.popleft()
print(user_id)

# очереди переместите пять элементов из начала очереди в её конец. Извлеките последний элемент из очереди. Запишите полученное число в качестве ответа

from hidden import users
from collections import deque
users = deque(users)
user_id = users.popleft()
# Окончание копии предыдущего решения
users.rotate(-5)
user_id = users.pop()
print(user_id)

# с тем номером, что был извлечён в предыдущем задании, осталось в модифицированной очереди? Запишите ответ в числовой форме

from collections import deque
users = deque(users)
user_id = users.popleft()
users.rotate(-5)
user_id = users.pop()
# Окончание копии предыдущего решения
print(users.count(user_id))

# Введите свое решение ниже
from collections import deque

```Напишите функцию brackets(line), которая определяет, является ли последовательность из круглых скобок line правильной.````

def brackets(line):
    # Напишите тело функции
    stack = deque()
    for i in line:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if len(stack) == 0:
                return False
            stack.pop()
    if len(stack) == 0:
        return True
    return False

print(brackets("(()())"))
# True
print(brackets(""))
# True
print(brackets("(()()))"))
# False
