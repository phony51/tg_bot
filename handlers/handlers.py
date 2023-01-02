from aiogram import Router

from handlers.registration.handlers import registration_router

start_router = Router()
start_router.include_router(registration_router)
