import sqlite3

def initiate_db():
    """Создает таблицы Products и Users, если они еще не существуют."""
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()

    # Таблица Products
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            price INTEGER NOT NULL
        )
    ''')

    # Таблица Users
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            age INTEGER NOT NULL,
            balance INTEGER NOT NULL
        )
    ''')

    connection.commit()
    connection.close()

def add_user(username, email, age):
    """Добавляет нового пользователя в таблицу Users."""
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()
    cursor.execute('''
        INSERT INTO Users (username, email, age, balance)
        VALUES (?, ?, ?, ?)
    ''', (username, email, age, 1000))
    connection.commit()
    connection.close()

def is_included(username):
    """Проверяет наличие пользователя с заданным именем в таблице Users."""
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Users WHERE username = ?', (username,))
    result = cursor.fetchone()
    connection.close()
    return result is not None

def get_all_products():
    """Возвращает все записи из таблицы Products."""
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()
    cursor.execute('SELECT id, title, description, price FROM Products')
    products = cursor.fetchall()
    connection.close()
    return products