from planetarion_bot.ships.factory import Factory
from planetarion_bot.utility.attack import Attack
from planetarion_bot.utility.efficiency import Efficiency
from planetarion_bot.utility.ticker import Ticker
from planetarion_bot.utility.file import File
from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


class Bot:

    def __init__(self, token, chat_id, config=None):
        self.config = config
        application = ApplicationBuilder().token(token).build()
        application.add_handler(CommandHandler('att', self.attack))
        application.add_handler(CommandHandler('eff', self.calculate_eff))
        application.add_handler(CommandHandler(['start', 'help'], self.get_help))
        application.add_handler(CommandHandler('song', self.song))
        application.add_handler(CommandHandler('tick', self.update_tick))
        # application.add_handler(CommandHandler('s', self.store))
        # application.add_handler(CommandHandler('e', self.echo))
        Ticker(chat_id, application.job_queue).start()
        application.run_polling()

    async def get_help(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        message = """
        Commands
        
        <pre>/att</pre> - list current attacks
        <pre>/att add x y z</pre> - add attack (x=target, y=landing tick, z=ships to send)
        <pre>/att remove x</pre> - remove attack (x=ID)
        <pre>/eff x y</pre> - calculate efficiency of ships (x=number, y=name)
        <pre>/song</pre> - get current battle song
        <pre>/song x</pre> - set current battle song (x=youtube link)
        <pre>/tick</pre> - get current tick
        """

        await self.send_message(message, update, context, ParseMode.HTML)

    async def update_tick(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        ticker = Ticker()
        ticker.clear_attacks(context)
        await self.send_message(str(ticker.get_current_tick()), update, context)

    async def calculate_eff(self, update: Update, context: ContextTypes.DEFAULT_TYPE):

        if len(context.args) != 2:
            message = 'Example: /eff 100 harpy'
            await self.send_message(message, update, context)
            return

        count = context.args[0]

        if not count.isnumeric():
            message = f"'{count}' doesn't look like a number..."
            await self.send_message(message, update, context)
            return

        count = int(count)
        search = str(context.args[1])

        if count and search:
            file = File()
            eff = Efficiency(Factory(), file.get_stats(self.config['files']['stats']))
            message = eff.calculate(search, count)
            await self.send_message(message, update, context)
            return

        message = 'Oh gosh, something went unexpectedly wrong!'
        await self.send_message(message, update, context)

    async def attack(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        if 'attacks' not in context.chat_data:
            context.chat_data['attacks'] = []

        att = Attack(context.chat_data['attacks'])

        if len(context.args) > 0:
            match context.args[0]:
                case 'add':
                    a = {
                        'targ': context.args[1],
                        'land': int(context.args[2]),
                        'ship': context.args[3]
                    }
                    att.add(a)
                    context.chat_data['attacks'] = att.get()
                case 'remove':
                    att.remove(int(context.args[1]) - 1)
                    context.chat_data['attacks'] = att.get()

        if att.get():
            message = f'<pre>{att.get_formatted()}</pre>'
        else:
            message = 'There are no scheduled attacks.'

        await self.send_message(message, update, context, ParseMode.HTML)

    async def song(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        if context.args:
            context.chat_data['song'] = context.args[0]
        else:
            if 'song' in context.chat_data:
                message = context.chat_data['song']
            else:
                message = 'No song set. Use /song YOUTUBE_LINK to add a battle song.'

            await self.send_message(message, update, context)

    @staticmethod
    async def send_message(message, update, context, parse_mode=None):
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=message,
            parse_mode=parse_mode
        )

    @staticmethod
    async def store(context: ContextTypes.DEFAULT_TYPE):
        data = context.args[0]
        context.chat_data['message'] = data

    @staticmethod
    async def echo(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        message = context.chat_data['message']
        await context.bot.self.send_message(
            chat_id=update.effective_chat.id,
            text=message
        )
