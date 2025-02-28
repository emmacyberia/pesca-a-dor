from time import sleep
from core.actions import log, pause_event, login, logout, apply_elixir_mode
from core.accounts import pxg_accounts
from core.config import *
from itertools import cycle

def main_money_maker():
    """Main function."""
    log("-------------------")
    log(f"MONEY-MAKER {VERSION}")
    log("-------------------")
    log(f"{START_KEY}   → Start")
    log(f"{PAUSE_KEY} → Pause")
    log(f"{STOP_KEY}       → Exit")
    log("-------------------")

    use_thread_kill_shiny = True
    accounts = pxg_accounts
    infinite_accounts = cycle(accounts)

    for account in infinite_accounts:
        pause_event.wait() 
        login(account["email"], account["password"], account["imagem"], account["char"])
        apply_elixir_mode(use_thread_kill_shiny, account)    
        logout()
        print("esperando 15s antes de logar na outra conta")
        sleep(15)  # pra rotação ficar permanente, precisa esperar pelo menos 10s entre todas as contas