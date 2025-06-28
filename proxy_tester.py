import requests
import os

def banner():
    os.system('clear')
    print("""
\033[1;34m
   ████████╗███████╗███████╗████████╗███████╗██████╗ 
   ╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝██╔════╝██╔══██╗
      ██║   █████╗  ███████╗   ██║   █████╗  ██████╔╝
      ██║   ██╔══╝  ╚════██║   ██║   ██╔══╝  ██╔═══╝ 
      ██║   ███████╗███████║   ██║   ███████╗██║     
      ╚═╝   ╚══════╝╚══════╝   ╚═╝   ╚══════╝╚═╝     
\033[1;37m
     🌐 Proxy Tester | Dev: Ali Hamza AF
     🛡️ AF Cyber Force | Termux Special
    ============================================
""")

def check_ip(proxy=None):
    try:
        if proxy:
            proxies = {"http": f"http://{proxy}", "https": f"http://{proxy}"}
            r = requests.get("https://api.myip.com", proxies=proxies, timeout=5)
        else:
            r = requests.get("https://api.myip.com", timeout=5)
        print("[✓] IP Info:", r.json())
    except Exception as e:
        print(f"[✘] Proxy Failed ({proxy}):", e)

if __name__ == "__main__":
    banner()
    print("[*] Checking original IP...")
    check_ip()
    print("\n[*] Checking via first proxy from file...")
    with open("proxies.txt", "r") as f:
        proxy = f.readline().strip()
        check_ip(proxy)
