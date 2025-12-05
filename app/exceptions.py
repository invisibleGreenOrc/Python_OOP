class UserAlreadyExistsError(Exception):
    """
    Исключение, выбрасываемое, если пытаются добавить пользователя с уже существующим именем.
    """
    def __init__(self, username: str):
        self.username = username

    def __str__(self) -> str:
        return f"Пользователь с username {self.username} уже существует, невозможно добавить."

class UserNotFoundError(Exception):
    """
    ИИсключение, выбрасываемое, если пользователь с указанным именем не найден.
    """
    def __init__(self, username: str):
        self.username = username

    def __str__(self) -> str:
        return f"Пользователь с username {self.username} не найден."