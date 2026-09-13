"""
Failinimi: generate_data.py
Kirjeldus: Kood genereerib 200 juhuslikku täisarvu vahemikus 1 kuni 100 ja prindib neid välja
Autor: Taissija Rychkova
"""

import random as rnd

def main():
    #genereeritakse 200 arvu listi 1-1000 vahemikus
    random_nums = [rnd.randint(1,1000) for i in range(200)]
    #prinditakse iga arvu uuel real faili salvestamise mugavuseks
    for num in random_nums:
        print(num)
if __name__ == "__main__":
    main()
