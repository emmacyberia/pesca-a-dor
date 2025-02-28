from pyautogui import locateOnScreen, position
import pesca_a_dor.core.config as config

# function to locate the (left, top) position of each image
while True:
    bubble = locateOnScreen(config.bubble_img, confidence=0.7)
    hook = locateOnScreen(config.hook_img, confidence=0.5)
    bar = locateOnScreen(config.bar_img, confidence=0.7)
    fish = locateOnScreen(config.fish_img, confidence=0.7, grayscale=True)
    hungry = locateOnScreen(config.hungry_img, confidence=0.91, region=(982,236,17,20))
    krabby = locateOnScreen(config.krabby_img, confidence=0.7)
    tentacool = locateOnScreen(config.tentacool_img, confidence=0.88)
    feebas = locateOnScreen(config.feebas_img, confidence=0.8)
    giant_karp = locateOnScreen(config.giant_karp_img, confidence=0.90)
    shiny_giant_karp = locateOnScreen(config.shiny_giant_karp_img, confidence=0.85, region=(1180, 350, 180, 140))
    magikarp = locateOnScreen(config.magikarp_img, confidence=0.9)
    shiny_dratini = locateOnScreen(config.dratini_img, confidence=0.69)
    shiny_dragonair = locateOnScreen(config.dragonair_img, confidence=0.69)
    elixir = locateOnScreen(config.elixir_img, confidence=0.8, region=(1382, 879, 36,21))
    combat = locateOnScreen(config.combat_img, confidence=0.9, region=(960, 850, 110, 70))
    electabuzz = locateOnScreen(config.electabuzz_img, confidence=0.95, region=(1717, 228, 34, 34))
    shedinja = locateOnScreen(config.shedinja_img, confidence=0.9, region=(1717, 228, 34, 34))
    battle = locateOnScreen(config.battle_img, confidence=0.9)

    print(position())                       # mouse position
    #print("bubble",bubble)                 # bubble and hook positions
    #print("hook",hook)
    #print("bar",bar)                       # minigame features positions
    #print("fish",fish)
    #print("hungry",hungry)                 # hungry position (the icon must be RED if the pokemon is hungry)
    #print("shiny krabby",krabby)           # dead pokemon positions
    #print("shiny tentacool",tentacool)
    #print("shiny giant magikarp", shiny_giant_karp)
    #print("shiny magikarp", magikarp)
    #print("shiny dratini",shiny_dratini)
    #print("shiny dragonair",shiny_dragonair)
    #print("normal dratini",normal_dratini)
    #print("normal dragonair",normal_dragonair)
    #print("elixir",elixir)
    #print("combat",combat)
    #print("electabuzz",electabuzz)
    #print("shedinja",shedinja)
    #print("battle",battle)
    #print("karpa",karpa)