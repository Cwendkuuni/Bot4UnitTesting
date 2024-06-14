# Bot4UnitTesting

## Objective
Develop a bot using the BESSER Bot Framework to assist in creating unit tests for functions. The bot will use OpenAI's GPT-3.5-turbo model to generate unit test cases based on user inputs and uploaded class files.

## Features
- **Interactive Dialogue**: The bot interacts with users to gather information about the function they want to test.
- **Function Details Extraction**: The bot extracts details such as function name, parameters, expected results, programming language, and JUnit version.
- **File Upload**: Users can upload class files which the bot processes to generate unit tests.
- **Test Case Generation**: The bot uses GPT-3.5-turbo to generate unit test cases based on the provided information and class content.
- **Validation Step**: After generating the test cases, the bot asks the user to validate or modify the tests if needed.

## Usage

### Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/Cwendkuuni/Bot4UnitTesting.git
    ```
2. Navigate to the project directory:
    ```sh
    cd Bot4UnitTesting
    ```
3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```
4. Create a `.env` file and add your OpenAI API key:
    ```sh
    OPENAI_API_KEY=your_openai_api_key
    ```

### Run the Bot

Start the bot:
```sh
python3 test_bot.py
```

## Interaction Flow

1. The bot will greet you and ask how it can assist you.
2. Provide the function name, parameters, expected results, conditions, programming language, and JUnit version as prompted.
3. Upload the class file when requested.
4. The bot will generate the unit test cases and ask you to validate them.
5. Validate or provide modifications as needed.

### Example

- :bust_in_silhouette: **User:** I need to write tests for a function
- :robot: **Bot:** What is the name of the function you want to test?
- :bust_in_silhouette: **User:** The function name is addNumbers
- :robot: **Bot:** Please provide the parameters for the function.
- :bust_in_silhouette: **User:** It takes two integers as parameters
- :robot: **Bot:** What should the function return under normal circumstances?
- :bust_in_silhouette: **User:** It should return the sum of both integers
- :robot: **Bot:** Do you want to specify any conditions for the function?
- :bust_in_silhouette: **User:** If the parameter is null, it should return zero
- :robot: **Bot:** What is the programming language of the function?
- :bust_in_silhouette: **User:** The programming language is Java
- :robot: **Bot:** Which JUnit version are you using?
- :bust_in_silhouette: **User:** The JUnit version is 4
- :robot: **Bot:** Please upload the class file or paste the class code for the function.
- :bust_in_silhouette: **User:** Uploads the class file.
- :robot: **Bot:** Generated test case: ... Are these tests correct? If not, what would you like to modify?

## Limitations

- The bot currently supports only Java and JUnit for unit test generation.
- The bot relies on the correctness of user inputs to generate accurate test cases.
- The test cases generated are based on the information provided and may not cover all edge cases or specific requirements.
- Limited support for complex class structures and dependencies.

## Future Features

- Support for additional programming languages (e.g., Python, C#).
- Integration with other testing frameworks.
- Enhanced validation and error-checking mechanisms for user inputs.
- Automated handling of more complex class structures and dependencies.
- Improved user interface for better interaction and ease of use.

## References
- [BESSER-Bot-Framework](https://github.com/BESSER-PEARL/BESSER-Bot-Framework)
- [BESSER Bot Framework Documentation](https://besserbot-framework.readthedocs.io/en/latest/)

## Contribution

Feel free to fork the repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

This project was developed as part of the course "Advanced Software Development: Building Your Own (Intelligent) Low-Code Platform" taught by Jordi Cabot. Special thanks to the BESSER project for providing the bot framework.

