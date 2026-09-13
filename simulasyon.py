import sys
import time

# ANSI Renk Kodları
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
RESET = "\033[0m"

# ASCII Banner (Yeşil Renk)
print(
    f"{GREEN} ___ ____    ____  ____  _   _ _____ _____ ____  \n|_ _/ ___|  | __ )|  _ \\| | | |_   _| ____|  _ \\ \n | || |      |  _ \\| |_) | | | | | |  _| | |_) |\n | || |___   | |_) |  _ <| |_| | | | |___|  _ < \n|___\\____|  |____/|_| \\_\\\\___/  |_| |_____|_| \\_\\{RESET}"
)
print(f"{MAGENTA}    * Terminal Simulation Tool *{RESET}\n")

# Kullanıcıdan hedef alma
target = input(f"{CYAN}Enter target username: {RESET}")
print(f"{GREEN}[+] Initializing brute-force on @{target}...{RESET}\n")

# Sahte şifre deneme simülasyonu
passwords = [
    "master7799*",
    "master7877%",
    "master8899!",
    "master5999!",
    "mustang1571",
]

for i, pwd in enumerate(passwords, 1):
  print(
      f"{GREEN}[*]{RESET} Trying password ({i}/10000): {pwd}... "
      f"{RED}Failed{RESET}"
  )
  time.sleep(0.4)  # Efekt için yarım saniye bekletme

