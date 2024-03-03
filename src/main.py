import argparse
import asyncio
import os

from config_loader import load_config
from edu_bot import EduBot
from utils import get_args

async def main() -> None:
    args = get_args()
    config = load_config(args.config)
    edu_bot = EduBot(config)

    await edu_bot.start()

if __name__ == "__main__":
    asyncio.run(main())