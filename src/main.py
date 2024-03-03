# import argparse
# import os
import asyncio

from config_loader import load_config
from utils import get_args
from edu_bot import EduBot


async def main() -> None:
    try:
        args = get_args()
        config = load_config(args.config)
    except:
        print('Видимо используется не VSCode')
        config = load_config("config.yaml")
    edu_bot = EduBot(config)

    await edu_bot.start()


if __name__ == "__main__":
    asyncio.run(main())
