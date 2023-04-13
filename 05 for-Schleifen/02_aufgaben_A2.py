"""
1. Aufgabe

Im unten stehenden Code findest du erneut den Code zur Erzeugung der Temperaturübersicht aus dem Eingangsbeispiel.
Implemtiere den Code durch Verwendung einer for-Schleife so, dass er mit lediglich einem print-Befehl auskommt.
Solltest du nicht weiterkommen, nutze die Tipps.

Tipp 1:
  Um die Temperaturdaten auszulesen, musst du in jedem Schleifendurchlauf auf das jeweilige Listenelement zugreifen.

Tipp 2:
  Ist i gegeben, greifst du mit temperatur[i] auf das i-te Listenelement zu.
"""

"""
2. Aufgabe

Der Befehl len(list) gibt die Länge einer Liste list zurück. 
Ändere deinen Code aus Aufgabe 1 so ab, 
dass stets alle Elemente der Liste temperatur in der for-Schleife ausgegeben werden, 
egal wie viele Elemente in der Liste sind. 
Prüfe deine Implementierung mit unterschiedlich langen Listen.
"""

"""
3. Aufgabe (Für Schnelle)

Implementiere zusätzlich Code, sodass dein Programm auch die maximale Temperatur in der Liste ausgibt.

Solltest du nicht weiterkommen, nutze die Tipps.

Tipp 1:
  Hilfsvariable, die vor der for-Schleife deklariert wird. 

Tipp 2:
  Die Hilfsvariable speichert immer ab, welche maximale Temperatur bisher in der Schleife gefunden wurde.

Tipp 3:
  Die Hilfsvariable sollte bei der Deklaration einen sehr kleinen Wert haben, der auf jeden Fall überschritten wird.
  Siehe auch hier: https://www.codingem.com/python-max-and-min-values-for-integers/
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
