# Chatbot generation template for unit test creation

import logging

from besser.bot.core.bot import Bot
from besser.bot.core.session import Session

# Configure the logging module
logging.basicConfig(level=logging.INFO, format='{levelname} - {asctime}: {message}', style='{')

# Create the bot
bot = Bot('unit-test-bot-dialogue')
bot.load_properties('config.ini')
websocket_platform = bot.use_websocket_platform(use_ui=True)

# STATES
central_state = bot.new_state('central_state', initial=True)

state_1 = bot.new_state('state_1')

state_2 = bot.new_state('state_2')

state_3 = bot.new_state('state_3')

state_4 = bot.new_state('state_4')

state_5 = bot.new_state('state_5')

state_6 = bot.new_state('state_6')

state_7 = bot.new_state('state_7')

state_8 = bot.new_state('state_8')


# INTENTS

state_1_intent = bot.new_intent('state_1_intent', [
    
    "I want to test a function"
    
])

state_2_intent = bot.new_intent('state_2_intent', [
    
    "What is the name of the function?"
    
])

state_3_intent = bot.new_intent('state_3_intent', [
    
    "Please provide the name of the function you want to test."
    
])

state_4_intent = bot.new_intent('state_4_intent', [
    
    "What parameters does {{function_name}} take?"
    
])

state_5_intent = bot.new_intent('state_5_intent', [
    
    "{{function_name}} takes two integers"
    
])

state_6_intent = bot.new_intent('state_6_intent', [
    
    "It should return the sum of both integers"
    
])

state_7_intent = bot.new_intent('state_7_intent', [
    
    "If either parameter is null, {{function_name}} should return zero"
    
])

state_8_intent = bot.new_intent('state_8_intent', [
    
    "Yes, please"
    
])


# STATES BODIES + TRANSITIONS
def central_state_body(session: Session):
    session.reply("Welcome to the Unit Test Assistant. How can I assist you in creating your unit tests?")
central_state.set_body(central_state_body)


def state_1_body(session: Session):
    session.reply("What_function_would_you_like_to_test_today_")
    session.go_to(central_state)

state_1.set_body(state_1_body)
central_state.when_intent_matched_go_to(state_1_intent, state_1)

def state_2_body(session: Session):
    session.reply("Please_provide_the_name_of_the_function_you_want_to_test_")
    session.go_to(central_state)

state_2.set_body(state_2_body)
central_state.when_intent_matched_go_to(state_2_intent, state_2)

def state_3_body(session: Session):
    session.reply("What_parameters_does___function_name___take_")
    session.go_to(central_state)

state_3.set_body(state_3_body)
central_state.when_intent_matched_go_to(state_3_intent, state_3)

def state_4_body(session: Session):
    session.reply("Please_describe_the_parameters___function_name___takes_")
    session.go_to(central_state)

state_4.set_body(state_4_body)
central_state.when_intent_matched_go_to(state_4_intent, state_4)

def state_5_body(session: Session):
    session.reply("What_should___function_name___return_under_normal_circumstances_")
    session.go_to(central_state)

state_5.set_body(state_5_body)
central_state.when_intent_matched_go_to(state_5_intent, state_5)

def state_6_body(session: Session):
    session.reply("Do_you_want_to_specify_any_conditions_for___function_name___")
    session.go_to(central_state)

state_6.set_body(state_6_body)
central_state.when_intent_matched_go_to(state_6_intent, state_6)

def state_7_body(session: Session):
    session.reply("Great__I_have_all_the_information__Would_you_like_me_to_generate_the_test_for___function_name___now_")
    session.go_to(central_state)

state_7.set_body(state_7_body)
central_state.when_intent_matched_go_to(state_7_intent, state_7)

def state_8_body(session: Session):
    session.reply("Generating_your_test_case_for___function_name_____")
    session.go_to(central_state)

state_8.set_body(state_8_body)
central_state.when_intent_matched_go_to(state_8_intent, state_8)


# Adding a fallback state to handle unmatched intents
fallback_state = bot.new_state('fallback_state')
def fallback_state_body(session: Session):
    session.reply("I'm sorry, I didn't understand that. Can you please rephrase?")
    session.go_to(central_state)

fallback_state.set_body(fallback_state_body)

# RUN APPLICATION
if __name__ == '__main__':
    bot.run()