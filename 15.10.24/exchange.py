#c_uan = float(input("Введите курс юаня:   "))
#c_dol = float(input("Введите курс доллара:   "))
#c_tenge = float(input("Введите курс тенге:   "))

from currency_converter import CurrencyConverter
c = CurrencyConverter()

count = float(input("Введите число рублей:   "))

print(c.convert(count, 'RUB', 'CNY')), "юаней"
print(c.convert(count, 'RUB', 'USD')), "долларов"
print(c.convert(count, 'RUB', 'NZD')), "новозеландский доллар"

#print(f'{count} рублей - это {c_uan} юаней, {c_dol} долларов, {c_tenge} тенге.')