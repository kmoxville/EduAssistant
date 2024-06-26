# import argparse
# import utils
import asyncio

from src.config.config import Config
from edu_bot import EduBot
from utils import *


async def main() -> None:
    args = get_args()
    config = Config(args.token)
    edu_bot = EduBot(config)

    await edu_bot.start()


if __name__ == "__main__":
    asyncio.run(main())
