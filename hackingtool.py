#!/usr/bin/env python3
"""HackingTool - All in One Hacking Tool for Hackers.

Main entry point for the hackingtool application.
Provides a menu-driven interface to various security and pentesting tools.
"""

import os
import sys
import subprocess

# Ensure the script is run with Python 3
if sys.version_info[0] < 3:
    print("[!] HackingTool requires Python 3. Please use python3.")
    sys.exit(1)


BANNER = r"""
 ██╗  ██╗ █████╗  ██████╗██╗  ██╗██╗███╗   ██╗ ██████╗
 ██║  ██║██╔══██╗██╔════╝██║ ██╔╝██║████╗  ██║██╔════╝
 ███████║███████║██║     █████╔╝ ██║██╔██╗ ██║██║  ███╗
 ██╔══██║██╔══██║██║     ██╔═██╗ ██║██║╚██╗██║██║   ██║
 ██║  ██║██║  ██║╚██████╗██║  ██╗██║██║ ╚████║╚██████╔╝
 ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝
          ████████╗ ██████╗  ██████╗ ██╗
          ╚══██╔══╝██╔═══██╗██╔═══██╗██║
             ██║   ██║   ██║██║   ██║██║
             ██║   ██║   ██║██║   ██║██║
             ██║   ╚██████╔╝╚██████╔╝███████╗
             ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
"""

CATEGORIES = [
    "[01] Information Gathering",
    "[02] Wordlist Generator",
    "[03] Wireless Attack Tools",
    "[04] SQL Injection Tools",
    "[05] Phishing Attack Tools",
    "[06] Web Attack Tools",
    "[07] Post Exploitation",
    "[08] Forensic Tools",
    "[09] Payload Creator",
    "[10] Exploit Framework",
    "[11] Reverse Engineering",
    "[12] DDOS Attack Tools",
    "[13] Remote Administration Tools (RAT)",
    "[14] XSS Attack Tools",
    "[15] Steganography Tools",
    "[16] SocialMedia Brute Force",
    "[17] Android Hacking Tools",
    "[18] IDN Homograph Attack",
    "[19] Email Verify Tools",
    "[20] Hash Cracking Tools",
    "[21] Wifi Deauthenticate",
    "[22] SocialMedia Finder",
    "[23] Payload Injector",
    "[24] Web Crawling",
    "[25] Mix Tools",
    "[99] Exit",
]


def clear_screen():
    """Clear the terminal screen."""
    os.system("clear" if os.name == "posix" else "cls")


def print_banner():
    """Print the application banner."""
    print("\033[1;31m" + BANNER + "\033[0m")
    print("\033[1;34m" + " " * 10 + "Fork of Z4nzu/hackingtool" + "\033[0m")
    print("\033[1;32m" + " " * 10 + "All in One Hacking Tool" + "\033[0m")
    print()


def print_menu():
    """Display the main category menu."""
    print("\033[1;33m" + "=" * 50 + "\033[0m")
    print("\033[1;33m" + "  SELECT A CATEGORY" + "\033[0m")
    print("\033[1;33m" + "=" * 50 + "\033[0m")
    for category in CATEGORIES:
        print("\033[1;36m  " + category + "\033[0m")
    print("\033[1;33m" + "=" * 50 + "\033[0m")


def check_root():
    """Check if the script is run with root privileges."""
    if os.geteuid() != 0:
        print("\033[1;31m[!] Some tools require root privileges.\033[0m")
        print("\033[1;31m[!] Consider running with sudo.\033[0m")
        print()


def get_user_choice():
    """Prompt the user for a menu selection and return it."""
    try:
        choice = input("\033[1;32m[>>] Enter your choice: \033[0m").strip()
        return choice
    except (KeyboardInterrupt, EOFError):
        print("\n\033[1;31m[!] Interrupted. Exiting...\033[0m")
        sys.exit(0)


def handle_choice(choice):
    """Handle the user's menu selection.

    Args:
        choice (str): The user's input from the menu.

    Returns:
        bool: False if the user chose to exit, True otherwise.
    """
    if choice == "99":
        print("\033[1;32m[*] Thank you for using HackingTool. Goodbye!\033[0m")
        return False

    # Placeholder: individual category modules will be imported and called here
    # as they are added to the project.
    print(f"\033[1;33m[*] Category '{choice}' is not yet implemented.\033[0m")
    input("\033[1;36m[*] Press Enter to return to the main menu...\033[0m")
    return True


def main():
    """Main loop for the HackingTool application."""
    check_root()
    running = True
    while running:
        clear_screen()
        print_banner()
        print_menu()
        choice = get_user_choice()
        running = handle_choice(choice)


if __name__ == "__main__":
    main()
