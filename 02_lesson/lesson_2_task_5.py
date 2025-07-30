def month_to_season(m):
    if m in (12, 1, 2):
        return "Зима"
    elif m in (3, 4, 5):
        return "Весна"
    elif m in (6, 7, 8):
        return "Лето"
    else:
        return "Осень"


# Примеры использования
print(month_to_season(2))  # Зима
print(month_to_season(7))  # Лето
print(month_to_season(9))  # Осень
