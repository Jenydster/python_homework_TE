# 09_lesson/test_crud_operations.py
import pytest
from sqlalchemy.orm import Session
from config import get_db, Base, engine
from models import Student, Subject


# Создаем таблицы перед запуском тестов
@pytest.fixture(scope="session", autouse=True)
def create_tables():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def db_session():
    """Фикстура для получения сессии БД"""
    db = next(get_db())
    try:
        yield db
    finally:
        db.rollback()
        db.close()


def test_create_student(db_session: Session):
    """Тест на создание студента"""
    # Подготовка данных
    student_data = {
        "name": "Иван Иванов",
        "email": "ivan@example.com"
    }

    # Создание объекта
    student = Student(**student_data)
    db_session.add(student)
    db_session.commit()
    db_session.refresh(student)

    # Проверка
    assert student.id is not None
    assert student.name == "Иван Иванов"
    assert student.email == "ivan@example.com"

    # Очистка
    db_session.delete(student)
    db_session.commit()


def test_update_subject(db_session: Session):
    """Тест на обновление предмета"""
    # Создаем предмет для теста
    subject = Subject(name="Математика", description="Базовый курс")
    db_session.add(subject)
    db_session.commit()
    db_session.refresh(subject)

    # Обновляем данные
    subject_id = subject.id
    db_session.query(Subject).filter(Subject.id == subject_id).update({
        "description": "Продвинутый курс математики"
    })
    db_session.commit()

    # Проверяем обновление
    updated_subject = db_session.query(Subject).filter(Subject.id == subject_id).first()
    assert updated_subject.description == "Продвинутый курс математики"

    # Очистка
    db_session.delete(updated_subject)
    db_session.commit()


def test_delete_student(db_session: Session):
    """Тест на удаление студента"""
    # Создаем студента для теста
    student = Student(name="Петр Петров", email="petr@example.com")
    db_session.add(student)
    db_session.commit()
    db_session.refresh(student)

    student_id = student.id

    # Удаляем студента
    db_session.query(Student).filter(Student.id == student_id).delete()
    db_session.commit()

    # Проверяем, что студент удален
    deleted_student = db_session.query(Student).filter(Student.id == student_id).first()
    assert deleted_student is None


def test_create_student_with_unique_email(db_session: Session):
    """Дополнительный тест на уникальность email"""
    # Первый студент
    student1 = Student(name="Анна Сидорова", email="anna@example.com")
    db_session.add(student1)
    db_session.commit()
    db_session.refresh(student1)

    # Второй студент с тем же email (должен вызвать ошибку)
    student2 = Student(name="Другая Анна", email="anna@example.com")
    db_session.add(student2)

    # Ожидаем исключение при коммите
    with pytest.raises(Exception):
        db_session.commit()

    # Явно делаем откат после исключения
    db_session.rollback()

    # Очистка - удаляем первого студента
    db_session.delete(student1)
    db_session.commit()
