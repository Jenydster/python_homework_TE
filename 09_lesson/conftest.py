# 09_lesson/conftest.py
import pytest
from sqlalchemy.orm import Session
from config import get_db, Base, engine


@pytest.fixture(scope="session", autouse=True)
def setup_database():
    """Создание и удаление таблиц для тестов"""
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def db() -> Session:
    """Фикстура для получения сессии БД"""
    database = next(get_db())
    try:
        yield database
    finally:
        database.rollback()
        database.close()
