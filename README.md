# Maria

Maria is an innovative chatbot designed to provide companionship and support, especially for those who may find themselves alone, such as the elderly or individuals without immediate family care. Developed in Python, Maria operates entirely locally, ensuring user privacy. It utilizes the Ollama for text completion and Pyttsx3 for text-to-speech functionalities, engaging users in seamless conversation by transcribing their speech and replying vocally. This program is released under the Apache 2.0 License, emphasizing its commitment to user privacy and open-source collaboration.

## Features

- Operates 100% locally to protect user privacy.
- Engages in natural conversations with text-to-speech capabilities.
- Recommended LLM: Llama3.1 8B.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a Virtual Environment:**
   We recommend using Anaconda (optional).
   ```bash
   conda create -n maria python=3.12.4 -y
   conda activate maria
   ```

3. **Install the Requirements:**
   ```bash
   pip install -r requirements.txt
   ```

## How to Run

1. **Activate the Virtual Environment:**
   ```bash
   conda activate maria
   ```

2. **Run the Program:**
   Navigate to the directory where you cloned the repository and execute:
   ```bash
   python main.py
   ```

3. **Interact with Maria:**
   - Speak to Maria, and she will respond vocally.
   - Press `Ctrl+Q` to clear the conversation memory.
   - Press `Ctrl+C` to stop the program.

## Clearing Memory

To clear the conversation memory during a session, press `Ctrl+Q`. This will reset the conversation, allowing you to start fresh.

## Stopping the Program

To stop the program, press `Ctrl+C` in the terminal where the program is running.

## License

This project is licensed under the Apache 2.0 License. See the [LICENSE](LICENSE) file for more details.
