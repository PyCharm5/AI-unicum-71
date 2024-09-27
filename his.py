try:
    day = int(input())
    month = int(input())
    year = int(input())
except:
    print("Введите число")
    exit()

dayInMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print(0)
    if (day == 29) and (month == 2):
        print("Да")
else:
    if dayInMonths[month] <= day:
        print("Да")
    else:
        print("Нет")