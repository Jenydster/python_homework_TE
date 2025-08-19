import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


# Позитивные тесты
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),             # Стандартный случай
    ("hello world", "hello world"),       # Без начальных пробелов
    ("   2023 год", "2023 год"),          # Цифры в начале
    ("\t\nне должно удаляться", "\t\nне должно удаляться")
    # Не-пробельные символы
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


# Негативные тесты
@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),            # Пустая строка
    ("   ", ""),         # Строка из пробелов
    (None, None),        # None (проверяем обработку исключений)
])
def test_trim_negative(input_str, expected):
    if input_str is None:
        with pytest.raises(AttributeError):
            string_utils.trim(input_str)
    else:
        assert string_utils.trim(input_str) == expected


# Позитивные тесты
@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", True),         # Символ в начале
    ("Тест", "с", True),           # Кириллический символ
    ("12345", "3", True),          # Цифры в строке
    ("04 апреля 2023", "апреля", True)  # Подстрока с пробелом
])
def test_contains_positive(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected


# Негативные тесты
@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "U", False),       # Отсутствующий символ
    ("", "a", False),             # Пустая строка
    (" ", "a", False),            # Строка из пробела
    ("Hello", "", True),          # Пустой символ (особый случай!)
    (None, "a", False)            # None вместо строки
])
def test_contains_negative(string, symbol, expected):
    if string is None:
        with pytest.raises(AttributeError):
            string_utils.contains(string, symbol)
    else:
        assert string_utils.contains(string, symbol) == expected


# Позитивные тесты
@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),            # Удаление одного символа
    ("Hello world", "l", "Heo word"),    # Удаление нескольких символов
    ("123456", "34", "1256"),            # Удаление подстроки с цифрами
    ("Тестирование", "и", "Тестроване")  # Кириллические символы
])
def test_delete_symbol_positive(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected


# Негативные тесты
@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "X", "SkyPro"),     # Отсутствующий символ
    ("", "a", ""),                 # Пустая строка
    ("   ", " ", ""),              # Строка из пробелов
    ("Text", "", "Text"),          # Пустой символ удаления
    (None, "a", None)              # None вместо строки
])
def test_delete_symbol_negative(string, symbol, expected):
    if string is None:
        with pytest.raises(AttributeError):
            string_utils.delete_symbol(string, symbol)
    else:
        assert string_utils.delete_symbol(string, symbol) == expected
