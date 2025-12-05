from exceptions import UserAlreadyExistsError, UserNotFoundError

class User:
    def __init__(self, username: str, email: str, age: int):
        self.username = username
        self.email = email
        self.age = age

    def __str__(self):
        return f"Пользователь: {self.username}, email: {self.email}, возраст: {self.age}"
    
class UserManager:
    users: dict[str, User] = {}

    def add_user(self, user: User) -> None:
        """
        Добавляет пользователя.
        """
        if user.username in UserManager.users:
            raise UserAlreadyExistsError(user.username)
        
        UserManager.users[user.username] = user

    def remove_user(self, username: str) -> None:
        """
        Удаляет пользователя.
        """
        if UserManager.users.pop(username, None) is None:
            raise UserNotFoundError(username)
        
    def find_user(self, username: str) -> User:
        """
        Возвращает пользователя.
        """
        if (user:= UserManager.users.pop(username, None)) is None:
            raise UserNotFoundError(username)
        
        return user