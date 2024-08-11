# Hello_pk_assistant

pk Assistant is a voice-activated virtual assistant that uses Google's Generative AI to provide responses and perform various actions on your computer. It listens for the activation phrase "hello pk" and then waits for your command. 

## Features

- **Voice Activation**: Activates on hearing "hello pk".
- **Voice Commands**: Responds to various commands like opening calculator, notepad, Chrome, YouTube, and playing videos.
- **Generative AI**: Uses Google's Generative AI to provide responses to queries.
- **Text-to-Speech**: Reads out the responses using pyttsx3.
- **Speech Recognition**: Uses Google Web Speech API for recognizing spoken commands.

## Requirements

- Python 3.6 or higher
- `google-generativeai` package
- `pyttsx3` package
- `speech_recognition` package
- Microphone for voice input

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your_username/pk-assistant.git
    cd pk-assistant
    ```

2. Install the required packages:
    ```sh
    pip install google-generativeai pyttsx3 speechrecognition
    ```

3. Get an API key for Google Generative AI and replace `"Your_api_key"` in the script with your actual API key.

## Usage

1. Run the script:
    ```sh
    python pk_assistant.py
    ```

2. Speak the activation phrase "hello pk" followed by your command. For example, say "hello pk, open calculator" or "hello pk, open YouTube".

3. The assistant will respond to the command accordingly and perform the desired action.

## Commands

- **Open Calculator**: Opens the calculator application.
- **Open Notepad**: Opens the notepad application.
- **Open Chrome**: Opens Google Chrome.
- **Open YouTube**: Opens YouTube in the default web browser.
- **Play [video]**: Plays a specific video on YouTube.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

1. Fork the repository.
2. Create your feature branch:
    ```sh
    git checkout -b feature/AmazingFeature
    ```
3. Commit your changes:
    ```sh
    git commit -m 'Add some AmazingFeature'
    ```
4. Push to the branch:
    ```sh
    git push origin feature/AmazingFeature
    ```
5. Open a pull request.

## Acknowledgments

- [Google Generative AI](https://cloud.google.com/generative-ai)
- [pyttsx3](https://pypi.org/project/pyttsx3/)
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)

