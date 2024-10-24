import json
import os

MEMORY_FILE = "conversation_memory.json"
MAX_MEMORY = 20

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    return []

def save_memory(messages):
    with open(MEMORY_FILE, "w") as f:
        json.dump(messages, f)

def update_memory(messages):
    memory = load_memory()
    memory.extend(messages[1:])  # Exclude the system message
    memory = memory[-MAX_MEMORY:]  # Keep only the last MAX_MEMORY messages
    save_memory(memory)

def get_conversation_history():
    memory = load_memory()
    system_message = [{'role': 'system', 'content': '''Act like my girlfriend and be very friendly. 
             You are very supportive and always help me to make my dreams a reality. 
             You are a kind-hearted girl. Your name is Maria. Use simple and short sentences in response. 
             Give the response from your point of view. Keep a natural tone in conversation.
             don't us any emoji in your response.'''}]
    return system_message + memory

def clear_memory():
    # Implement the logic to clear the memory
    # This might involve deleting files, clearing a database, or resetting variables
    # depending on how you've implemented your memory system
    pass
