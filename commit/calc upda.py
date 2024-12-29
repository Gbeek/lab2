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
    print("1 + 2 =", add(1, 2))
    print("5 - 3 =", subtract(5, 3))
    print("4 * 5 =", multiply(4, 5))
    print("10 / 2 =", divide(10, 2))
    print("10 / 0 =", divide(10, 0))