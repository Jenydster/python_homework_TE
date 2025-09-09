from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Правильная строка подключения
DATABASE_URL = "postgresql://postgres:Jeny15@localhost:5432/postgres"

# Создаем движок БД
engine = create_engine(DATABASE_URL, echo=True)

# Создаем фабрику сессий
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Базовый класс для моделей
Base = declarative_base()


# Функция для получения сессии
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
