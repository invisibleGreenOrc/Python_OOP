from classes.authentication_service import AuthenticationService

auth_service = AuthenticationService()

_, msg = auth_service.register("Customer", "IvanT", "ivan@mail.ru", "qwerty", address = "Omsk 5-6")
print(msg)
_, msg = auth_service.register("Customer", "KonstantinHO", "Kost@mail.ru", "123456", address = "Ufa 65-26")
print(msg)
_, msg = auth_service.register("Customer", "AnnaQ", "anna@mail.ru", "anna2005", address = "Rostov 52-7")
print(msg)

_, msg = auth_service.register("Admin", "RomanSA", "roman@mail.ru", "roman123", admin_level = 2)
print(msg)
_, msg = auth_service.register("Admin", "OlegH", "oleg@mail.ru", "Oleg2000", admin_level = 4)
print(msg)

_, msg = auth_service.register("Admin", "OlegH", "oleg@mail.ru", "Oleg2000", admin_level = 4)
print(msg)
_, msg = auth_service.register("SuperAdmin", "Oleg", "oleg@mail.ru", "Oleg2000", admin_level = 4)
print(msg)
_, msg = auth_service.register("Admin", "Oleg", "oleg@mail.ru", "Oleg2000")
print(msg)
_, msg = auth_service.register("Customer", "Oleg", "oleg@mail.ru", "Oleg2000")
print(msg)

# Пробуем выполнить до того, как пользователь вошел.
_, msg = auth_service.get_current_user()
print(msg)
_, msg, _ = auth_service.list_users()
print(msg)

# Ошибка в пароле.
_, msg = auth_service.login("IvanT", "qwerty1234")
print(msg)
# Ошибка в пароле.
_, msg = auth_service.login("IvanTTTT", "qwerty1234")
print(msg)
# Вход.
_, msg = auth_service.login("IvanT", "qwerty")
print(msg)

# Получаем текущего пользователя.
_, msg = auth_service.get_current_user()
print(msg)

# Пробуем получить список пользователь по клиентом.
_, msg, _ = auth_service.list_users()
print(msg)

auth_service.logout()
# Проверяем, что вышли.
_, msg = auth_service.get_current_user()
print(msg)

# Входим под админом
_, msg = auth_service.login("RomanSA", "roman123")
print(msg)
# Проверяем, что вошли.
_, msg = auth_service.get_current_user()
print(msg)
# Получаем список пользователей
is_success, msg, users = auth_service.list_users()
if is_success:
    print("Список пользователей:")
    print(* [user.get_details() for user in users], sep= "\n")

# Удаляем несуществующего пользователя.
_, msg = auth_service.delete_users("AnnaQ123123")
print(msg)

# Удаляем AnnaQ.
_, msg = auth_service.delete_users("AnnaQ")
print(msg)

# Проверяем, что нет AnnaQ.
is_success, msg, users = auth_service.list_users()
if is_success:
    print("Список пользователей:")
    print(* [user.get_details() for user in users], sep= "\n")