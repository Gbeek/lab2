def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Ошибка: деление на ноль"
    return x / y


if __name__ == "__main__":
    print("Простой калькулятор")

    num1 = float(input("Введите первое число: "))
    operation = input("Введите операцию (+, -, *, /): ")
    num2 = float(input("Введите второе число: "))


    if operation == '+':
        print(num1, "+", num2, "=", add(num1, num2))
    elif operation == '-':
        print(num1, "-", num2, "=", subtract(num1, num2))
    elif operation == '*':
        print(num1, "*", num2, "=", multiply(num1, num2))
    elif operation == '/':
       print(num1, "/", num2, "=", divide(num1, num2))
    else:
        print("Неверная операция")