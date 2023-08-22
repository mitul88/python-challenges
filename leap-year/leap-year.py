def is_leap(year):
    """Its going to reaturn a boolean value indicating if the year is leap year or not"""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(y, m):
    """It will return number of days in a given month of a given year"""
    if m > 12 or m < 1:
        return "Invalid Month"
    leap_year = is_leap(y)
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if leap_year == False:
        month_days[1] = 29
    return month_days[m - 1]


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
