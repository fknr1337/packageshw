import datetime
from application.salary import calculate_salary
from db.people import get_employees

if __name__ == '__main__':
    print(datetime.datetime.now())
    print(calculate_salary(1000))
    get_employees()
