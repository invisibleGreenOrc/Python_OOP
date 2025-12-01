from classes.users import User, Admin, Customer

class AuthenticationService:
    """
    Сервис для управления регистрацией и аутентификацией пользователей.
    """
    def __init__(self):
        self.current_user = None

    def register(self, user_class: str, username: str, email: str, password: str, **kwargs) -> tuple[bool, str]:
        """
        Регистрация нового пользователя.
        """
        if username in [user.username for user in User.users]:
            return (False, f"Имя пользователя {username} занято.")

        if user_class == "Customer":
            if "address" not in kwargs:
                return (False, "Не передан параметр 'address'.")
            
            new_user = Customer(username, email, password, kwargs["address"])
            User.users.append(new_user)

            return (True, f"Создан пользователь: '{new_user.get_details()}'.")

        elif user_class == "Admin":
            if "admin_level" not in kwargs:
                return (False, "Не передан параметр 'admin_level'.")
            
            new_user = Admin(username, email, password, kwargs["admin_level"])
            User.users.append(new_user)

            return (True, f"Создан пользователь: '{new_user.get_details()}'.")
        
        else:
            return (False, f"Передан неизвестный класс пользователя: '{user_class}'.")

    def login(self, username: str, password: str) -> tuple[bool, str]:
        """
        Аутентификация пользователя.
        """
        users = [user for user in User.users if user.username == username]

        if len(users) == 0:
            return (False, f"Пользователь: '{username}' не найден.")

        if not User.check_password(users[0].password_hash, password):
            return (False, "Неверный пароль.")
        
        self.current_user = users[0]
        return (True, "Вход выполнен.")

    def logout(self):
        """
        Выход пользователя из системы.
        """
        self.current_user = None

    def get_current_user(self) -> tuple[bool, str]:
        """
        Возвращает текущего вошедшего пользователя.
        """
        if self.current_user is None:
            return (False, "Пользователь не вошел.")

        return (True, f"Текущший пользователь: '{self.current_user.get_details()}'")
    
    def list_users(self) -> tuple[bool, str, list[User]]:
        """
        Выводит список всех пользователей.
        """
        if self.current_user is None:
            return (False, "Пользователь не вошел.", [])

        if isinstance(self.current_user, Admin):
            return (True, "", Admin.list_users())
        
        return (False, "Нет доступа.", [])
    
    def delete_users(self, username: str) -> tuple[bool, str]:
        """
        Выводит список всех пользователей.
        """
        if self.current_user is None:
            return (False, "Пользователь не вошел.")

        if isinstance(self.current_user, Admin):
            return Admin.delete_user(username)
        
        return (False, "Нет доступа.")