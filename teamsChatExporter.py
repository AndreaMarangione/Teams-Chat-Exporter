from playwright.sync_api import sync_playwright
import time

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
"""

    print(green)

    for line in banner.split("\n"):
        print(line)
        time.sleep(0.015)

    print("=" * 50)
    print("      ⚡ POWERED BY ANDREA MARANGIONE ⚡")
    print("=" * 50)

    print(reset)


def pick_chat_container(page):
    print("\n")
    print("Cliccare nella parte bianca della chat")

    return page.evaluate_handle("""
    () => new Promise(resolve => {

        function findScrollable(el) {
            while (el) {
                if (el.scrollHeight > el.clientHeight + 100) {
                    return el;
                }
                el = el.parentElement;
            }
            return null;
        }

        function handler(e) {
            document.removeEventListener('click', handler, true);

            let container = findScrollable(e.target);

            if (!container) {
                alert("❌ Nessun container trovato");
                resolve(null);
                return;
            }

            container.style.outline = "3px solid red";

            resolve(container);
        }

        document.addEventListener('click', handler, true);
    })
    """)


def get_messages(page):
    return page.evaluate("""
    () => {

        let items = document.querySelectorAll('[data-tid="chat-pane-item"]');

        let results = [];

        let current_date = "";

        for (let item of items) {

            let full_text = item.innerText.trim();
            if (!full_text) continue;

            let lower = full_text.toLowerCase();

            if (
                lower.startsWith("march ") ||
                lower.startsWith("april ") ||
                lower.startsWith("may ") ||
                lower.startsWith("june ") ||
                lower.startsWith("july ") ||
                lower.startsWith("august ") ||
                lower.startsWith("september ") ||
                lower.startsWith("october ") ||
                lower.startsWith("november ") ||
                lower.startsWith("december ") ||
                lower.startsWith("yesterday") ||
                lower.startsWith("monday") ||
                lower.startsWith("tuesday") ||
                lower.startsWith("wednesday") ||
                lower.startsWith("thursday") ||
                lower.startsWith("friday") ||
                lower.startsWith("saturday") ||
                lower.startsWith("sunday") ||
                /^[0-9]{1,2}\\/[0-9]{1,2}/.test(lower)
            ) {
                current_date = full_text;
                continue;
            }

            let author_el = item.querySelector('[data-tid="message-author-name"]');
            let author = author_el ? author_el.innerText.trim() : "Sconosciuto";

            let time_el = item.querySelector("time");
            let time = time_el ? time_el.innerText.trim() : "";

            let body_el = item.querySelector('[data-tid="chat-pane-message"]');
            if (!body_el) continue;

            let clone = body_el.cloneNode(true);

            let quotes = clone.querySelectorAll('[data-tid="quoted-reply-card"]');
            for (let q of quotes) q.remove();

            let text = clone.innerText.trim();
            if (!text) continue;

            text = text.replace(/\\d+\\s+\\w+\\s+reaction\\.?/gi, "").trim();

            let datetime = time;

            results.push({
                author: author,
                time: datetime,
                text: text
            });
        }

        return results;
    }
    """)


def scroll(page, container, direction="down", fast=True):
    if fast:
        delta = -3000 if direction == "up" else 3000
    else:
        delta = -1200 if direction == "up" else 1200

    page.evaluate("""
    ({el, delta}) => {
        el.dispatchEvent(new WheelEvent('wheel', {
            deltaY: delta,
            bubbles: true,
            cancelable: true
        }));
    }
    """, {"el": container, "delta": delta})


def force_scroll(page, container, direction="down"):
    delta = 1500 if direction == "down" else -1500

    page.evaluate("""
    ({el, delta}) => {
        el.scrollBy(0, delta);
    }
    """, {"el": container, "delta": delta})


def nudge(page, container):
    page.evaluate("(el) => el.scrollBy(0, 1)", container)


def scroll_up_manual(page, container):
    print("\n")
    print("Caricamento dell'intera chat...")
    print("\n")
    print("Premere INVIO quando la chat è stata caricata tutta")

    i = 0
    stable_rounds = 0
    last_count = 0

    while True:

        fast_mode = stable_rounds < 2

        scroll(page, container, "up", fast_mode)
        scroll(page, container, "up", fast_mode)

        time.sleep(0.1 if fast_mode else 0.2)

        i += 1

        if i % 5 == 0:
            nudge(page, container)

        if i % 15 == 0:
            force_scroll(page, container, "up")

        blocks = get_messages(page)
        if len(blocks) == last_count:
            stable_rounds += 1
        else:
            stable_rounds = 0

        last_count = len(blocks)

        if i % 5 == 0:
            import select, sys
            if select.select([sys.stdin], [], [], 0.01)[0]:
                input()
                print("Caricamento completato ✅")
                break


def collect_messages(page, container):
    print("\n")
    print("Raccolta messaggi in corso...")
    print("\n")
    print("Premere INVIO quando sono stati raccolti tutti i messaggi")

    seen = set()
    raw = []

    i = 0
    stable_rounds = 0
    last_len = 0

    while True:

        blocks = get_messages(page)

        for b in blocks:

            key = (b["author"], b["time"], b["text"])

            if key not in seen:
                seen.add(key)
                raw.append(b)

        fast_mode = stable_rounds < 2

        scroll(page, container, "down", fast_mode)
        scroll(page, container, "down", fast_mode)

        time.sleep(0.1 if fast_mode else 0.25)

        if i % 5 == 0:
            nudge(page, container)

        if i % 15 == 0:
            force_scroll(page, container, "down")

        if len(raw) == last_len:
            stable_rounds += 1
        else:
            stable_rounds = 0

        last_len = len(raw)
        i += 1

        if stable_rounds >= 5:
            import select, sys
            if select.select([sys.stdin], [], [], 0.01)[0]:
                input()
                print("Raccolta messaggi terminata ✅")
                break

    return raw


def main():
    hacker_banner()
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://teams.microsoft.com")

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

        browser.close()


if __name__ == "__main__":
    main()
