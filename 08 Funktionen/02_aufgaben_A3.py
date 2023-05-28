"""
Aufgabe

Schreibe eine Funktion für die Ausgabe des Temperaturmaximums, das eine Liste und den Namen der Stadt als Parameter enthält. 
Ersetze anschließend den vorher dafür zuständigen Code durch entsprechende Funktionsaufrufe.
Beachte bei der Implementierung auch den Fall, dass die Liste leer sein könnte.
Fange auch den Fall, dass keine Liste als Parameter eingegeben wurde, entsprechend ab.
"""

# Wetterdaten
temperatur_wiesbaden = [13, 14, 18, 19, 20, 21, 19]
temperatur_mainz = [14, 16, 17, 20, 19, 19, 23]
temperatur_frankfurt = [17, 16, 18, 16, 20, 21, 22]

temp_max = -1000
for temp in temperatur_wiesbaden:
    if temp > temp_max:
        temp_max = temp
print(
    f"Maximale Temperatur in Wiesbaden in den kommenden {len(temperatur_wiesbaden)} Tagen: {temp_max} Grad."
)

temp_max = -1000
for temp in temperatur_mainz:
    if temp > temp_max:
        temp_max = temp
print(
    f"Maximale Temperatur in Mainz in den kommenden {len(temperatur_mainz)} Tagen: {temp_max} Grad."
)

temp_max = -1000
for temp in temperatur_frankfurt:
    if temp > temp_max:
        temp_max = temp
print(
    f"Maximale Temperatur in Frankfurt in den kommenden {len(temperatur_frankfurt)} Tagen: {temp_max} Grad."
)
