# main.py

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

num = int(input("Введите число: "))
result = factorial(num)
print("Факториал:", result)