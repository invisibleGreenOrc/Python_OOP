def convert_to_int(value: str) -> int:
    try:
        result = int(value)
        return result
    except ValueError as e:
        print("Невозможно преобразовать.", e)
    except BaseException as e:
        print("Неожиданная ошибка.", e)
    finally:
        print("Попытка преборазования завершена.")


convert_to_int("123")
convert_to_int("abc")
convert_to_int([1, 2, 3])