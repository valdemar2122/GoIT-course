from datetime import date, timedelta

start_date = date.today()
end_date = start_date + timedelta(7)

def get_period(start_date: date, days: int):
    result = {}
    for i in range(days + 1):
        result[start_date.day, start_date.month] = start_date.year
        start_date += timedelta(7)

def get_bd(users: list) -> list:
    start_date = date.today()
    end_date = start_date + timedelta(7)

    for user in users:
        bd: date = user["birthday"]
        bd.replace(year = start_date.year)

if __name__ == '__main__':
    users = [{"name": "Bill", "birthday": date(1990, 9, 28)},
              {"name": "Marry", "birthday": date(2000, 10, 2)},
             ]
    

get_bd(users)