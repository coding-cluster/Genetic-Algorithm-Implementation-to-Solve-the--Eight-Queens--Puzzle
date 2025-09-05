import time
import os

def logo():
    clear_screen()
    logo_el = (".-    .-..  .     -..-  ..    ...",
               "A     L     E     X     I     S",
               "--..  ..-   -.    ..    --.   .-",
               "Z     Ú     Ñ     I     G     A")
    
    for el in logo_el:
        print(el)
        time.sleep(0.15)  # Pausa de 250 ms
    
    for i in range(1, 34):
        print('-', end='')
        time.sleep(0.03)  # Pausa de 150 ms
    print()

def clear_screen():
    if os.name == "nt":
        _ = os.system("cls")
    else:
        _ = os.system("clear")