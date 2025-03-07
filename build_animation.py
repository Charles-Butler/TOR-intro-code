import time
import sys
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def scrolling_code(lines=20, delay=0.1):
    """Simulates scrolling terminal code."""
    for _ in range(lines):
        code_line = f"{random.choice(['int', 'float', 'def', 'return', 'if', 'else', 'import', 'print'])} {random.choice(['variable', 'function', 'value', 'data', 'output'])} = {random.randint(1, 100)}"
        print(code_line)
        time.sleep(delay)
        sys.stdout.flush()

def flashing_build_complete(build_message="BUILD COMPLETE", review_message="NOW REVIEWING: DARK SOULS", flashes=5, delay=0.5):
    """Flashes the BUILD COMPLETE and NOW REVIEWING messages."""
    for _ in range(flashes):
        print(f"\033[1;32m{build_message}\033[0m")  # Green text
        sys.stdout.flush()
        time.sleep(delay)
        clear_screen()
        time.sleep(delay)
    print(f"\033[1;32m{build_message}\033[0m")  # Final persistent build message
    print(f"\033[1;34m{review_message}\033[0m")  # Blue text for review message

def main(build_message="BUILD COMPLETE", review_message="NOW REVIEWING: DARK SOULS"):
    clear_screen()
    scrolling_code()
    print("\nCompiling...\n")
    time.sleep(2)
    flashing_build_complete(build_message, review_message)

if __name__ == "__main__":
    main()
