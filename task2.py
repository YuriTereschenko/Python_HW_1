# Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.

first_string = "дом, кот, морж, кот, бутерброд"
second_string = "кот"
count = 0
while (second_string in first_string) is True:
    first_string = first_string.replace(second_string, "", 1)
    count += 1
print(count)
