import time
import sys
import random
import os
import colorama
from colorama import Fore, Style

colorama.init()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def logging_info(message):
    separator = "=" * 40
    boxed_message = f"* {message} *"
    padding = "*" * len(boxed_message)
    print(f"{Fore.YELLOW}{separator}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{padding}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{boxed_message}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{padding}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}{separator}{Style.RESET_ALL}")
    sys.stdout.flush()
    time.sleep(random.uniform(0.5, 1.5))  # Random delay between 0.5s - 1.5s

def simulate_gradle_build():
    clear_screen()
    print(f"{Fore.GREEN}Gradle Build Starting...{Style.RESET_ALL}\n")
    
    build_steps = [
        "Starting a Gradle Daemon...",
        "===============================",
        "Configuring build...",
        "===============================",
        "Resolving dependencies...",
        "===============================",
        "Compiling source code...",
        "===============================",
        "Running tests...",
        "===============================",
        "Assembling outputs...",
        "===============================",
        "Generating build reports...",
        "===============================",
        "Finalizing build...",
    ]
    
    for step in build_steps:
        logging_info(step)
    
    print(f"\n{Fore.GREEN}{Style.BRIGHT}BUILD SUCCESSFUL{Style.RESET_ALL}\n")
    print(f"{Fore.BLUE}NOW REVIEWING: DARK SOULS{Style.RESET_ALL}\n")

def main():
    simulate_gradle_build()
    
if __name__ == "__main__":
    main()
