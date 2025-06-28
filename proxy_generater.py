import requests
from bs4 import BeautifulSoup
import os

def banner():
    os.system('clear')
    print("""
\033[1;32m
   █████╗ ███████╗     ██████╗ ██╗   ██╗██████╗ 
  ██╔══██╗██╔════╝     ██╔══██╗██║   ██║██╔══██╗
  ███████║███████╗     ██████╔╝██║   ██║██████╔╝
  ██╔══██║╚════██║     ██╔═══╝ ██║   ██║██╔═══╝ 
  ██║  ██║███████║     ██║     ╚██████╔╝██║     
  ╚═╝  ╚═╝╚══════╝     ╚═╝      ╚═════╝ ╚═╝     
\033[1;37m
     🔥 AF-BypassProxy - Proxy Scraper & Tester 🔥
     💻 Developer: Ali Hamza AF
     🛡️ Powered By: AF Cyber Force ❤️
    =============================================
""")

def fetch_proxies():
    url = "https://free-proxy-list.net/"
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    proxies = []
    for row in soup.select("table#proxylisttable tbody tr"):
        cols = row.find_all("td")
        if cols[6].text == "yes":  # HTTPS support
            proxies.append(f"{cols[0].text}:{cols[1].text}")
    return proxies

if __name__ == "__main__":
    banner()
    print("[✓] Scraping fresh proxies...")
    proxies = fetch_proxies()
    with open("proxies.txt", "w") as f:
        for p in proxies:
            f.write(p + "\n")
    print(f"[✓] Saved {len(proxies)} proxies to proxies.txt\n")
