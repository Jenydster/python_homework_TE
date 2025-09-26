# Проект автоматизированного тестирования

# Этот проект содержит тесты для веб-приложений с использованием Selenium и Allure для отчетов.



## Структура проекта



- `pages/` - Классы Page Object для работы со страницами

- `tests/` - Тестовые сценарии

- `requirements.txt` - Зависимости проекта



## Запуск тестов



1. Установите зависимости:

```bash

pip install -r requirements.txt



Запуск тестов командой pytest --alluredir=allure_results

отчет 

allure serve allure_results

