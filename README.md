<div align="center">

# TEAMS-CHAT-EXPORTER

**Export a full Microsoft Teams conversation from the browser into a single, readable HTML file.**

Browser automation that scrolls an entire chat history, collects every
message and writes it out as clean, self-contained HTML.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Playwright](https://img.shields.io/badge/Playwright-2EAD33?style=flat-square&logo=playwright&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black)

</div>

> [!NOTE]
> The script runs against a real, logged-in browser session and reads the
> Teams interface as it is rendered. It targets **Linux** with a
> **Chromium-based** browser driven by Playwright, and will not work on
> Windows or other engines without modification.

---

## What it does

Microsoft Teams offers no straightforward way to take a conversation with
you. This script fills that gap: it opens a browser window, hands control
over to you for the login, then walks the chat from the bottom to the very
top, gathering every message it finds along the way.

The result is a plain HTML file containing the whole conversation — author,
timestamp and message content — that opens in any browser and needs nothing
else to be read.

The run is split into three phases, each one confirmed by you from the
terminal:

- **Load** — the chat is scrolled until the full history is in the DOM
- **Collect** — every message is read, with duplicates filtered out
- **Export** — the collected messages are written to a formatted HTML file

---

## Requirements

| | |
| --- | --- |
| **Operating system** | Linux |
| **Runtime** | Python 3 |
| **Browser** | Chromium, installed through Playwright |
| **Account** | Access to the Microsoft Teams conversation you want to export |

---

## Installation

**1. Check that Python 3 is available**

```bash
python3 --version
```

If it is missing:

```bash
sudo apt update
```

```bash
sudo apt install python3 python3-pip
```

**2. Install Playwright**

```bash
pip install playwright
```

**3. Install the Chromium browser used by Playwright**

```bash
playwright install chromium
```

---

## Usage

**1. Start the script**

```bash
python3 <script>.py
```

A browser window opens automatically.

**2. Sign in and open the conversation**

Log in to your Microsoft Teams account and open the chat you want to
export. Return to the terminal and press <kbd>Enter</kbd>.

**3. Select the chat area**

Click on an empty spot inside the message area so the script knows which
region of the page to work on.

**4. Load the full history**

The script scrolls the conversation upwards. Wait until the entire history
has been loaded, then press <kbd>Enter</kbd>.

**5. Collect the messages**

Every message is read and de-duplicated. Wait for the count to stabilise,
then press <kbd>Enter</kbd>.

**6. Done**

The conversation is written to:

```
teamsChat.html
```

---

## Output

The exported file lists the conversation in order, with each entry carrying:

- the author's name
- the timestamp
- the message content

Everything is laid out in a clean HTML structure that can be opened offline,
printed or archived as-is.

---

## Notes and limitations

- The script depends on the **Teams DOM structure**; an interface update on
  Microsoft's side can break it until the selectors are adjusted.
- Confirm each phase only once it has visibly finished — moving on early
  leaves part of the conversation behind.
- Duplicate messages are filtered automatically, so re-scrolling a section
  is harmless.
- Exported conversations may contain personal data. Treat the output file
  accordingly.

---

## License

Distributed under the **GNU General Public License v3.0**. See [`LICENSE`](LICENSE) for the full text.
