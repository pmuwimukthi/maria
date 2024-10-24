from ollama import Client
from memory_utils import get_conversation_history, update_memory

ollama_client = Client()

def initialize_conversation():
    return get_conversation_history()

def generate_response(messages):
    response = ollama_client.chat(model='llama3.1:latest', messages=messages)
    update_memory(messages[-2:])  # Save the last user message and AI response
    return response['message']['content']
