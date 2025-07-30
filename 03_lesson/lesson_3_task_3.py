# lesson_3_task_3.py
from address import Address
from mailing import Mailing

# Создаем адреса отправителя и получателя
to_address = Address("123456", "Москва", "Ленина", "10", "25")
from_address = Address("654321", "Санкт-Петербург", "Пушкина", "5", "30")

# Создаем почтовое отправление
mail = Mailing(
    to_address=to_address,
    from_address=from_address,
    cost=500,
    track="RR123456789RU"
)

# Выводим информацию о почтовом отправлении с разбивкой строк
print(
    f"Отправление {mail.track} из "
    f"{mail.from_address.index}, {mail.from_address.city}, "
    f"{mail.from_address.street}, {mail.from_address.house} - "
    f"{mail.from_address.apartment} в "
    f"{mail.to_address.index}, {mail.to_address.city}, "
    f"{mail.to_address.street}, {mail.to_address.house} - "
    f"{mail.to_address.apartment}. Стоимость {mail.cost} рублей."
)
