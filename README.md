# Bot4UnitTesting
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
    git clone https://github.com/yourusername/Bot4UnitTesting.git
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


## Interaction Flow

1. The bot will greet you and ask how it can assist you.
2. Provide the function name, parameters, expected results, conditions, programming language, and JUnit version as prompted.
3. Upload the class file when requested.
4. The bot will generate the unit test cases and ask you to validate them.
5. Validate or provide modifications as needed.

### Example

**User**: I need to write tests for a function  
**Bot**: What is the name of the function you want to test?  
**User**: The function name is addNumbers  
**Bot**: Please provide the parameters for the function.  
**User**: It takes two integers as parameters  
**Bot**: What should the function return under normal circumstances?  
**User**: It should return the sum of both integers  
**Bot**: Do you want to specify any conditions for the function?  
**User**: If the parameter is null, it should return zero  
**Bot**: What is the programming language of the function?  
**User**: The programming language is Java  
**Bot**: Which JUnit version are you using?  
**User**: The JUnit version is 4  
**Bot**: Please upload the class file or paste the class code for the function.  
**User**: *Uploads the class file.*  
**Bot**: Generated test case: ... Are these tests correct? If not, what would you like to modify?

## Contribution

Feel free to fork the repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

This project was developed as part of the course "Advanced Software Development: Building Your Own (Intelligent) Low-Code Platform" taught by Jordi Cabot. Special thanks to the BESSER project for providing the bot framework.

