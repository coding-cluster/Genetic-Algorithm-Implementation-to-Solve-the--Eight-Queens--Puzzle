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
        time.sleep(0.1)  # Pausa de 100 ms
    
    for i in range(1, 34):
        print('-', end='')
        time.sleep(0.02)  # Pausa de 20 ms
    print()

def clear_screen():
    if os.name == "nt":
        _ = os.system("cls")
    else:
        _ = os.system("clear")