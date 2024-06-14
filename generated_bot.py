import logging
from besser.bot.core.bot import Bot
from besser.bot.core.session import Session

logging.basicConfig(level=logging.INFO, format='{levelname} - {asctime}: {message}', style='{')

bot = Bot('')
websocket_platform = bot.use_websocket_platform(use_ui=True)



initial_state = bot.new_state('initial_state', initial=True)
initial_state.set_body(lambda session: session.reply("How can I assist you?"))



if __name__ == '__main__':
    bot.run()