from playwright.sync_api import sync_playwright
import time
import platform

OUTPUT_FILE = "teamsChat.html"


def hacker_banner():
    green = "\033[92m"
    reset = "\033[0m"

    banner = r"""
████████╗███████╗ █████╗ ███╗   ███╗███████╗
╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██╔════╝
   ██║   █████╗  ███████║██╔████╔██║███████╗
   ██║   ██╔══╝  ██╔══██║██║╚██╔╝██║╚════██║
   ██║   ███████╗██║  ██║██║ ╚═╝ ██║███████║
   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝
"""

    print(green)
    for line in banner.split("\n"):
        print(line)
        time.sleep(0.015)

    print("=" * 50)
    print("      ⚡ POWERED BY ANDREA MARANGIONE ⚡")
    print("=" * 50)
    print(reset)


# --- TUTTO IL TUO CODICE RESTA IDENTICO FINO A main() ---


def main():
    hacker_banner()
    with sync_playwright() as p:

        system = platform.system()

        if system == "Windows":
            print("Uso Edge su Windows")

            context = p.chromium.launch_persistent_context(
                user_data_dir=r"C:\temp\teams_profile",   # ✅ PATH FIX
                headless=False,
                channel="msedge",
                args=[
                    "--disable-blink-features=AutomationControlled",
                    "--disable-features=IsolateOrigins,site-per-process"
                ]
            )

            # ✅ STEALTH PATCH (ANTI DETECTION)
            context.add_init_script("""
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
            });

            window.chrome = {
                runtime: {}
            };

            Object.defineProperty(navigator, 'plugins', {
                get: () => [1, 2, 3]
            });

            Object.defineProperty(navigator, 'languages', {
                get: () => ['it-IT', 'it']
            });
            """)

        else:
            print("Uso Chromium su Linux")
            context = p.chromium.launch_persistent_context(
                user_data_dir="teams_profile_linux",
                headless=False
            )

        page = context.new_page()

        page.goto("https://teams.microsoft.com/v2/")

        input("Salve sig. Taiana!\nEffettui il login, apra la chat da esportare e prema INVIO qui nel terminale")

        container = pick_chat_container(page)

        if container is None:
            print("Container non trovato ❌")
            return

        scroll_up_manual(page, container)

        messages = collect_messages(page, container)

        html = """
        <html>
        <head>
        <meta charset="UTF-8">
        <style>
        body { font-family: Arial; background:#f4f6f8; padding:20px; }
        .msg { background:white; padding:10px; margin-bottom:10px; border-radius:8px; }
        .time { font-size:12px; color:gray; margin-bottom:5px; }
        </style>
        </head>
        <body>
        <h2>Teams Export</h2>
        """

        for m in messages:
            html += f"""
            <div class="msg">
                <div class="time">{m['author']} — {m['time']}</div>
                <div>{m['text']}</div>
            </div>
            """

        html += "</body></html>"

        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            f.write(html)

        print("\n")
        print("Chat esportata con successo ✅")

        context.close()


if __name__ == "__main__":
    main()
