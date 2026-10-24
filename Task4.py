#4

from datetime import datetime, date, timedelta

def get_upcoming_birthdays(users):
    today = date.today()
    upcoming_birthdays = []

    def birthday_in_year(birthday, year):
        try:
            return birthday.replace(year=year)
        except ValueError:
            # 29 лютого у невисокосному році -> 28 лютого
            return birthday.replace(year=year, day=28)

    for user in users:
        birthday = datetime.strptime(user['birthday'], '%Y.%m.%d').date()

        birthday_this_year = birthday_in_year(birthday, today.year)
        # робимо в об'єкт

        if birthday_this_year < today:
            birthday_this_year = birthday_in_year(birthday, today.year + 1)
        # якщо др пройшов

        if (birthday_this_year - today).days < 7:
            # Перевіряємо, чи попадає день народження
            # у найближчі сім календарних днів, включаючи сьогоднішній

            if birthday_this_year.weekday() >= 5:
                birthday_this_year += timedelta(days=7 - birthday_this_year.weekday())
            # Субота (+2) або неділя (+1) -> переносимо на понеділок

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
