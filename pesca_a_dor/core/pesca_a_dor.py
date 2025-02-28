from threading import Thread
from core.actions import log, pause_event, set_fishing_rod, threadKillShiny, some_actions, start_and_join_thread, constant_search_dragon, ball_dragon, kill_shiny, wait_bubble, minigame, find_elixir, apply_elixir_mode, logout_session, join_thread_if_alive
from core.config import *

threadSomeActions = Thread(target=some_actions, args=(config_json["USE_THREAD_KILL_SHINY"],))

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