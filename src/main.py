import asyncio
import logging

from config.config_loader import load_config
from edu_bot import EduBot
from utils import get_args

# Подключаем логированиеpip install pipreqs
logger = logging.getLogger(__name__)


async def main() -> None:
    # Конфигурируем логирование
    logging.basicConfig(level=logging.INFO,
                        format='%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s')
    # Выводим в консоль информацию о начале запуска бота
    logger.info('Starting bot')
    args = get_args()
    config = load_config(args.config)
    edu_bot = EduBot(config)
    await edu_bot.start()


if __name__ == "__main__":
    asyncio.run(main())
