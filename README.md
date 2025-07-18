# WhatsApp Auto Message Sender

A Python tool that automates sending WhatsApp messages using the PyWhatKit module.

## Features

- Send scheduled messages to individual contacts
- Send instant messages without scheduling
- Send messages to WhatsApp groups
- Command-line interface for easy use

## Prerequisites

- Python 3.6 or higher
- WhatsApp account
- Web browser
- Internet connection
- WhatsApp Web must be linked to your account

## Installation

1. Clone this repository or download the files
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## How to Use

### Send a Scheduled Message to an Individual

```bash
python whatsapp_sender.py individual 9123456789 "Hello, this is an automated message"
```

Note: Phone number should include country code with a '+' sign (e.g., '+911234567890' for +91 1234 567890)

### Send an Instant Message

```bash
python whatsapp_sender.py instant 9123456789 "Hello, urgent message!"
```

### Send a Message to a Group

```bash
python whatsapp_sender.py group "AB123CDEfghi456" "Hello group, this is an automated message"
```

Note: The group ID can be found in the group's invite link.

## How It Works

The script uses the PyWhatKit library to automate WhatsApp Web. When you run the command:

1. It opens your default web browser
2. Navigates to WhatsApp Web
3. If you're not already logged in, you'll need to scan the QR code
4. At the scheduled time, it will send the message to the specified recipient

## Important Notes

- Your computer must remain on and connected to the internet until the scheduled time
- WhatsApp Web must be properly linked to your WhatsApp account
- The script uses automation to interact with the browser, so avoid using the mouse/keyboard during the sending process
- Do not use this for spam or any malicious activities

## License

This project is for educational purposes only.
