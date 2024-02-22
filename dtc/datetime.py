from datetime import datetime, date

from .base import Base


class DateTime(Base):
    """
    Конвертация даты/времени
    """

    def __init__(self, value: datetime):
        super().__init__(value)

    def datetime(self) -> datetime:
        return self.value

    def date(self) -> date:
        return self.value.date()

    def dstring(self) -> str:
        return self.value.strftime('%d.%m.%Y')

    def dtstring(self) -> str:
        return self.value.strftime('%d.%m.%Y %H:%M:%S')
