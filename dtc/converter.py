from datetime import datetime, date, timedelta, timezone

from .base import Base
from .date import Date
from .datetime import DateTime
from .tools import clear_string, convert


class DTConvert(Base):

    def __init__(self, value: any = None):
        super().__init__(value)
        if self.value:
            if isinstance(self.value, datetime):
                self._model_ = DateTime(self.value)
            elif isinstance(self.value, date):
                self._model_ = Date(self.value)
            elif isinstance(self.value, str):
                self._model_ = convert(clear_string(self.value))
            else:
                self._model_ = None
        else:
            delta = timedelta(hours=3, minutes=0)
            self._model_ = DateTime(datetime.now(timezone.utc) + delta)

    @property
    def datetime(self):
        return self._model_.datetime() if self._model_ else None

    @property
    def date(self):
        return self._model_.date() if self._model_ else None

    @property
    def dstring(self):
        return self._model_.dstring() if self._model_ else None

    @property
    def dtstring(self):
        return self._model_.dtstring() if self._model_ else None
