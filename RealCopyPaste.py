import time
import pyperclip
from pynput.keyboard import Key, Controller

# Main Defines
keyboard = Controller()

def print_clipboard_text_with_delay():   # Get text from clipboard
    text = pyperclip.paste()
    print("Följande text pasteas i dokumentet om 5 sekunder")
    print(text)
    time.sleep(5)  # Wait for 5 seconds   # Print text with delay
    for char in text:
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(0.05)  # Adjust delay here if needed


if __name__ == "__main__":
    print_clipboard_text_with_delay()
