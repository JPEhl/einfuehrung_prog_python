# Abfrage des Geburtsjahres
name = input("Nenne mir deinen Namen: ")
jahr = int(input("Gib an, in welchem Jahr du geboren bist: "))
atemzuege_10_sek = int(input("Wie oft atmest du in 10 Sekunden ein und aus: "))

# Berechnung der Atemzüge
jahre = 2023 - jahr
tage = jahre * 365
stunden = tage * 24
minuten = stunden * 60
atemzuege = minuten * 6 * atemzuege_10_sek

# Ausgabe des Ergebnisses
print("Hallo", name, ". Du hast in deinem Leben bereits etwa",
      atemzuege, "Mal ein- und ausgeatmet.")
