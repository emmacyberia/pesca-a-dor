from tkinter.ttk import Label, Button, Style
from tkinter import messagebox
from ttkthemes import ThemedTk
from PIL import Image, ImageTk
import keyboard
import pyautogui
import pesca_a_dor.core.config as config
import json
import threading
import pynput
import pesca_a_dor.core.actions as actions

pyautogui.PAUSE = 0.01

with open("pesca_a_dor/core/infos.json", "r") as file:
    config_json = json.load(file)

root = ThemedTk(theme="radiance", themebg=True)
root.iconbitmap(default="ui/assets/images/fishing_rod.ico")

root.title("pesca-a-dor")
root.resizable(False, False)
style = Style()
style.configure("TButton", font=("Roboto", 10))
style.configure("ON.TButton", foreground="green", font=("Roboto", 10, "bold"))
style.configure("OFF.TButton", foreground="red", font=("Roboto", 10, "bold"))
style.configure('TCheckbutton', font=('Roboto', 10))

fishing_position = ''

def load_image():
    image = Image.open("ui/assets/images/trash.png")
    resized = image.resize((20,20))
    return ImageTk.PhotoImage(resized)

def widget(widget, row, column, sticky="NSEW", columnspan=None, **kwargs):
    new_widget = widget(**kwargs)
    new_widget.grid(row=row, column=column, padx=5, pady=5, sticky=sticky, columnspan=columnspan)
    return new_widget

def get_fishing_position():
    global fishing_position
    messagebox.showinfo(title="Fishing Position", message="Place the mouse over 'Fishing Position' and press 'Insert'")
    keyboard.wait('insert')
    x, y = pyautogui.position()
    label_fishing_position.configure(text=f"({x}, {y})")
    fishing_position = [x, y]

def clear():
    label_fishing_position.configure(text="Empty")

def kill_shiny():
    config_json["USE_THREAD_KILL_SHINY"] = not config_json["USE_THREAD_KILL_SHINY"]

    if config_json["USE_THREAD_KILL_SHINY"]:
        button_kill_shiny.configure(style="ON.TButton") 
    else:
        button_kill_shiny.configure(style="OFF.TButton")
    
    print(f'USE_THREAD_KILL_SHINY state: {config_json["USE_THREAD_KILL_SHINY"]}')
    return config_json["USE_THREAD_KILL_SHINY"]

def elixir():
    config_json["FISH_MAGIKARP"] = not config_json["FISH_MAGIKARP"]

    if config_json["FISH_MAGIKARP"]:
        button_elixir.configure(style="ON.TButton") 
    else:
        button_elixir.configure(style="OFF.TButton")
    
    print(f'FISH_MAGIKARP state: {config_json["FISH_MAGIKARP"]}')
    return config_json["FISH_MAGIKARP"]

def auto_catch_dragonair():
    config_json["USE_THREAD_BALL_DRAGON"] = not config_json["USE_THREAD_BALL_DRAGON"]

    if config_json["USE_THREAD_BALL_DRAGON"]:
        button_auto_catch_dragonair.configure(style="ON.TButton") 
    else:
        button_auto_catch_dragonair.configure(style="OFF.TButton")

    print(f'USE_THREAD_BALL_DRAGON state: {config_json["USE_THREAD_BALL_DRAGON"]}')
    return config_json["USE_THREAD_BALL_DRAGON"]

def money_maker():
    config_json["MONEY_MAKER"] = not config_json["MONEY_MAKER"]

    if config_json["MONEY_MAKER"]:
        button_moneymaker.configure(style="ON.TButton") 
    else:
        button_moneymaker.configure(style="OFF.TButton")

    print(f'MONEY_MAKER state: {config_json["MONEY_MAKER"]}')
    return config_json["MONEY_MAKER"]

def save():
    my_data = {
        "FISHING_POSITION": fishing_position,
        "USE_THREAD_KILL_SHINY": "ON.TButton" in button_kill_shiny.configure('style'),
        "USE_THREAD_BALL_DRAGON": "ON.TButton" in button_auto_catch_dragonair.configure('style'),
        "FISH_MAGIKARP": "ON.TButton" in button_elixir.configure('style'),
        "MONEY_MAKER": "ON.TButton" in button_moneymaker.configure('style')
    }
    with open('pesca_a_dor/core/infos.json', 'w') as file:
        file.write(json.dumps(my_data))

def load():
    with open('pesca_a_dor/core/infos.json', 'r') as file:
        data = json.loads(file.read())

    label_fishing_position.configure(text=f"({data['FISHING_POSITION'][0]}, {data['FISHING_POSITION'][1]})")
    button_kill_shiny.configure(style="ON.TButton" if data["USE_THREAD_KILL_SHINY"] else "OFF.TButton")
    button_elixir.configure(style="ON.TButton" if data["FISH_MAGIKARP"] else "OFF.TButton")
    button_auto_catch_dragonair.configure(style="ON.TButton" if data["USE_THREAD_BALL_DRAGON"] else "OFF.TButton")
    button_moneymaker.configure(style="ON.TButton" if data["MONEY_MAKER"] else "OFF.TButton")
    return data 

trash = load_image()

button_kill_shiny = widget(Button, row=1, column=0, text="Kill Shiny", command=kill_shiny)
button_elixir = widget(Button, row=1, column=1, text="Fisherman's Elixir", command=elixir)
button_auto_catch_dragonair = widget(Button, row=2, column=0, text="Auto Catch Dragonair", command=auto_catch_dragonair)
button_moneymaker = widget(Button, row=2, column=1, text="Money Maker", command=money_maker)

button_fishing_position = widget(Button, row=0, column=0, text="Fishing Position", command=get_fishing_position)
label_fishing_position = widget(Label, row=0, column=1, text="Empty", font=("Roboto", 10), sticky="W")
button_fishing_position_trash = widget(Button, row=0, column=1, image=trash, sticky="E", command=clear)

def key_code(key):
    if key == pynput.keyboard.Key.esc:
        myEvent.set()
        root.deiconify()
        return False
    
def listener_keyboard():
    with pynput.keyboard.Listener(on_press=key_code) as listener:
        listener.join()

def start():
    root.iconify()
    global data
    data = load()
    global myEvent
    myEvent = threading.Event()
    global start_thread
    start_thread = threading.Thread(target=run, args=(data["FISHING_POSITION"],))
    start_thread.start()
    keyboard_thread = threading.Thread(target=listener_keyboard)
    keyboard_thread.start()

button_load = widget(Button, row=3, column=0, text="Load", command=load)
button_save = widget(Button, row=3, column=1, text="Save", command=save)
button_start = widget(Button, row=4, column=0, text="Start", columnspan=2, command=start)

data = load()

def run(initial_fishing_position):
    global fishing_position
    fishing_position = initial_fishing_position
    
    while not myEvent.is_set():    
        fishing_position = actions.set_fishing_rod()
        print(f"Fishing Position: {fishing_position}")

        actions.start_and_join_thread(actions.threadKillShiny,actions.kill_shiny,(config.KILL_POKEMON_LIST, config_json["USE_THREAD_KILL_SHINY"]))
        actions.start_and_join_thread(actions.threadSomeActions,actions.some_actions,(config_json["USE_THREAD_KILL_SHINY"],))
    
        print("actions.constant_search_dragon():", actions.constant_search_dragon())
        print('config_json["USE_THREAD_BALL_DRAGON"]:', config_json["USE_THREAD_BALL_DRAGON"])

        if actions.constant_search_dragon() and config_json["USE_THREAD_BALL_DRAGON"]:
            actions.threadSearchDragon = threading.Thread(target=actions.ball_dragon)
            actions.threadSearchDragon.start()

        actions.wait_bubble(fishing_position)
        config.counter = actions.minigame(config.counter)

        print("actions.find_elixir()", actions.find_elixir())
        print('config_json["FISH_MAGIKARP"]:', config_json["FISH_MAGIKARP"])

        if actions.find_elixir() and config_json["FISH_MAGIKARP"]:
            config_json["USE_THREAD_KILL_SHINY"] = actions.apply_elixir_mode(config_json["USE_THREAD_KILL_SHINY"])

        #actions.logout(config.counter)

    actions.join_thread_if_alive(actions.threadSearchDragon)

root.mainloop()