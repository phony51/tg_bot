from aiogram.filters import BaseFilter
from aiogram.types import Message


class MinAgeFilter(BaseFilter):
    def __init__(self, min_age: int) -> None:
        self.min_age = min_age

    async def __call__(self, message: Message) -> bool:
        return int(message.text) >= self.min_age
