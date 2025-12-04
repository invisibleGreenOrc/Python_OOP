def validate_user_input(data: dict[str, str | int]) -> None:
    try:
        if not isinstance(data, dict):
            raise TypeError("Переданный аргумент не является словарем.")
        
        if not isinstance(data.get("name"), str):
            raise ValueError("Не передан name или name не строка")
        
        if not isinstance(age:= data.get("age"), int) or age <= 0:
            raise ValueError("Не передан age или age не положительное число")
    except BaseException as e:
        print(e)

validate_user_input({"name": "Alice", "age": 30})
validate_user_input({"age": 30})
validate_user_input({"name": "Alice", "age": -1})
validate_user_input({"name": "Alice", "age": "6"})
validate_user_input(("Alice", 6))
validate_user_input("Alice")