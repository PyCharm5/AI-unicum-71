try:
    line = int(input("Строк на странице: "))
    letters = int(input("Символов в строке: "))
    page = int(input("Кол-во страниц: "))

except:
    print("Введите число")

def degree(line, letters, page):
    print(f'{page * line * letters * 2 * 8} Бит')
    print(f'{page * line * letters * 2 / 1024} КБ')

degree(line, letters, page)