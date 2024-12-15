from datetime import datetime

def get_days_from_today(date):
    """
    Розраховує кількість днів між заданою датою і поточною датою.

    :param date: рядок, що представляє дату у форматі 'РРРР-ММ-ДД'
    :return: ціле число, яке вказує на кількість днів від заданої дати до поточної
    """
    try:
        
        input_date = datetime.strptime(date, '%Y-%m-%d').date()
        
        today_date = datetime.today().date()
        
        delta = (today_date - input_date).days
        return delta
    except ValueError:
        
        raise ValueError("Неправильний формат дати. Використовуйте формат 'РРРР-ММ-ДД'.")


if __name__ == "__main__":
    try:
        example_date = "2021-10-09"
        result = get_days_from_today(example_date)
        print(f"Кількість днів від {example_date} до сьогоднішньої дати: {result}")
    except ValueError as e:
        print(e)
