"""
Für Schnelle: 
In dieser Aufgabe wurde ein Timer erstellt, der in 1-Sekunden-Schritten immer eine Zahl hochzählt. 
Der Timer beginnt bei einer Zufallszahl. Ergänze das Programm so, dass damit die Uhrzeit angezeigt wird. 
Die Zahl 0 der Zahl bedeutet dabei 0:00 Uhr.
(Für besondere Ästheten: ein String str lässt sich mit str.zfill(2) mit führenden 0en schreiben.)
"""

import time
import random
from IPython.display import clear_output

# Anzahl Sekunden des Tags
TAG_SEKUNDEN = 86400  # z.B. 24 Stunden = 86400 Sekunden

# Zufallszahl zwischen 0 und Anzahl Sekunden des Tags
zufallszahl = random.randint(0, TAG_SEKUNDEN)

# Schleife, die jede Sekunde läuft
while True:
    # Ausgabe in der Zelle löschen
    clear_output(wait=True)

    # Ausgabe der Zufallszahl zur Kontrolle
    print(f"zufallszahl = {zufallszahl}")

    """ Hier kommt dein Code hin"""

    # Zufallszahl erhöhen
    zufallszahl += 1
    # 1 Sekunde pausieren
    time.sleep(1)
