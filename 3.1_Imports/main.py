from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime
import aiogram


def daytodays():
    print(f'Сегодня {datetime.today().strftime("%Y-%m-%d")}')


if __name__ == '__main__':
    calculate_salary()
    get_employees()
    daytodays()
