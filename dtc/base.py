from abc import ABC, abstractmethod


class Base(ABC):
    """
    Базовый класс конвертации
    """

    def __init__(self, value: any):
        self.value = value

    def __repr__(self):
        return self.value

    @abstractmethod
    def datetime(self):
        """
        Преобразование self.value в datetime
        :return: datetime | None
        """
        pass

    @abstractmethod
    def date(self):
        """
        Преобразование self.value в date
        :return: date | None
        """
        pass

    @abstractmethod
    def dstring(self):
        """
        Date string - преобразование self.value в str (формат ДД.ММ.ГГГГ)
        :return: str | None
        """
        pass

    @abstractmethod
    def dtstring(self):
        """
        DateTime string - преобразование self.value в str (формат ДД.ММ.ГГГГ ЧЧ:ММ:СС)
        :return: str | None
        """
        pass
