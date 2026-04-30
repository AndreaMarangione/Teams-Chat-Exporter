# 📄 README.md

## 🧠 Overview

This Python script allows you to **export a full Microsoft Teams chat** directly from your browser into a clean HTML file.

It uses browser automation to:
- Scroll through the entire chat history
- Collect all messages
- Export them into a readable `.html` file

---

## ⚠️ Requirements

This script currently works **ONLY under the following conditions**:

- 🐧 **Linux operating system**
- 🌐 **Chromium-based browser** (used via Playwright)

It will **NOT work properly on Windows or non-Chromium browsers** without modifications.

---

## 📦 Installation

### 1. Install Python

Make sure Python 3 is installed:

```bash
python3 --version
```

If not installed:

```bash
sudo apt update
sudo apt install python3 python3-pip
```

---

### 2. Install dependencies

Install Playwright:

```bash
pip install playwright
```

Then install Chromium for Playwright:

```bash
playwright install chromium
```

---

## 🚀 Usage Guide

### Step 1 — Run the script

```bash
python3 your_script_name.py
```

---

### Step 2 — Login to Microsoft Teams

A browser window will open automatically.

- Log in to your account on **Microsoft Teams**
- Open the chat you want to export

👉 Then go back to the terminal and press **ENTER**

---

### Step 3 — Select the chat area

The script will ask you to:

> Click on the blank area of the chat

👉 Click anywhere inside the chat message area (white space)

📸 *(Insert screenshot here — selecting chat area)*

---

### Step 4 — Load the full chat

The script will start scrolling automatically:

> Loading the full chat...

👉 Wait until the entire chat history is loaded

Then press **ENTER**

📸 *(Insert screenshot here — chat fully loaded)*

---

### Step 5 — Collect messages

The script will now collect all messages:

> Collecting messages...

👉 Wait until the process stabilizes

Then press **ENTER**

📸 *(Insert screenshot here — message collection)*

---

### Step 6 — Export completed

Once finished, you will see:

```
Chat exported successfully ✅
```

The output file will be:

```
teamsChat.html
```

---

## 📁 Output

The exported file contains:
- Author name
- Timestamp
- Message content

All formatted in a clean, readable HTML layout.

---

## ⚙️ Notes

- The script relies on **DOM structure of Microsoft Teams**, so it may break if Teams updates its UI.
- Make sure the chat is **fully loaded before confirming**, otherwise some messages may be missing.
- The script avoids duplicate messages automatically.

---

## 👨‍💻 Author

Powered by **Andrea Marangione**

---

## 🧩 Future Improvements

- Windows support
- Firefox support
- Automatic full scroll detection (no manual ENTER)
- Export to CSV / JSON

---

## 📸 Screenshots

*(Add your screenshots here to visually guide users step-by-step)*
