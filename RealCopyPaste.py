import time
import random
import pyperclip
from pynput.keyboard import Key, Controller

# Main Defines
keyboard = Controller()
base_delay = 0.1 

def get_delay(char):
    if char.isalpha():
        return random.uniform(0.5 * base_delay, 1.5 * base_delay)
    elif char.isdigit():
        return random.uniform(1.0 * base_delay, 2.0 * base_delay)
    else:
        return random.uniform(1.5 * base_delay, 2.5 * base_delay)

def print_clipboard_text_with_delay():
    text = pyperclip.paste()
    print("Följande text pasteas i dokumentet om 5 sekunder")
    print(text)
    time.sleep(5)
    
    for char in text:
        delay = get_delay(char)
        if char in '.!?':
            pause = random.uniform(5.0 * base_delay, 10.0 * base_delay)
            time.sleep(pause)
        
        keyboard.press(char)
        time.sleep(delay)
        keyboard.release(char)
        time.sleep(random.uniform(0.1 * base_delay, 0.5 * base_delay))

if __name__ == "__main__":
    print_clipboard_text_with_delay()
