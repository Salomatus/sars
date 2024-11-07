class ConversionError(Exception):
    """Класс ошибки конвертации валюты"""

    def __init__(self, *args: str) -> None:
        """Конструктор сущности исключения"""
        self.message: str = args[0] if args else "Ошибка конвертации валюты"

    def __str__(self) -> str:
        """Строковое представление экземпляра класса"""
        return self.message
