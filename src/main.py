import asyncio
import logging

from aiogram import Dispatcher

from config_loader import load_config
from edu_bot import EduBot
from utils import get_args

dp = Dispatcher()
# Подключаем логирование
logger = logging.getLogger(__name__)


async def main(dispatcher) -> None:
    # Конфигурируем логирование
    logging.basicConfig(level=logging.INFO,
                        format='%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s')
    # Выводим в консоль информацию о начале запуска бота
    logger.info('Starting bot')
    args = get_args()
    config = load_config(args.config)
    edu_bot = EduBot(config)
    # Настраиваем главное меню бота

    await edu_bot.start()
    await dispatcher.start_polling(edu_bot)


if __name__ == "__main__":
    asyncio.run(main(dp))
