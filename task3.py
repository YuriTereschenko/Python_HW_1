# Подсчитать сумму цифр в вещественном числе.
n = input()
n = list(n)
n.remove(".")
result = 0
for i in range(0, len(n)):
    result += int(n[i])
print(result)