# Telephone Encrption System

This Python program is a functional encryption and decryption tool based on the classic **multi-tap** mobile phone keypad. It converts standard alphabetical messages into numeric sequences and translates grouped numeric codes back into readable text.

## Features

* **Multi-Tap Encryption:** Maps letters to repeated button presses (e.g., `A` = `2`, `B` = `22`, `C` = `222`).
* **Intelligent Decryption:** Uses index tracking to group consecutive identical digits, ensuring accurate reconstruction of original letters (e.g., distinguishing `H` from `G`).
* **Interactive Menu:** A continuous command-line loop that allows users to seamlessly switch between encrypting, decrypting, and exiting.

## How to Use

Run the script directly from your terminal:

> `python app.py`

You will be prompted with an interactive menu.

**Menu Options**

* **1. Encrypt:** Type a text message (letters only) to receive the numeric multi-tap sequence.
* **2. Decrypt:** Enter a numeric code to reveal the hidden text message.
* **3. Exit:** Safely terminate the program.


