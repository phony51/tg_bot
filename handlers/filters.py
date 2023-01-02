import re

from aiogram.filters import BaseFilter
from aiogram.types import Message


class ContainFilter(BaseFilter):
    def __init__(self, values: int) -> None:
        self.values = values

    async def __call__(self, message: Message) -> bool:
        return message.text in self.values


class RegexFilter(BaseFilter):
    def __init__(self, regex: str) -> None:
        self.regex = regex

    async def __call__(self, message: Message) -> bool:
        return bool(re.fullmatch(self.regex, message.text))
