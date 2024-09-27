line = int(input("Строк: "))
char = int(input("Символов в строке: "))

byte = line * char * 2
print(f'{byte} байт')
print(f'{byte // 1024} Кб')