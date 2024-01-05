

from telegram.ext.filters import MessageFilter
from .enums import GREETINGS


class GoPediaFilter(MessageFilter):
    is_available = False

    def filter(self, message):
        for greeting in GREETINGS:
            self.is_available = greeting in message.text.upper()
            if self.is_available:
                break
        return self.is_available
