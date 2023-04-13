"""
1. Aufgabe

Im unten stehenden Code findest du erneut den Code zur Erzeugung der Temperaturübersicht aus dem Eingangsbeispiel.
Implementiere den Code durch Verwendung einer for-Schleife so, dass er mit lediglich einem print-Befehl auskommt.
Solltest du nicht weiterkommen, nutze die Tipps.

Tipp 1:
  Um die Temperaturdaten auszulesen, musst du in jedem Schleifendurchlauf auf das jeweilige Listenelement zugreifen.

Tipp 2:
  Ist i gegeben, greifst du mit temperatur[i] auf das i-te Listenelement zu.
"""

"""
2. Aufgabe

Du hast in der Klammer des range-Befehls wahrscheinlich eine feste Zahl eingefügt.
So funktioniert der Code auch problemlos. 
Erkläre kurz, welche Nachteile das Eingeben einer festen Zahl mit sich bringt.

Schreibe deine Antwort hier in die Kommentare:


"""

# Temperaturdaten
temperatur = [16, 14, 12, 8, 9, 12, 13, 17]

# Ausgabe der Wetterdaten --> DIESEN CODE ABÄNDERN
print(f"Tag 0: {temperatur[0]} Grad.")
print(f"Tag 1: {temperatur[1]} Grad.")
print(f"Tag 2: {temperatur[2]} Grad.")
print(f"Tag 3: {temperatur[3]} Grad.")
print(f"Tag 4: {temperatur[4]} Grad.")
print(f"Tag 5: {temperatur[5]} Grad.")
print(f"Tag 6: {temperatur[6]} Grad.")
print(f"Tag 7: {temperatur[7]} Grad.")
