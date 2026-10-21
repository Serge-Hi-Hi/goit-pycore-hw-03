#4
from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user['birthday'], '%Y.%m.%d').date()

        try:
            birthday_this_year = birthday.replace(year=today.year)
        except ValueError:
            birthday_this_year = birthday.replace(
                year=today.year, day=28
            )
        # робимо в обьект

        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year=today.year + 1)
        # якщо др пройшов

        if 0 <= (birthday_this_year - today).days < 7:
            # Перевіряємо, чи попадає день народження
            # у найближчі сім календарних днів, включаючи сьогоднішній

            if birthday_this_year.weekday() == 5:
                birthday_this_year += timedelta(days=2)
            # Якщо день народження у суботу, додаємо два дні, щоб отримати понеділо

            elif birthday_this_year.weekday() == 6:
                birthday_this_year += timedelta(days=1)
            # Якщо день народження у недiлю, додаємо два дні, щоб отримати понеділо

            upcoming_birthdays.append({
                'name': user['name'],
                'congratulation_date': birthday_this_year.strftime('%Y.%m.%d')
            })

    return upcoming_birthdays


users = [
    {'name': 'John Doe', 'birthday': '1985.01.23'},
    {'name': 'Jane Smith', 'birthday': '1990.01.27'}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
