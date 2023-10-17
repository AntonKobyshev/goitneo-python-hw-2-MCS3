import json
from datetime import datetime
from collections import defaultdict


def get_birthdays_per_week(users_data):
    birthdays_per_week = defaultdict(list)
    days_of_week = {
        0: 'Monday', 1: 'Tuesday', 2: 'Wednesday',
        3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'
    }

    today = datetime.today().date()

    for user in users_data:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year=today.year + 1)

        delta_days = (birthday_this_year - today).days

        if delta_days < 7:
            if birthday_this_year.weekday() >= 5:
                birthdays_per_week[days_of_week[0]].append(name)
            else:
                birthdays_per_week[days_of_week[birthday_this_year.weekday()]].append(
                    name)

    for day, users_list in birthdays_per_week.items():
        print(f"{day}: {', '.join(users_list)}")


def main():
    with open('data/users.json', 'r') as file:
        users_data = json.load(file)

    for user in users_data:
        user["birthday"] = datetime.strptime(user["birthday"], "%Y-%m-%d")

    get_birthdays_per_week(users_data)


if __name__ == "__main__":
    main()