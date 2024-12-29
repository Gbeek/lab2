# Функция сложения
def add(x, y):
    return x + y

# Функция вычитания
def subtract(x, y):
    return x - y

# Функция умножения
def multiply(x, y):
    return x * y

# Функция деления
def divide(x, y):
    if y == 0:
        return "Ошибка: деление на ноль"
    return x / y

# Функция для выполнения вычислений
def calculate(num1, operation, num2):
    if operation == '+':
        return add(num1, num2)
    elif operation == '-':
       return subtract(num1, num2)
    elif operation == '*':
       return multiply(num1, num2)
    elif operation == '/':
       return divide(num1, num2)
    else:
        return "Неверная операция"

if __name__ == "__main__":
    print("Простой калькулятор")

    while True:
        try:
            num1 = float(input("Введите первое число: "))
            operation = input("Введите операцию (+, -, *, /) (или 'q' для выхода): ")

            if operation == 'q':
               break

            num2 = float(input("Введите второе число: "))

            result = calculate(num1, operation, num2)
            print(num1, operation, num2, "=", result)


        except ValueError:
            print("Ошибка: Неверный ввод числа.")
        except Exception as e:
            print(f"Неизвестная ошибка: {e}")