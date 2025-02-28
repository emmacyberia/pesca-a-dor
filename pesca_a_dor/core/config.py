from json import load

# software version
VERSION = "v1.0"

# define status and core variables
#loop_status = False
START_KEY = "PAGE UP"
PAUSE_KEY = "PAGE DOWN"
STOP_KEY = "END"

# global variables
#USE_THREAD_KILL_SHINY = False        # Set as True/False if do/dont want to use threadKillShiny on main loop
#USE_THREAD_BALL_DRAGON = True        # Set as True/False if do/dont want to project dragonair on main loop
#FISH_MAGIKARP = False                # Set as True to activate elixir mode 
#MONEY_MAKER = False
IMG_BUBBLE_SIZE = (26,28)          
IMG_HOOK_SIZE = (30, 30)
REGION_BATTLE = (1714, 383, 206, 323)

#REGION_FISHING = (1646, 243)        # pewter paras/diglett
#REGION_FISHING = (1574, 393)        # pewter-cerulean road (dragonair)
#REGION_FISHING = (1391, 284)        # pewter-cerulean road (magikarp)

#REGION_FISHING = (952, 430)         # vermilion west (dragonair)
#REGION_FISHING = (1208, 321)        # hamlin lake

#REGION_FISHING = (1464, 430)        # cerulean CP 
#REGION_FISHING = (1537, 430)        # hamlin east 

REGION_MINIGAME = (991,253,268,455)  
REGION_HUNGRY = (1877,244,17,20)   
REGION_POKEBALL = (1730, 246)      
REGION_POKEBALL_SLOT = (1717, 228, 34, 34)
REGION_POKEBODY = (1209, 359, 193, 155)
REGION_ELIXIR = (1382, 879, 36,21)
REGION_COMBAT = (960, 850, 110, 70)
#REGION_POKE = (1337, 404)            # north     
REGION_POKE = (1292, 435)             # left 
#REGION_POKE = (1252, 441)            # two left

REGION_EMAIL = (1026, 365)
REGION_PASSWORD = (1015, 472)
REGION_LOGIN = (1090, 604)
REGION_CONFIRM_LOGOUT = (1426, 565)

# img path
bubble_img='pesca_a_dor/assets/images/bubble.PNG'
bar_img='pesca_a_dor/assets/images/bar.PNG'
fish_img='pesca_a_dor/assets/images/fish_bin.PNG'
shiny_img='pesca_a_dor/assets/images/shiny.PNG'
krabby_img='pesca_a_dor/assets/images/krabby.PNG'
tentacool_img='pesca_a_dor/assets/images/tentacool.PNG'
dratini_img='pesca_a_dor/assets/images/dratini.PNG'
dragonair_img='pesca_a_dor/assets/images/dragonair.PNG'
giant_karp_img='pesca_a_dor/assets/images/giant_karp.PNG'
shiny_giant_karp_img='pesca_a_dor/assets/images/shiny_giant_karp.PNG'
magikarp_img='pesca_a_dor/assets/images/magikarp.PNG'
shiny_karp_img='pesca_a_dor/assets/images/shiny_karp.PNG'
feebas_img='pesca_a_dor/assets/images/feebas.PNG'
hungry_img='pesca_a_dor/assets/images/hungry.PNG'
hook_img='pesca_a_dor/assets/images/hook.PNG'
elixir_img='pesca_a_dor/assets/images/elixir.PNG'
combat_img='pesca_a_dor/assets/images/combat.PNG'
electabuzz_img='pesca_a_dor/assets/images/electabuzz.PNG'
shedinja_img='pesca_a_dor/assets/images/shedinja.PNG'
battle_img='pesca_a_dor/assets/images/battle.PNG'
walrein_img='pesca_a_dor/assets/images/walrein.PNG'
mantine_img='pesca_a_dor/assets/images/mantine.PNG'
lapras_img='pesca_a_dor/assets/images/lapras.PNG'
gyarados_img='pesca_a_dor/assets/images/gyarados.PNG'
kingdra_img='pesca_a_dor/assets/images/kingdra.PNG'
tentacruel_img='pesca_a_dor/assets/images/tentacruel.PNG'
dead_gya_img='pesca_a_dor/assets/images/dead_gya.PNG'
dead_cruel_img='pesca_a_dor/assets/images/dead_cruel.PNG'
normal_dratini_img='pesca_a_dor/assets/images/normal_dratini.PNG'
normal_dragonair_img='pesca_a_dor/assets/images/normal_dragonair.PNG'

# list of tuples containing pokemons to kill_shiny
'''
KILL_POKEMON_LIST = [
    ("pokémon", shiny_img, 0.9),
    ("Feebas", feebas_img, 0.85),
    ("Giant Magikarp", giant_karp_img, 0.9),
]
'''

KILL_POKEMON_LIST = [
    ("pokémon", shiny_img, 0.9),
    ("Feebas", feebas_img, 0.85),
    ("Giant Magikarp", giant_karp_img, 0.9),
    ("Walrein", walrein_img, 0.85),
    ("Mantine", mantine_img, 0.85),
    ("Lapras", lapras_img, 0.85),
    ("Gyarados", gyarados_img, 0.85),
    ("Kingdra", kingdra_img, 0.85),
    ("Tentacruel", tentacruel_img, 0.85)
]

with open("pesca_a_dor/core/infos.json", "r") as file:
    config_json = load(file)

if config_json["MONEY_MAKER"]:
    POKEMON_ATTACK_HOTKEY = {
        "pokémon": ['F8', 'F7', 'F4', 'F5', 'F6'],
        "Feebas": ['F8', 'F7', 'F4', 'F5', 'F6'],
        "Giant Magikarp": ['F8', 'F7', 'F4', 'F5', 'F6']
    }

else:
    POKEMON_ATTACK_HOTKEY = {
        "pokémon": ['F7', 'F6', 'F4', 'F5'],
        "Feebas": ['F7', 'F6', 'F4', 'F5'],
        "Giant Magikarp": ['F7', 'F6', 'F4', 'F5'],
        "Walrein": ['F7', 'F6', 'F4', 'F5'],
        "Mantine": ['F7', 'F6', 'F4', 'F5'],
        "Lapras": ['F7', 'F6', 'F4', 'F5'],
        "Gyarados": ['F7', 'F6', 'F4', 'F5'],
        "Kingdra": ['F7', 'F6', 'F4', 'F5'],
        "Tentacruel": ['F7', 'F6', 'F4', 'F5']
    }

# minigame repeats
''' Set the number of minigame_repeats
    A minigame appears for every 4 minutes on average
    minigame_repeats = 100 -> AFK fishing for ~6.5 hours '''

minigame_repeats = 100   # 100
counter = 0