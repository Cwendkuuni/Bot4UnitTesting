import importlib
import re

import numpy as np
import streamlit as st

from pandas import DataFrame

from jinja2 import Environment, FileSystemLoader


def generate_bot(bot_name: str, df: DataFrame):
    st.subheader('Data preview')
    st.dataframe(df)

    # Replace NaN values with empty strings
    df = df.fillna('')

    # Function to sanitize state names
    def sanitize_name(name):
        return re.sub(r'\W|^(?=\d)', '_', name)

    # Step 1: Parse the CSV file
    intents = {}
    states = {}
    
    for index, row in df.iterrows():
        question = row['question'].strip()
        answer = row['answer'].strip()
        
        sanitized_answer = sanitize_name(answer)
        
        if sanitized_answer not in states:
            state_name = f"state_{len(states) + 1}"
            states[sanitized_answer] = state_name
        else:
            state_name = states[sanitized_answer]

        if state_name not in intents:
            intents[state_name] = []

        intents[state_name].append(question)
    
    # Step 2: Create a JSON-like dictionary
    data = {
        'bot_name': bot_name,
        'intents': intents,
        'states': states
    }

    # Step 3: Render the Jinja template
    env = Environment(loader=FileSystemLoader(''))
    template = env.get_template('bot_generation/generator/bot_generation.py.j2')
    rendered_code = template.render(data)
    
    # Step 4: Save the rendered template
    with open(f'bot_generation/bots/{bot_name}.py', 'w') as file:
        file.write(rendered_code)

    # Import the generated module and return the bot
    gen_module = importlib.import_module(f'bot_generation.bots.{bot_name}')
    return gen_module.bot
