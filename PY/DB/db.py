from sqlalchemy import create_engine, Column, Integer, String, Date, Float, DateTime, ForeignKey, Table, func
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from datetime import datetime

Base = declarative_base()

# Промежуточная таблица для связи многие-ко-многим Child и Ingredient
child_allergens = Table(
    'child_allergens', Base.metadata,
    Column('child_id', Integer, ForeignKey('children.id'), primary_key=True),
    Column('ingredient_id', Integer, ForeignKey('ingredients.id'), primary_key=True)
)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    children = relationship("Child", back_populates="user")

class Child(Base):
    __tablename__ = 'children'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    name = Column(String, nullable=False)
    birth_date = Column(Date, nullable=False)
    gender = Column(String, nullable=False)
    height = Column(Float)
    weight = Column(Float)
    allergens = relationship("Ingredient", secondary=child_allergens, back_populates="children")
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    user = relationship("User", back_populates="children")

class IngredientCategory(Base):
    __tablename__ = 'ingredient_categories'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)
    ingredients = relationship("Ingredient", back_populates="category")

class Ingredient(Base):
    __tablename__ = 'ingredients'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)
    category_id = Column(Integer, ForeignKey('ingredient_categories.id'))
    category = relationship("IngredientCategory", back_populates="ingredients")
    children = relationship("Child", secondary=child_allergens, back_populates="allergens")

class DatabaseManager:
    def __init__(self):
        self.engine = create_engine('sqlite:///myapp2.db')
        Base.metadata.create_all(self.engine)

def populate_initial_data():
    """Заполнение базы данных начальными значениями"""
    engine = create_engine('sqlite:///myapp2.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    try:
        with Session() as session:
            categories = [
                "Овощи", "Фрукты", "Молочные продукты",
                "Мясо", "Рыба", "Зерновые", "Специи",
                "Орехи и семена", "Напитки", "Мучные изделия"
            ]

            existing_categories = {c.name for c in session.query(IngredientCategory.name).all()}
            new_categories = [IngredientCategory(name=cat) for cat in categories if cat not in existing_categories]

            if new_categories:
                session.add_all(new_categories)
                session.commit()
                print(f"Добавлено категорий: {len(new_categories)}")
            else:
                print("Категории уже существуют.")

    except Exception as e:
        print(f"Ошибка при заполнении данных: {e}")
        session.rollback()

if __name__ == '__main__':
    db_manager = DatabaseManager()
    populate_initial_data()