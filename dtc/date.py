from datetime import date, datetime

from .base import Base


class Date(Base):
    """
    Конвертация даты
    """

    def __init__(self, value: date):
        super().__init__(value)

    def datetime(self) -> datetime:
        return datetime.combine(self.value, datetime.min.time())

    def date(self) -> date:
        return self.value

    def dstring(self) -> str:
        return self.value.strftime('%d.%m.%Y')

    def dtstring(self) -> str:
        return self.datetime().strftime('%d.%m.%Y %H:%M:%S')
    