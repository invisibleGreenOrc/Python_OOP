from users import UserManager, User
from exceptions import UserAlreadyExistsError, UserNotFoundError

user_manager = UserManager()

try:
    user_manager.add_user(User("Olga", "Olga@mail.ru", 19))
    user_manager.add_user(User("Olga", "Olga@mail.ru", 19))
except UserAlreadyExistsError as e:
    print(e)
except Exception as e:
    print("Неожиданная ошибка.", e)

try:
    user_manager.remove_user("Oleg")
except UserNotFoundError as e:
    print(e)
except Exception as e:
    print("Неожиданная ошибка.", e)

try:
    user_manager.find_user("Oleg")
except UserNotFoundError as e:
    print(e)
except Exception as e:
    print("Неожиданная ошибка.", e)