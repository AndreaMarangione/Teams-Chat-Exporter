<pre style="color:#00ff00; font-family: monospace;">

████████╗███████╗ █████╗ ███╗   ███╗███████╗
╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██╔════╝
   ██║   █████╗  ███████║██╔████╔██║███████╗
   ██║   ██╔══╝  ██╔══██║██║╚██╔╝██║╚════██║
   ██║   ███████╗██║  ██║██║ ╚═╝ ██║███████║
   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝

 ██████╗██╗  ██╗ █████╗ ████████╗
██╔════╝██║  ██║██╔══██╗╚══██╔══╝
██║     ███████║███████║   ██║   
██║     ██╔══██║██╔══██║   ██║   
╚██████╗██║  ██║██║  ██║   ██║   
 ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   

███████╗██╗  ██╗██████╗  ██████╗ ██████╗ ████████╗███████╗██████╗ 
██╔════╝╚██╗██╔╝██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝██╔════╝██╔══██╗
█████╗   ╚███╔╝ ██████╔╝██║   ██║██████╔╝   ██║   █████╗  ██████╔╝
██╔══╝   ██╔██╗ ██╔═══╝ ██║   ██║██╔══██╗   ██║   ██╔══╝  ██╔══██╗
███████╗██╔╝ ██╗██║     ╚██████╔╝██║  ██║   ██║   ███████╗██║  ██║
╚══════╝╚═╝  ╚═╝╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝

==================================================
      POWERED BY ANDREA MARANGIONE
==================================================

</pre>

## <span style="color:#00ff00;">OVERVIEW</span>

This Python script allows you to export a full Microsoft Teams chat directly from your browser into a clean HTML file.

It uses browser automation to:
- Scroll through the entire chat history
- Collect all messages
- Export them into a readable HTML file


## <span style="color:#00ff00;">REQUIREMENTS</span>

This script works ONLY under the following conditions:

- Linux operating system
- Chromium-based browser (via Playwright)

It will not work properly on Windows or non-Chromium browsers without modifications.


## <span style="color:#00ff00;">INSTALLATION</span>

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

### 2. Install dependencies

Install Playwright:

```bash
pip install playwright
```

Install Chromium:

```bash
playwright install chromium
```


## <span style="color:#00ff00;">USAGE GUIDE</span>

### Step 1 - Run the script

```bash
python3 your_script_name.py
```

### Step 2 - Login to Microsoft Teams

A browser window will open automatically.

- Log in to your account
- Open the chat you want to export

Then return to the terminal and press ENTER


### Step 3 - Select the chat area

Click on the blank area of the chat

Click anywhere inside the chat message area


### Step 4 - Load the full chat

Loading the full chat...

Wait until the entire chat history is loaded

Press ENTER


### Step 5 - Collect messages

Collecting messages...

Wait until the process stabilizes

Press ENTER


### Step 6 - Export completed

Chat exported successfully

Output file:

```
teamsChat.html
```


## <span style="color:#00ff00;">OUTPUT</span>

The exported file contains:
- Author name
- Timestamp
- Message content

All formatted in a clean HTML layout.


## <span style="color:#00ff00;">NOTES</span>

- The script depends on Microsoft Teams DOM structure
- UI updates may break compatibility
- Ensure the chat is fully loaded before confirming
- Duplicate messages are automatically filtered


## <span style="color:#00ff00;">AUTHOR</span>

Andrea Marangione


## <span style="color:#00ff00;">FUTURE IMPROVEMENTS</span>

- Windows support
- Firefox support
- Automatic full scroll detection
- Export to CSV / JSON
