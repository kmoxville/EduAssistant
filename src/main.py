# import argparse
# import os
import asyncio

from config_loader import load_config
from utils import get_args
from edu_bot import EduBot


async def main() -> None:
    args = get_args()
    config = load_config(args.config)
    edu_bot = EduBot(config)
    await edu_bot.start()


if __name__ == "__main__":
    asyncio.run(main())
