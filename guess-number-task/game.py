"""Игра угадай число"""

import numpy as np

number = np.random.randint(1, 101) # загадываем число

# количество попыток
guessing_made = 0
while guessing_made <= 20:
    while True:
        guessing_made+=1
        predict_number = int(input("Загадано число от 1 до 100. Ваше предположение?: "))
    
        if predict_number > number:
            print("Неверно! Число должно быть меньше!")

        elif predict_number < number:
            print("Неверно! Число должно быть больше!")
    
        else:
            print(f"Поздравляю! Вы угадали число! Это число = {number}, вам потребовалось {guessing_made} попыток")
            break #конец игры выход из цикла
        
else:
    print (f"Попытки закончились. Вы не угадали! Было загадано число {number}")
