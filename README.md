# HealthSAGE

Welcome to the Healthcare Assistant Chatbot project!

The Healthcare Assistant Chatbot is an intelligent chatbot designed to provide probable diagnoses based on user interactions and symptoms. It utilizes the power of natural language processing and the GPT-3.5 language model to generate accurate and helpful responses.

## Features

- **Probable Diagnosis:** Get a probable diagnosis based on the symptoms provided by the user.
- **Natural Language Interaction:** Engage in natural language conversations with the chatbot.
- **Easy-to-Use Interface:** Simple and intuitive user interface for interacting with the chatbot.

## Project Setup

To use the Healthcare Assistant Chatbot locally, follow these steps:

1. Clone the repository: 
```
git clone https://github.com/squirrellovespie/HealthSAGE.git
```

2. Install the required dependencies. Make sure you have Python and pip installed, then run the following command: 
```
pip install -r requirements.txt
```

3. Set up your OpenAI API credentials by replacing YOUR_API_KEY in app.py with your actual OpenAI API key.

4. Run the application:
```
streamlit run main.py
```

5. The URL will automatically open after the command is executed.

## Usage

1. Enter your symptoms or describe the problem in the text input field.

2. Click the "Get Diagnosis" button.

3. The chatbot will generate a probable diagnosis based on the provided symptoms.

Please note that the diagnosis provided by the chatbot is for informational purposes only and should not substitute professional medical advice. Always consult a healthcare professional for accurate diagnosis and treatment.

## Contributing

Contributions to the Healthcare Assistant Chatbot project are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

1. The project utilizes the OpenAI GPT-3.5 language model for generating responses.
   
2. Thanks to the Streamlit community for providing a user-friendly framework for building web applications.
