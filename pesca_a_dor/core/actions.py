from pyautogui import center, moveTo, click, locateOnScreen, dragTo, mouseDown, mouseUp, write, doubleClick
from time import localtime, strftime, time, sleep
from datetime import date
from keyboard import add_hotkey, press, release, press_and_release
from threading import Thread, Event
from core.config import *
from core.accounts import pxg_accounts
from json import load
import argparse
import ctypes
import os

def start_loop():
    pause_event.set()
    log("STARTED FISHING")

def pause_loop():
    pause_event.clear()
    log("PAUSED!")
    log("PRESS PAGE UP TO RESUME")

def stop_loop():
    log("EXITING...")
    stop_event.set()
    pause_event.set()
    os._exit(0)

def get_current_day():
    today_var = date.today()
    return today_var.strftime("%d%m%Y")

def get_current_time():
    t = localtime()
    return strftime("%H:%M:%S", t)

def log(message):
    current_time = get_current_time()
    formatted_message = f"{current_time}: {message}\n"
    with open(today_log, "w", encoding="utf-8") as log_output:
        log_output.write(formatted_message)
    print(current_time, ":", message)

def set_fishing_rod(account=None):
    log("...")

    if account is None:
        with open("pesca_a_dor/core/infos.json", "r") as file:
            config_json = load(file)

        area = config_json["REGION_FISHING"]
        sleep_duration = 0.5
    else:
        area = account["REGION_FISHING"]
        sleep_duration = 1

    area_center = center((area[0], area[1], IMG_BUBBLE_SIZE[0], IMG_BUBBLE_SIZE[1]))
    moveTo(area_center)
    sleep(sleep_duration)
    click(button="left")
    press_and_release('numlock')
    return area

def wait_bubble(REGION_FISHING):
    while True:
        bubble = locateOnScreen(bubble_img, confidence=0.7, region=(REGION_FISHING[0], REGION_FISHING[1], IMG_BUBBLE_SIZE[0], IMG_BUBBLE_SIZE[1]))
        if bubble != None:
            press_and_release('numlock')
            break

def minigame(counter):
    sleep(1)
    fish = True
    message = None
    while fish != None:
        bar = locateOnScreen(bar_img, confidence=0.7, region=REGION_MINIGAME)
        fish = locateOnScreen(fish_img, confidence=0.7, grayscale=True, region=REGION_MINIGAME)
        if bar != None and fish != None:
            message="Solving puzzle..."
            if bar.top > fish.top:
                press('space')
            else:   
                release('space')
        else:
            press_and_release('space')
    if message != None:
        log(message)
        counter += 1
    return counter

def kill_shiny(pokemon_list, use_thread_kill_shiny, account=None):
    if use_thread_kill_shiny:
        for pokemon_info in pokemon_list:
            pokemon_name, img_path, confidence = pokemon_info
            shiny_found = False
            while True:
                shiny = locateOnScreen(img_path, confidence=confidence, region=REGION_BATTLE)
                if shiny == None:
                    break

                log("Wild {} appeared!".format(pokemon_name))
                press_and_release('backspace')

                press_hotkey = POKEMON_ATTACK_HOTKEY.get(pokemon_name, [])
                
                for key in press_hotkey:
                    press_and_release(key)
                    sleep(0.6)
            
                revive()
                order_pokemon(account)
                shiny_found = True

            if shiny_found and pokemon_name == "pokémon":
                ball_shiny("Shiny Krabby", krabby_img, 'F10', 0.7)
                ball_shiny("Shiny Tentacool", tentacool_img, 'F11', 0.85)
                ball_shiny("Shiny Giant Magikarp", shiny_giant_karp_img, 'F10', 0.85, offset_x=15, offset_y=15)
                ball_shiny("Shiny Magikarp", magikarp_img, 'F10', 0.9, offset_x=1, offset_y=1)
                ball_shiny("Shiny Gyarados", dead_gya_img, 'F10', 0.85)
                ball_shiny("Shiny Tentacruel", dead_cruel_img, 'F11', 0.85)

def ball_shiny(pokemon_name, img_path, key, confidence, offset_x=0, offset_y=0):
    sleep(0.5)
    pokemon_found = True
    while pokemon_found != None:
        pokemon_found = locateOnScreen(img_path, confidence=confidence, region=REGION_POKEBODY)
        if pokemon_found != None:
            log("{} defeated!".format(pokemon_name))
            pokemon_center = center(pokemon_found)
            if offset_x > 0:
                moveTo(pokemon_center[0] + offset_x, pokemon_center[1] + offset_y)
                sleep(0.5)
                click(button="right")
                sleep(1)
                press_and_release('right')
                sleep(0.2)
                press_and_release('right')
                sleep(0.2)
                press_and_release('right')
                sleep(1)
            moveTo(pokemon_center[0] + offset_x, pokemon_center[1] + offset_y)
            sleep(0.8)
            press_and_release(key)
            sleep(0.5)
            mouseDown(pokemon_center[0] + offset_x, pokemon_center[1] + offset_y)
            mouseUp()
            return True
        else:
            return False   

def some_actions(use_thread_kill_shiny, account=None):
    if stop_event.is_set():
        return
    
    #if use_thread_kill_shiny and threadKillShiny.is_alive():
    #    threadKillShiny.join()
    
    sleep(0.5)
    check_hook(use_thread_kill_shiny, account)
    feed_pokemon()
    press_and_release('ctrl+F5')
    press_and_release('tab')

def constant_search_dragon():
    shiny = True
    while shiny != None:
        shiny = locateOnScreen(shiny_img, confidence=0.9)
        if shiny != None:
            return True
        else:
            sleep(1)
    return False

def ball_dragon():
    log("Wild pokémon appeared!")
    while True:
        if stop_event.is_set():
            break

        pause_event.wait()
        config_json["USE_THREAD_BALL_DRAGON"] = False
        sleep(0.5)
        dratini = ball_shiny("Shiny Dratini", dratini_img, 'F12', 0.73)
        dragonair = ball_shiny("Shiny Dragonair", dragonair_img, 'F12', 0.69)

        # fishing with two characters - only one catching!
        krabby = ball_shiny("Shiny Krabby", krabby_img, 'F10', 0.7)
        tentacool = ball_shiny("Shiny Tentacool", tentacool_img, 'F11', 0.85)

        if dratini or dragonair:
            config_json["USE_THREAD_BALL_DRAGON"] = True
            break
        sleep(1)

def ball_normal():
    while True:
        if stop_event.is_set():
            break

        pause_event.wait()
        normal = locateOnScreen(normal_dragonair_img, confidence=0.69)
        if normal == None:
            break

        config_json["USE_THREAD_BALL_DRAGON"] = False
        sleep(0.5)

        #normal_dratini = ball_shiny("Dratini", normal_dratini_img, 'F10', 0.73)
        normal_dragonair = ball_shiny("Dragonair", normal_dragonair_img, 'F10', 0.69)

        if normal_dragonair:
        #if dratini or dragonair or krabby or tentacool:
            print("Normal pokémon appeared!")
            config_json["USE_THREAD_BALL_DRAGON"] = True
            #break
        sleep(0.5)

def find_elixir():
    use_elixir = config_json["FISH_MAGIKARP"]
    while use_elixir:
        elixir = locateOnScreen(elixir_img, confidence=0.9, region=REGION_ELIXIR)
        if elixir != None:
            return True
        else:
            return False

def change_pokemon(message):
    log(message)
    moveTo(REGION_POKEBALL, duration=0.5)
    sleep(0.5)
    click(button="right")
    sleep(1)
    moveTo(1735, 306)
    sleep(0.5)
    dragTo(1735, 243, button="left", duration=1)
    sleep(0.5)
    click(1735, 242, button="right")
    sleep(1)

def use_bait(message):
    sleep(1)
    log(message)
    press_and_release('ctrl+F2')

def use_elixir(message):
    sleep(1)    
    log(message)
    press_and_release('ctrl+F3')

def get_pokemon_info():
    electabuzz = locateOnScreen(electabuzz_img, confidence=0.9, region=REGION_POKEBALL_SLOT)
    shedinja = locateOnScreen(shedinja_img, confidence=0.9, region=REGION_POKEBALL_SLOT)
    if electabuzz != None:
        pokemon = "electabuzz"
    elif shedinja != None:
        pokemon = "shedinja"
    return pokemon 

def apply_elixir_mode(use_thread_kill_shiny, account=None):
    
    log("Starting elixir mode!")
    sleep(0.5)

    if account is None:
        original_use_thread_kill_shiny = use_thread_kill_shiny
        use_thread_kill_shiny = True
        pokemon = get_pokemon_info()

        if pokemon == "shedinja":
            sleep(1)
            combat = locateOnScreen(combat_img, confidence=0.9, region=REGION_COMBAT)
            while combat is not None:
                combat = locateOnScreen(combat_img, confidence=0.9, region=REGION_COMBAT)
                sleep(1)
            change_pokemon("Changing pokémon")
            order_pokemon()

        use_bait("Removing bait")
        use_elixir("Using fisherman's elixir")
        start_time = time()

        while config_json["FISH_MAGIKARP"] and time() - start_time < 300:
            threadSomeActions = Thread(target=some_actions, args=(use_thread_kill_shiny))
            fishing_position = set_fishing_rod()
            start_and_join_thread(threadKillShiny, kill_shiny, (KILL_POKEMON_LIST, use_thread_kill_shiny))
            start_and_join_thread(threadSomeActions, some_actions, (use_thread_kill_shiny,))
            wait_bubble(fishing_position)
            minigame(counter)

        start_and_join_thread(threadKillShiny, kill_shiny, (KILL_POKEMON_LIST, use_thread_kill_shiny))
        sleep(0.5)
        log("Exiting elixir mode!")

        if pokemon == "shedinja":
            sleep(1)
            combat = locateOnScreen(combat_img, confidence=0.9, region=REGION_COMBAT)
            while combat is not None:
                combat = locateOnScreen(combat_img, confidence=0.9, region=REGION_COMBAT)
                sleep(1)
            change_pokemon("Changing pokémon")
            order_pokemon()

        config_json["USE_THREAD_KILL_SHINY"] = original_use_thread_kill_shiny 
        use_bait("Applying bait")
        sleep(1)
        return config_json["USE_THREAD_KILL_SHINY"]

    else:
        use_thread_kill_shiny = True
        release_pokemon("Releasing pokémon")
        order_pokemon(account)
        use_elixir("Using fisherman's elixir")
        start_time = time()

        while use_thread_kill_shiny and time() - start_time < 300:
            threadSomeActions = Thread(target=some_actions, args=(use_thread_kill_shiny, account))
            fishing_position = set_fishing_rod(account)
            start_and_join_thread(threadKillShiny, kill_shiny, (KILL_POKEMON_LIST, use_thread_kill_shiny, account))
            start_and_join_thread(threadSomeActions, some_actions, (use_thread_kill_shiny, account))
            wait_bubble(fishing_position)
            minigame(counter)

        start_and_join_thread(threadKillShiny, kill_shiny, (KILL_POKEMON_LIST, use_thread_kill_shiny, account))
        sleep(0.5)
        log("Exiting elixir mode!")

def check_hook(use_thread_kill_shiny, account=None):
    #if use_thread_kill_shiny and threadKillShiny.is_alive():
    #    threadKillShiny.join()
    sleep(1)

    if account is None:
        with open("pesca_a_dor/core/infos.json", "r") as file:
            config_json = load(file)
        
        area = config_json['REGION_FISHING']
    
    else:
        area = account["REGION_FISHING"]
    
    hook = True
    while hook != None: 
        hook = locateOnScreen(hook_img, confidence=0.5, region=(area[0], area[1], area[0] + IMG_HOOK_SIZE[0], area[1] + IMG_HOOK_SIZE[1]))
        if hook == None:
            sleep(3)
            log("Fixing fishing position...")
            set_fishing_rod(account)
        break

def feed_pokemon():
    while True:
        hungry = locateOnScreen(hungry_img, confidence=0.91, region=REGION_HUNGRY)
        if hungry != None:
            log("Feeding pokémon...")
            press_and_release('capslock')
        break

def order_pokemon(account=None):
    if account is None:
        press_and_release('tab')
    else: 
        moveTo(REGION_POKE, duration=0.3)
        press_and_release('f2')
        sleep(0.4)
        press_and_release('f2')
        sleep(0.4)
        press_and_release('f2')
        sleep(0.4)
        press_and_release('f2')
        sleep(0.4)
        press_and_release('f2')
        sleep(0.4)
        press_and_release('f2')
        sleep(0.4 )
        press_and_release('tab')

def revive():
    moveTo(REGION_POKEBALL, duration=0.3)
    sleep(0.1)
    click(button="right", duration=1)
    sleep(0.1)
    press_and_release('f1')
    sleep(0.1)
    click(button="right", duration=1)

def start_and_join_thread(thread, target, args=()):
    if not thread.is_alive():
        thread = Thread(target=target, args=args)
        thread.start()
    thread.join()

def join_thread_if_alive(thread):
    if thread is not None and thread.is_alive():
        thread.join()

def logout_session(counter):
    if minigame_repeats == counter:
        log("Session complete. Logging out now.")
        sleep(20)
        press_and_release("ctrl+q")
        sleep(1)
        press_and_release("enter")

def is_capslock_on():
    return ctypes.windll.user32.GetKeyState(0x14) == 1 # capslock on

def disable_capslock():
    if is_capslock_on():
        press('capslock')
        
def login(email, password, user_image_path, char):
    disable_capslock()
    sleep(3)
    click(REGION_EMAIL, duration=0.3)
    write(email)
    sleep(0.3)

    click(REGION_PASSWORD, duration=0.3)
    write(password)
    sleep(0.3)         

    click(REGION_LOGIN, duration=0.3)
    sleep(5)

    char_image_location = locateOnScreen(user_image_path, confidence=0.65)

    if char_image_location:
        moveTo(char_image_location)
        sleep(1)
        doubleClick(char_image_location)
        log(f"Logging with {char}...")
    else:
        log(f"{char} not found. Exiting.")
    
    sleep(5)

def logout():
    combat = locateOnScreen(combat_img, confidence=0.9, region=REGION_COMBAT)
    while combat != None:
        combat = locateOnScreen(combat_img, confidence=0.9, region=REGION_COMBAT)
    sleep(1)
    log("Session complete. Logging out now.")
    sleep(1)
    press_and_release("ctrl+q")
    sleep(1)
    press_and_release("enter")
    sleep(1)
    press_and_release("esc")
    sleep(1)
    moveTo(REGION_CONFIRM_LOGOUT)
    sleep(0.2)
    click(button="left")

def release_pokemon(message):
    log(message)
    moveTo(REGION_POKEBALL, duration=0.5)
    sleep(0.5)
    click(button="right")
    sleep(1)

def main_pesca_a_dor():
    """Main function."""
    log("-------------------")
    log(f"PESCA-A-DOR {VERSION}")
    log("-------------------")
    log(f"{START_KEY}   → Start")
    log(f"{PAUSE_KEY} → Pause")
    log(f"{STOP_KEY}       → Exit")
    log("-------------------")
    
    with open("pesca_a_dor/core/infos.json", "r") as file:
        config_json = load(file)
    
    global counter
    while counter < minigame_repeats:
        pause_event.wait()
        REGION_FISHING = set_fishing_rod()
        start_and_join_thread(threadKillShiny, kill_shiny, (KILL_POKEMON_LIST, config_json["USE_THREAD_KILL_SHINY"]))
        start_and_join_thread(threadSomeActions, some_actions, (config_json["USE_THREAD_KILL_SHINY"],))
        
        if constant_search_dragon() and config_json["USE_THREAD_BALL_DRAGON"]:
            threadSearchDragon = Thread(target=ball_dragon)
            threadSearchDragon.start()
        
        wait_bubble(REGION_FISHING)
        counter = minigame(counter)

        if find_elixir() and config_json["FISH_MAGIKARP"]:
            config_json["USE_THREAD_KILL_SHINY"] = apply_elixir_mode(config_json["USE_THREAD_KILL_SHINY"])
        
        logout_session(counter)

    join_thread_if_alive(threadSearchDragon)

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
        sleep(15)

def main():
    parser = argparse.ArgumentParser(description="pesca-a-dor: fishing bot for PokeXGames")
    parser.add_argument('-m', '--mode', type=int, choices=[1, 2], required=True, help='Select mode: 1 for pesca-a-dor, 2 for money-maker')
    args = parser.parse_args()
    
    if args.mode == 1:
        main_pesca_a_dor()
    elif args.mode == 2:
        main_money_maker()
    
# control global events
pause_event = Event()
stop_event = Event()

# register keys to turn on/off the trainer
add_hotkey(START_KEY, start_loop)
add_hotkey(PAUSE_KEY, pause_loop)
add_hotkey(STOP_KEY, stop_loop)

threadKillShiny = Thread(target=kill_shiny, args=(KILL_POKEMON_LIST, config_json["USE_THREAD_KILL_SHINY"]))
threadSomeActions = Thread(target=some_actions, args=(config_json["USE_THREAD_KILL_SHINY"],))
threadSearchDragon = Thread(target=ball_dragon, args=(config_json["USE_THREAD_BALL_DRAGON"],))
threadSearchNormal = Thread(target=ball_normal, args=(config_json["USE_THREAD_BALL_DRAGON"],))

with open("pesca_a_dor/core/infos.json", "r") as file:
    config_json = load(file)

today_log="logs/{}.txt".format(get_current_day())