import time
import warnings
from colorama import init, Fore, Style
from speech_utils2 import listen_for_command, speak
from ai_utils import initialize_conversation, generate_response
from memory_utils import update_memory, clear_memory
from pynput import keyboard
import threading

# Initialize colorama
init(autoreset=True)

# Filter out specific warnings
warnings.filterwarnings("ignore", category=FutureWarning, module="whisper")
warnings.filterwarnings("ignore", category=UserWarning, message="FP16 is not supported on CPU; using FP32 instead")

def process_user_input(messages):
    user_input = listen_for_command()
    if user_input is not None:
        print(f"{Fore.CYAN}You said: {user_input}{Style.RESET_ALL}")
        if user_input.lower() == "clear memory":
            clear_memory()
            print(f"{Fore.YELLOW}Memory cleared.{Style.RESET_ALL}")
            return False
        messages.append({'role': 'user', 'content': user_input})
    return user_input is not None

def process_ai_response(messages):
    ai_response = generate_response(messages)
    print(f"{Fore.GREEN}Maria said: {ai_response}{Style.RESET_ALL}")
    messages.append({'role': 'assistant', 'content': ai_response})
    speak(ai_response)  # This should now be a synchronous call

def on_activate():
    print(f"\n{Fore.YELLOW}Clearing memory...{Style.RESET_ALL}")
    clear_memory()
    print(f"{Fore.YELLOW}Memory cleared. Continuing with a fresh conversation.{Style.RESET_ALL}")

def for_canonical(f):
    return lambda k: f(listener.canonical(k))

hotkey = keyboard.HotKey(
    keyboard.HotKey.parse('<ctrl>+q'),
    on_activate)
listener = keyboard.Listener(
    on_press=for_canonical(hotkey.press),
    on_release=for_canonical(hotkey.release))

def main():
    messages = initialize_conversation()
    
    print(f"{Fore.YELLOW}Press Ctrl+Q to clear memory or Ctrl+C to exit.{Style.RESET_ALL}")
    
    listener.start()
    
    while True:
        try:
            if process_user_input(messages):
                process_ai_response(messages)
                update_memory(messages[-2:])  # Update memory after each interaction
            time.sleep(1)
        except KeyboardInterrupt:
            print(f"\n{Fore.YELLOW}Exiting the program...{Style.RESET_ALL}")
            break

    listener.stop()

if __name__ == "__main__":
    main()
