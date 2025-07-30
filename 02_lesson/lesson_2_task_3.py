import math


def square(side):
    area = side ** 2  # Площадь квадрата = сторона²
    if isinstance(side, int):  # Если сторона целая
        return area
    else:  # Если сторона не целая → округляем вверх
        return math.ceil(area)


# Примеры вызова функции
print(square(4))     # 16 (целое → без округления)
print(square(2.5))   # 7 (2.5² = 6.25 → округлили до 7)
print(square(3.1))   # 10 (3.1² ≈ 9.61 → округлили до 10)
