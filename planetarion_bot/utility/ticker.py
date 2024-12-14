import math
from datetime import datetime, timedelta

from telegram.ext import ContextTypes

from planetarion_bot.utility.attack import Attack


class Ticker:

    def __init__(self, chat_id=None, job_queue=None):
        self.chat_id = chat_id
        self.job_queue = job_queue
        self.round_start = datetime(2023, 10, 20, 20)
        self.interval = 3600

    def clear_attacks(self, context):
        if not context.chat_data and 'attacks' not in context.chat_data:
            context.chat_data['attacks'] = []
        att = Attack(context.chat_data['attacks'])
        att.attacks = [a for a in att.get() if int(a['land']) > self.get_current_tick()]
        context.chat_data['attacks'] = att.get()

    def get_current_tick(self):
        current = datetime.now()
        tick = math.floor((current - self.round_start).total_seconds() // self.interval)
        tick += 1  # To account for timezone diff.
        return tick

    @staticmethod
    def get_next_hour():
        dt = datetime.now() + timedelta(hours=1)
        return datetime(dt.year, dt.month, dt.day, dt.hour) - datetime.now()

    def start(self):
        if self.job_queue is not None:
            self.job_queue.run_repeating(self.tick, interval=self.interval, first=self.get_next_hour())

    async def tick(self, context: ContextTypes.DEFAULT_TYPE):
        tick = self.get_current_tick()
        self.clear_attacks(context)
        await context.bot.send_message(chat_id=self.chat_id, text=f'Tick {tick}')
