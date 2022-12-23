from datetime import datetime


def is_today():
    return datetime.today().weekday()


print(datetime.now().strftime('%A'))

