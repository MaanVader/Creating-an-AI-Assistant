### Create Your Own AI Assistant with Jarvis

#### Description
This project guides you through creating an AI assistant named Jarvis, inspired by Iron Man. The assistant listens for voice commands, processes them with a local language model, and responds using text-to-speech.

#### Features
- **Voice Activation**: The assistant listens for the wake word "Jarvis" to initiate command processing.
- **Speech Recognition**: Converts spoken language into text using Google Speech Recognition.
- **Natural Language Processing**: Processes commands with a local instance of an OpenAI-compatible language model.
- **Text-to-Speech**: Responds to commands with spoken language using pyttsx3.

#### How It Works
1. **Listening for Commands**: The assistant continuously listens for the wake word "Jarvis" using the microphone.
2. **Speech Recognition**: Upon detecting the wake word, the assistant uses Google Speech Recognition to convert the audio command into text.
3. **Processing Commands**: The text command is sent to an OpenAI-compatible language model running locally, which interprets and generates a response.
4. **Responding**: The response is converted back to speech and spoken out loud by the assistant.

#### Getting Started
To get started with this project, follow these steps:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/MaanVader/Creating-an-AI-Assistant.git
    cd Creating-an-AI-Assistant
    ```

2. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Configure the Language Model**:
    - Ensure you have an OpenAI-compatible language model server running locally.
    - Update the `interpreter.llm.api_base` in `jarvis2.py` to point to your local server.
    - Provide the necessary API key in `interpreter.llm.api_key`.

4. **Run the Assistant**:
    ```bash
    python jarvis2.py
    ```

#### Prerequisites
- Python 3.6+
- A working microphone
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [Pyttsx3](https://pypi.org/project/pyttsx3/)
- A local instance of an OpenAI-compatible language model

#### Customization
You can customize the assistant to recognize different wake words or commands by modifying the `listen_for_jarvis` function. Additionally, you can integrate more sophisticated NLP models or external APIs for enhanced capabilities.

#### Contributions
Contributions are welcome! Feel free to submit issues and pull requests to enhance the functionality and features of the AI assistant.

#### License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Happy coding! Build your personal AI assistant today and bring Jarvis to life in your home or workspace.
