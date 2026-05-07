# HackingTool 🔧

> A fork of [Z4nzu/hackingtool](https://github.com/Z4nzu/hackingtool) — All in One Hacking Tool for Linux

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.6%2B-brightgreen.svg)](https://python.org)
[![Platform](https://img.shields.io/badge/platform-Linux-lightgrey.svg)]()

## ⚠️ Disclaimer

This tool is intended for **educational purposes only**. The developer is not responsible for any misuse or damage caused by this program. Use it only on systems you own or have explicit permission to test.

## 📋 Features

- Anonymous Surfing Tools
- Information Gathering Tools
- Wordlist Generator
- Wireless Attack Tools
- SQL Injection Tools
- Phishing Attack Tools
- Web Attack Tools
- Post Exploitation Tools
- Forensic Tools
- Payload Creation Tools
- Exploit Framework
- Reverse Engineering Tools
- DDOS Attack Tools
- Remote Administration Tools (RAT)
- XSS Attack Tools
- Steganography Tools
- SocialMedia Brute Force
- Android Hacking Tools
- IDN Homograph Attack Tools
- Email Verify Tools
- Hash Cracking Tools
- Wifi Deauthenticate
- SocialMedia Finder
- Payload Injector
- Web Crawling
- Mix Tools

## 🚀 Installation

### Requirements

- Python 3.6+
- Git
- Linux OS (Kali, Parrot, Ubuntu recommended)

### Quick Install

```bash
git clone https://github.com/YOUR_USERNAME/hackingtool.git
cd hackingtool
chmod +x install.sh
sudo bash install.sh
```

### Manual Install

```bash
git clone https://github.com/YOUR_USERNAME/hackingtool.git
cd hackingtool
pip3 install -r requirements.txt
sudo python3 hackingtool.py
```

### Docker

```bash
docker build -t hackingtool .
docker run -it hackingtool
```

## 🖥️ Usage

```bash
sudo python3 hackingtool.py
```

Navigate through the menu using the number keys to select your desired tool category.

> **Note:** I personally use this mostly for the Information Gathering and Hash Cracking sections while working through CTF challenges on HackTheBox/TryHackMe.

## 🗒️ Personal Notes

- Most tools require an active internet connection to clone/install on first run.
- On Ubuntu 22.04 I had to run `sudo apt install python3-dev libssl-dev` before `install.sh` would complete without errors.
- On Ubuntu 24.04 also needed `sudo apt install python3-venv` — the install script fails silently otherwise.
- On Ubuntu 24.04 with Python 3.12+, also run `sudo apt install python3-distutils` or the pip-based installs inside the script will fail with a `ModuleNotFoundError`.
- The Hash Cracking section works best when you point it at a local copy of `rockyou.txt` (usually at `/usr/share/wordlists/rockyou.txt` on Kali).

## 🤝 Contributing

Contributions are welcome! Please read our [Pull Request Template](.github/PULL_REQUEST_TEMPLATE.md) before submitting.

1. Fork the repository
2. Create your feature branch (`git checkout -b feat/new-tool`)
3. Commit your changes (`git commit -m 'feat: add new tool category'`)
4. Push to the branch (`git push origin feat/new-tool`)
5. Open a Pull Request

### Requesting a New Tool

Use the [Tool Request](.github/ISSUE_TEMPLATE/tool_request.md) issue template.

### Reporting Bugs

Use the [B