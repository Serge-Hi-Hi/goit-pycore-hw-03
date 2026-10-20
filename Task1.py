#1

from datetime import datetime

def get_days_from_today(date):
    try:
        given_date = datetime.strptime(date, '%Y-%m-%d').date()
        today = datetime.today().date()
        difference = today - given_date
        return difference.days
    except ValueError:
        return 'Wrong format'


print(get_days_from_today('2021-10-09'))