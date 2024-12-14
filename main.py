import logging
import os

from dotenv import load_dotenv
from planetarion_bot.bot.bot import Bot

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

if __name__ == '__main__':
    load_dotenv()
    current_round = os.getenv('CURRENT_ROUND')
    config = {
        'files': {
            'stats': os.path.abspath(f'stats/{current_round}.xml'),
        }
    }
    bot = Bot(os.getenv('TG_TOKEN'), os.getenv('CHAT_ID'), config)
