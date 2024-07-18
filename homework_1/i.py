import calendar

N, year = int(input()), int(input())
months = tuple(calendar.month_abbr)
holidays = [(int(d), months.index(m[0:3]) - 1) for _ in range(N) for d, m in (input().split(),)]
days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
first_day_of_year = days.index(input())
quantity_days_in_year = {
    'Monday': 0, 'Tuesday': 0, 'Wednesday': 0, 'Thursday': 0, 'Friday': 0, 'Saturday': 0, 'Sunday': 0
}
days_in_month = (31, 29 if calendar.isleap(year) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

for month in range(12):
    for day in range(1, days_in_month[month] + 1):
        if (day, month) not in holidays:
            quantity_days_in_year[days[first_day_of_year]] += 1
        first_day_of_year = (first_day_of_year + 1) % 7


print(max(quantity_days_in_year.items(), key=lambda x: x[1])[0], min(quantity_days_in_year.items(), key=lambda x: x[1])[0])