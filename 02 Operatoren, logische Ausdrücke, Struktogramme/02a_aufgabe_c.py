"""
(Für Schnelle) 

In dieser Aufgabe geht es um das Würfelspiel „Mäxle“. 
Dabei werden zwei Würfel gleichzeitig geworfen und jede Spielerin / jeder Spieler hat das Ziel, einen „höheren“ Wurf als die Vorgängerin bzw. der Vorgänger zu werfen.
Bei einem Wurf ist stets die höhere Augenzahl die Zehnerstelle und die niedrigere die Einerstelle. Die beiden Augenzahlen 3 und 5 ergeben also z.B. die Zahl 53.

Zwei gleiche Augenzahlen gelten als Pasch, die 1 und die 2 (also 21) als „Mäxle“. 
Die Reihenfolge ist: „normale Zahlen“ wie 31, 32, 41,..., 65; dann die Päsche 11, 22, ..., 66 und schließlich als höchstes Ergebnis das „Mäxle“ (21). 

Im folgenden Code wird ein Würfelwurf simuliert. Gib mit logischen Verknüpfungen an, ob folgende Ereignisse wahr oder falsch sind:
    -Beide Würfel zeigen die Augenzahl 4.
    -Es wird ein Pasch oder das „Mäxle“ gewürfelt.
    -Es wird eine „normale Zahl“, aber nicht das „Mäxle“ gewürfelt.
    -Es wird eine „normale Zahl“ über 60 gewürfelt. (D.h. der Sechserpasch ist nicht dabei)
    -Denke dir noch weitere Ereignisse aus und formuliere dazu die passenden Aussagen (als Kommentare im Code)
"""

import random

# Zufallszahl zwischen 1 und 6 für beide Würfel
wuerfel_1 = random.randint(1, 6)
wuerfel_2 = random.randint(1, 6)

# Ausgabe des Würfelwurfs
print(f"Gewürfelt wurde {wuerfel_1}{wuerfel_2}")

# Beide Würfel zeigen die Augenzahl 4.

# Es wird ein Pasch oder das „Mäxle“ gewürfelt.

# Es wird eine „normale Zahl“, aber nicht das „Mäxle“ gewürfelt.

# Es wird eine „normale Zahl“ über 60 gewürfelt. (D.h. der Sechserpasch ist nicht dabei)
