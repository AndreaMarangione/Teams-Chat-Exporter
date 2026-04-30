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

        for (let item of items) {
            let full_text = item.innerText.trim();
            if (!full_text) continue;

            let author_el = item.querySelector('[data-tid="message-author-name"]');
            let author = author_el ? author_el.innerText.trim() : "Sconosciuto";

            let time_el = item.querySelector("time");
            let time = time_el ? time_el.innerText.trim() : "";

            let body_el = item.querySelector('[data-tid="chat-pane-message"]');
            if (!body_el) continue;

            let text = body_el.innerText.trim();
            if (!text) continue;

            results.push({
                author: author,
                time: time,
                text: text
            });
        }

        return results;
    }
    """)


def scroll(page, container, direction="down", fast=True):
    delta = -3000 if direction == "up" else 3000 if fast else -1200 if direction == "up" else 1200
    page.evaluate("({el, delta}) => el.dispatchEvent(new WheelEvent('wheel',{deltaY: delta,bubbles: true,cancelable: true}))", {"el": container, "delta": delta})


def force_scroll(page, container, direction="down"):
    delta = 1500 if direction == "down" else -1500
    page.evaluate("({el, delta}) => el.scrollBy(0, delta)", {"el": container, "delta": delta})


def nudge(page, container):
    page.evaluate("(el) => el.scrollBy(0, 1)", container)


def scroll_up_manual(page, container):
    print("\nCaricamento dell'intera chat...\nPremere INVIO quando la chat è stata caricata tutta")

    while True:
        scroll(page, container, "up")
        time.sleep(0.15)
        import msvcrt
        if msvcrt.kbhit():
            input()
            break


def collect_messages(page, container):
    print("\nRaccolta messaggi in corso...\nPremere INVIO quando sono stati raccolti tutti i messaggi")

    seen, raw = set(), []

    while True:
        for b in get_messages(page):
            key = (b["author"], b["time"], b["text"])
            if key not in seen:
                seen.add(key)
                raw.append(b)

        scroll(page, container, "down")
        time.sleep(0.2)

        import msvcrt
        if msvcrt.kbhit():
            input()
            break

    return raw


def main():
    hacker_banner()
    with sync_playwright() as p:

        if platform.system() == "Windows":
            context = p.chromium.launch_persistent_context(
                user_data_dir=r"C:\temp\teams_profile",
                headless=False,
                channel="msedge",
                args=[
                    "--disable-blink-features=AutomationControlled",
                    "--disable-features=IsolateOrigins,site-per-process"
                ]
            )

            context.add_init_script("""
            Object.defineProperty(navigator, 'webdriver', {get: () => undefined});
            window.chrome = {runtime:{}};
            Object.defineProperty(navigator, 'plugins', {get: () => [1,2,3]});
            Object.defineProperty(navigator, 'languages', {get: () => ['it-IT','it']});
            """)

        else:
            context = p.chromium.launch_persistent_context(
                user_data_dir="teams_profile_linux",
                headless=False
            )

        page = context.new_page()
        page.goto("https://teams.microsoft.com/v2/")

        input("Effettua login e premi INVIO")

        container = pick_chat_container(page)
        scroll_up_manual(page, container)
        messages = collect_messages(page, container)

        html = "<html><body>"
        for m in messages:
            html += f"<div><b>{m['author']}</b> [{m['time']}]<br>{m['text']}</div><hr>"
        html += "</body></html>"

        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            f.write(html)

        print("Chat esportata ✅")
        context.close()


if __name__ == "__main__":
    main()
