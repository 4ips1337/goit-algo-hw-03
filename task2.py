import random

def get_numbers_ticket(min_val, max_val, quantity):
    """
    Генерує відсортований список унікальних випадкових чисел у заданому діапазоні.

    :param min_val: Мінімальне можливе число (не менше 1).
    :param max_val: Максимальне можливе число (не більше 1000).
    :param quantity: Кількість чисел, які потрібно вибрати.
    :return: Відсортований список унікальних чисел або пустий список, якщо параметри некоректні.
    """
    
    if not (1 <= min_val <= max_val <= 1000):
        return []
    if not (0 < quantity <= (max_val - min_val + 1)):
        return []

    
    numbers = random.sample(range(min_val, max_val + 1), quantity)


    return sorted(numbers)


lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)