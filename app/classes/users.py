from abc import ABC
import hashlib

class User(ABC):
    """
    Базовый класс, представляющий пользователя.
    """
    users = [] # Список для хранения всех пользователей

    def __init__(self, username: str, email: str, password: str) -> None:
        self.username = username
        self.email = email
        self.password_hash = User.hash_password(password)

    @staticmethod
    def hash_password(password: str) -> str:
        """
        Хэширование пароля.
        """
        hash_obj = hashlib.sha256()
        hash_obj.update(password.encode('utf-8'))
        pass_hash = hash_obj.hexdigest()
        return pass_hash

    @staticmethod
    def check_password(password_hash: str, provided_password: str) -> bool:
        """
        Проверка пароля.
        """
        provided_password_hash = User.hash_password(provided_password)
        result = password_hash == provided_password_hash
        return result

    def get_details(self) -> str:
        return f"Пользователь: {self.username}, Email: {self.email}"

class Customer(User):
    """
    Класс, представляющий клиента, наследующий класс User.
    """
    def __init__(self, username: str, email: str, password: str, address: str):
        super().__init__(username, email, password)
        self.address = address

    def get_details(self) -> str:
        return f"Клиент: {self.username}, Email: {self.email}, Адрес: {self.address}"

class Admin(User):
    """
    Класс, представляющий администратора, наследующий класс User.
    """
    def __init__(self, username: str, email: str, password: str, admin_level: int):
        super().__init__(username, email, password)
        self.admin_level = admin_level

    def get_details(self) -> str:
        return f"Администратор: {self.username}, Email: {self.email}, Уровень: {self.admin_level}"

    @staticmethod
    def list_users() -> list[User]:
        """
        Выводит список всех пользователей.
        """
        return User.users

    @staticmethod
    def delete_user(username: str) -> tuple[bool, str]:
        """
        Удаляет пользователя по имени пользователя.
        """
        users = [user for user in User.users if user.username == username]
        
        if len(users) == 0:
            return (False, f"Пользователь {username} не найден.")

        User.users.remove(users[0])
        return (True, f"Пользователь {username} удален.")