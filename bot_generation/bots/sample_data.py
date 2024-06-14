# Chatbot generation template

import logging

from besser.bot.core.bot import Bot
from besser.bot.core.session import Session
from besser.bot.nlp.intent_classifier.intent_classifier_prediction import IntentClassifierPrediction

# Configure the logging module
logging.basicConfig(level=logging.INFO, format='{levelname} - {asctime}: {message}', style='{')

# Create the bot
bot = Bot('sample_data')
bot.load_properties('config.ini')
websocket_platform = bot.use_websocket_platform(use_ui=True)

# STATES
central_state = bot.new_state('central_state', initial=True)

state_1 = bot.new_state('state_1')

state_2 = bot.new_state('state_2')

state_3 = bot.new_state('state_3')


# INTENTS

state_1_intent = bot.new_intent('state_1_intent', [
    
    "I need help"
    
])

state_2_intent = bot.new_intent('state_2_intent', [
    
    "help", 
    
    "help please"
    
])

state_3_intent = bot.new_intent('state_3_intent', [
    
    "What is the weather?"
    
])


# STATES BODIES + TRANSITIONS
def central_state_body(session: Session):
    session.reply("How can I assist you?")
    return None

central_state.set_body(central_state_body)


def state_1_body(session: Session):
    session.reply("this is the help message")
    return central_state

state_1.set_body(state_1_body)
central_state.when_intent_matched_go_to(state_1_intent, state_1)


def state_2_body(session: Session):
    session.reply("")
    return central_state

state_2.set_body(state_2_body)
central_state.when_intent_matched_go_to(state_2_intent, state_2)


def state_3_body(session: Session):
    session.reply("it is 23 degrees")
    return central_state

state_3.set_body(state_3_body)
central_state.when_intent_matched_go_to(state_3_intent, state_3)



# RUN APPLICATION
if __name__ == '__main__':
    bot.run()