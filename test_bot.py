import os
from openai import OpenAI
from dotenv import load_dotenv
from besser.bot.core.bot import Bot
from besser.bot.core.session import Session
from besser.bot.core.file import File
from besser.bot.nlp.intent_classifier.intent_classifier_configuration import SimpleIntentClassifierConfiguration
import logging

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

# Configure the logging module
logging.basicConfig(level=logging.INFO, format='{levelname} - {asctime}: {message}', style='{')
logger = logging.getLogger(__name__)

# Function to generate test case using OpenAI API
def generate_test_with_chatgpt(function_details, file_content, language, junit_version=None):
    prompt = f"Generate unit tests for the following function details in {language}:\n{function_details}\n\nClass content:\n{file_content}"
    if junit_version:
        prompt += f"\nPlease use JUnit version {junit_version}."
    logger.info(f"Generated prompt for ChatGPT:\n{prompt}")
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant for generating unit tests."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()

# Create the bot
bot = Bot('Bot4UnitTesting')
bot.load_properties('config.ini')
websocket_platform = bot.use_websocket_platform(use_ui=True)

# Set default intent classifier configuration to Simple Intent Classifier
simple_ic_config = SimpleIntentClassifierConfiguration()
bot.set_default_ic_config(simple_ic_config)

# Define entities
function_name_entity = bot.new_entity('function_name_entity')
parameter_type_entity = bot.new_entity('parameter_type_entity')
parameter_name_entity = bot.new_entity('parameter_name_entity')
return_type_entity = bot.new_entity('return_type_entity')
condition_entity = bot.new_entity('condition_entity')
language_entity = bot.new_entity('language_entity')
junit_version_entity = bot.new_entity('junit_version_entity')

# STATES
initial_state = bot.new_state('initial_state', initial=True, ic_config=simple_ic_config)
awaiting_state = bot.new_state('awaiting_state', ic_config=simple_ic_config)
specify_function_state = bot.new_state('specify_function_state', ic_config=simple_ic_config)
define_parameters_state = bot.new_state('define_parameters_state', ic_config=simple_ic_config)
set_expected_results_state = bot.new_state('set_expected_results_state', ic_config=simple_ic_config)
add_test_condition_state = bot.new_state('add_test_condition_state', ic_config=simple_ic_config)
specify_language_state = bot.new_state('specify_language_state', ic_config=simple_ic_config)
specify_junit_version_state = bot.new_state('specify_junit_version_state', ic_config=simple_ic_config)
file_upload_state = bot.new_state('file_upload_state', ic_config=simple_ic_config)
generate_test_state = bot.new_state('generate_test_state', ic_config=simple_ic_config)
validate_test_state = bot.new_state('validate_test_state', ic_config=simple_ic_config)

# INTENTS
specify_function_intent = bot.new_intent('specify_function_intent', [
    'I want to test a function',
    'I need to write tests for a function',
    'Can you help me with testing a function'
])

define_parameters_intent = bot.new_intent('define_parameters_intent', [
    'The function takes parameters',
    'Here are the parameters for the function',
    'It accepts parameters'
])
define_parameters_intent.parameter('parameter', 'PARAM', parameter_name_entity)

set_expected_results_intent = bot.new_intent('set_expected_results_intent', [
    'The function should return',
    'Expected result of the function is',
    'It should return'
])
set_expected_results_intent.parameter('result', 'RESULT', return_type_entity)

add_test_condition_intent = bot.new_intent('add_test_condition_intent', [
    'If the parameter is null',
    'Under these conditions',
    'Test should include'
])
add_test_condition_intent.parameter('condition', 'COND', condition_entity)

specify_language_intent = bot.new_intent('specify_language_intent', [
    'The programming language is',
    'It is written in',
    'The code is in'
])
specify_language_intent.parameter('language', 'LANG', language_entity)

specify_junit_version_intent = bot.new_intent('specify_junit_version_intent', [
    'The JUnit version is',
    'JUnit version',
    'I am using JUnit version'
])
specify_junit_version_intent.parameter('junit_version', 'JUNIT', junit_version_entity)

generate_test_intent = bot.new_intent('generate_test_intent', [
    'Generate the test',
    'Create the test case',
    'Can you create the test'
])

validate_test_intent = bot.new_intent('validate_test_intent', [
    'The tests are correct',
    'The tests are fine',
    'The tests look good',
    'I want to modify the tests',
    'The tests need changes'
])

# STATES BODIES AND TRANSITIONS
def initial_state_body(session: Session):
    session.set('function_details', {})
    session.reply("Welcome to the Unit Test Assistant. I am a helpful assistant for generating unit tests.")

initial_state.set_body(initial_state_body)
initial_state.go_to(awaiting_state)  # Automatic transition to awaiting_state

def awaiting_state_body(session: Session):
    session.reply("How can I assist you?")

awaiting_state.set_body(awaiting_state_body)
awaiting_state.when_intent_matched_go_to(specify_function_intent, specify_function_state)
awaiting_state.when_intent_matched_go_to(define_parameters_intent, define_parameters_state)
awaiting_state.when_intent_matched_go_to(set_expected_results_intent, set_expected_results_state)
awaiting_state.when_intent_matched_go_to(add_test_condition_intent, add_test_condition_state)
awaiting_state.when_intent_matched_go_to(generate_test_intent, specify_language_state)

def specify_function_body(session: Session):
    session.reply("What is the name of the function you want to test?")

specify_function_state.set_body(specify_function_body)
specify_function_state.when_intent_matched_go_to(define_parameters_intent, define_parameters_state)

def define_parameters_body(session: Session):
    session.reply("Please provide the parameters for the function.")
    function_details = session.get('function_details')
    function_details['function_name'] = session.message
    session.set('function_details', function_details)

define_parameters_state.set_body(define_parameters_body)
define_parameters_state.when_intent_matched_go_to(set_expected_results_intent, set_expected_results_state)

def set_expected_results_body(session: Session):
    session.reply("What should the function return under normal circumstances?")
    function_details = session.get('function_details')
    function_details['parameters'] = session.message
    session.set('function_details', function_details)

set_expected_results_state.set_body(set_expected_results_body)
set_expected_results_state.when_intent_matched_go_to(add_test_condition_intent, add_test_condition_state)

def add_test_condition_body(session: Session):
    session.reply("Do you want to specify any conditions for the function?")
    function_details = session.get('function_details')
    function_details['expected_results'] = session.message
    session.set('function_details', function_details)

add_test_condition_state.set_body(add_test_condition_body)
add_test_condition_state.when_intent_matched_go_to(specify_language_intent, specify_language_state)

def specify_language_body(session: Session):
    session.reply("What is the programming language of the function?")
    function_details = session.get('function_details')
    function_details['conditions'] = session.message
    session.set('function_details', function_details)

specify_language_state.set_body(specify_language_body)
specify_language_state.when_intent_matched_go_to(specify_junit_version_intent, specify_junit_version_state)

def specify_junit_version_body(session: Session):
    session.reply("Which JUnit version are you using?")
    language = session.message
    session.set('language', language)

specify_junit_version_state.set_body(specify_junit_version_body)
specify_junit_version_state.when_intent_matched_go_to(generate_test_intent, file_upload_state)

def file_upload_body(session: Session):
    session.reply("Please upload the class file or paste the class code for the function.")

file_upload_state.set_body(file_upload_body)
file_upload_state.when_file_received_go_to(generate_test_state)

def generate_test_body(session: Session):
    file = session.file
    language = session.get('language')
    junit_version = session.get('junit_version')
    function_details = session.get('function_details')
    logger.info(f"Function details: {function_details}")
    
    if file:
        file_name = file.name
        session.reply(f"Received the file: {file_name}")
        # Preprocess the file and use context information to generate the test with ChatGPT
        test_case = generate_test_with_chatgpt(function_details, file.base64, language, junit_version)
        session.reply(f"Generated test case: {test_case}")
        session.move(validate_test_state)
    else:
        session.reply("No file received. Please upload the class file or paste the class code.")

generate_test_state.set_body(generate_test_body)
generate_test_state.when_no_intent_matched_go_to(awaiting_state)

def validate_test_body(session: Session):
    session.reply("Are these tests correct? If not, what would you like to modify?")

validate_test_state.set_body(validate_test_body)
validate_test_state.when_intent_matched_go_to(validate_test_intent, awaiting_state)

# Fallback body
def handle_user_message(session: Session):
    session.reply("Sorry, I didn't get it. Could you please rephrase?")
    session.move(awaiting_state)

# Set fallback bodies for states
awaiting_state.set_fallback_body(handle_user_message)
specify_function_state.set_fallback_body(handle_user_message)
define_parameters_state.set_fallback_body(handle_user_message)
set_expected_results_state.set_fallback_body(handle_user_message)
add_test_condition_state.set_fallback_body(handle_user_message)
specify_language_state.set_fallback_body(handle_user_message)
specify_junit_version_state.set_fallback_body(handle_user_message)
file_upload_state.set_fallback_body(handle_user_message)
generate_test_state.set_fallback_body(handle_user_message)
validate_test_state.set_fallback_body(handle_user_message)

# Start the bot
if __name__ == "__main__":
    bot.run() 
