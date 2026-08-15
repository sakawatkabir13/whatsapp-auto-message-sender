# WhatsApp Auto Message Sender

> A lightweight Python CLI and library for scheduling and sending WhatsApp messages — to contacts or groups — via WhatsApp Web using [PyWhatKit](https://pypi.org/project/pywhatkit/).

<p align="left">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.6%2B-blue?logo=python&logoColor=white" />
  <img alt="License" src="https://img.shields.io/badge/License-MIT-green.svg" />
  <img alt="pywhatkit" src="https://img.shields.io/badge/Built%20with-pywhatkit-orange" />
  <img alt="Platform" src="https://img.shields.io/badge/Platform-Cross--Platform-lightgrey" />
  <img alt="Status" src="https://img.shields.io/badge/Status-Active-success" />
</p>

---

## ✨ Features

- 📅 **Scheduled messages** — pick an exact hour and minute.
- ⚡ **Instant messages** — send right away without scheduling.
- 👥 **Group support** — message any WhatsApp group using its invite ID.
- 🖥️ **Dual mode** — use it as a CLI tool or import it as a Python library.
- 🧩 **Modular design** — clean, reusable functions with clear docstrings.

## 📋 Prerequisites

- **Python** 3.6 or higher
- An active **WhatsApp** account
- A **web browser** (default browser will be opened automatically)
- A stable **Internet connection**
- **WhatsApp Web** linked to your phone (scan the QR code on first run)

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/sakawatkabir13/whatsapp-auto-message-sender.git
   cd whatsapp-auto-message-sender
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Usage

### As a CLI

Run `whatsapp_sender.py` with one of three modes: `individual`, `instant`, or `group`.

#### 1. Scheduled message to an individual

```bash
python whatsapp_sender.py individual +911234567890 "Hello, this is an automated message"
```

Add an optional hour and minute (24-hour format) to send at a specific time:

```bash
python whatsapp_sender.py individual +911234567890 "Good morning!" 9 0
```

> 📌 Phone numbers **must** include the country code (e.g. `+91` for India). The `+` is optional; it will be added automatically if missing.

#### 2. Instant message

```bash
python whatsapp_sender.py instant +911234567890 "Hello, urgent message!"
```

#### 3. Message to a group

```bash
python whatsapp_sender.py group "AB123CDEfghi456" "Hello group!"
```

```bash
python whatsapp_sender.py group "AB123CDEfghi456" "Scheduled group hello" 15 45
```

> 📌 The group ID is taken from the group's invite link — for example, in `https://chat.whatsapp.com/AB123CDEfghi456` the ID is `AB123CDEfghi456`.

### As a Python library

```python
import whatsapp_sender

# Send a scheduled message
whatsapp_sender.send_whatsapp_message(
    phone_number="+911234567890",
    message="Hello! This is a scheduled message.",
    hour=14,
    minute=30,
)

# Send an instant message
whatsapp_sender.send_whatsapp_message_instantly(
    phone_number="+911234567890",
    message="Hello! This is instant.",
)

# Send to a group
whatsapp_sender.send_whatsapp_to_group(
    group_id="AB123CDEfghi456",
    message="Hello everyone!",
    hour=18,
    minute=0,
)
```

See [`example.py`](./example.py) for a complete working example.

## ⚙️ How It Works

1. The script opens your default browser and navigates to **WhatsApp Web**.
2. On first run, scan the **QR code** with your phone to log in.
3. At the scheduled time, **PyWhatKit** automatically focuses the chat and clicks **Send**.
4. Optionally closes the browser tab once the message is delivered.

## ⚠️ Important Notes

- 🖥️ Keep your computer **awake and online** until the message is sent.
- 🔗 WhatsApp Web **must remain linked** to your account.
- 🖱️ **Avoid touching the mouse or keyboard** during the sending process — PyWhatKit automates clicks.
- 🚫 **Do not** use this tool for spam, unsolicited messaging, or any malicious activity. Respect WhatsApp's [Terms of Service](https://www.whatsapp.com/legal/terms-of-service).
- ⏱️ Scheduled messages use your system clock — ensure it is set correctly.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📜 License

Distributed under the **MIT License**. See [`LICENSE`](./LICENSE) for more information.

## 🙏 Acknowledgements

- [PyWhatKit](https://github.com/Ankit404butfound/PyWhatKit) — the underlying automation library.
- [pyautogui](https://pypi.org/project/PyAutoGUI/) — for simulating mouse and keyboard input.

---

<p align="center">Made with ❤️ by <a href="https://github.com/sakawatkabir13">sakawatkabir13</a></p>
