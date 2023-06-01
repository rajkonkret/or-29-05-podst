class MyException(Exception):
    def __init__(self, message):
        super().__init__(message)


try:
    raise MyException("wystąpił bład")  # MyException: wystąpił bład
except Exception as e:
    print(e)  # wystąpił bład

# 11:25
