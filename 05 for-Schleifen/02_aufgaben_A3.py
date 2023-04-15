"""
1. Aufgabe

Im unten stehenden Code wurden 10 Städtenamen in einer Liste gespeichert.
Die Liste temperatur speichert (der Einfachheit halber zufällig) die Temperatur der nächsten 14 Tage für alle 10 Städte.

Beschreibe kurz die Datenstruktur, die in der Variable temperatur gespeichert wird, indem du sie einmal printest und dir die Ausgabe anschaust.
"""

"""
2. Aufgabe

Implementiere mit Hilfe von for-Schleifen (ohne List Comprehensions) eine übersichtliche Wetterübersicht der Städte für die nächsten Tage.

Dabei darfst du NICHT einfach Listen printen!
"""

"""
3. Aufgabe (für Schnelle)

Implemetiere das Programm weiter, sodass pro Stadt zusätzlich die Minimal- und die Maximaltemperatur angezeigt werden.
"""

"""
4. Aufgabe (für Schnelle)

Implementiere das Programm weiter, sodass pro Stadt zusätzlich die Durchschnittstemperatur angezeigt werden.
"""

"""
5. Aufgabe (für Schnelle)

Implemtiere weitere sinnvolle Eigenschaften wie beispielsweise das Wetter inklusive Anzeige der Regentage in den kommenden 14 Tagen oder Ähnliches..
"""


import random

staedte = [
    "Wiesbaden",
    "Mainz",
    "Berlin",
    "Hamburg",
    "Koeln",
    "Muenchen",
    "Dortmund",
    "Frankfurt am Main",
    "Leipzig",
    "Düsseldorf",
]
ANZ_TAGE = 14

temperatur = [[0 for i in range(ANZ_TAGE)] for j in range(len(staedte))]

for i in range(len(staedte)):
    temperatur[i][0] = random.randint(10, 20)
    for j in range(1, ANZ_TAGE):
        temperatur[i][j] = random.randint(
            temperatur[i][j - 1] - 3, temperatur[i][j - 1] + 3
        )
