"""
* @file main.py
* @author Elizaveta Konstantinova
* @brief Нахождение количества локальных максимумов
* @version 0.1
* @date 2022-10-07
*
* @copyright Copyright (c) 2022
*
"""

"""
* @brief функция для нахождения количества локальных максимумов
"""
def foo(amountStr, numbersStr):
    amount = int(amountStr)
    numbers = list(map(int, numbersStr.split()))
    counter = 0
    for i in range(0, amount - 1):
        if numbers[i] > numbers[i - 1] and numbers[i] > numbers[i + 1]:
            counter += 1
    return counter

