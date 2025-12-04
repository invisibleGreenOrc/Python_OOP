class NegativeNumberError(Exception):
    def __init__(self, number, message):
        super().__init__(message)
        self.number = number
        self.message = message

    def __str__(self):
        return f"Недопустимое значение {self.number}. {self.message}"

def check_positive_number(number: float | int):
    if number < 0:
        raise NegativeNumberError(number, "Передано отрицательное число")
    

try:
    check_positive_number(1)
    check_positive_number(-1)
except NegativeNumberError as e:
    print(e)