class Bizexception(Exception):
    def __init__(self, error_code, message):
        super().__init__(message)  # 调用基类的构造函数
        self.message = message
        self.error_code = error_code

    def __str__(self):
        if self.error_code:
            return f"{super().__str__()} (Error Code: {self.error_code})"
        return super().__str__()