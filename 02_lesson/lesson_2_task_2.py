def is_year_leap(year):
    if year % 4 == 0:  # Если год делится на 4 без остатка
        return True
    else:
        return False


# Пример вызова функции
year = 2024  # Можно выбрать любой год
result = is_year_leap(year)
print(f"год {year}: {result}")
