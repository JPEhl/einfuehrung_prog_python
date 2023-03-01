# Eingabe von Wohnort und Einwohnerzahl und Speicherung in Variablen
# Einwohner von Deutschland ist eine Konstante, daher die Großbuchstaben
wohnort = input("Wo wohnst du?")
anz_einwohner = int(input(f"Wie viele Einwohner hat {wohnort}?"))
ANZ_DEUTSCHLAND = 80000000

# Berechnung, jeder wie vielte in Deutschland im Wohnort wohnt.
# // ist eine Ganzzahldivision, damit wird das Ergebnis ohne Kommata angegeben.
jeder_wie_vielte = ANZ_DEUTSCHLAND // anz_einwohner

# Ausgabe
print(f"Jede/r {jeder_wie_vielte}. Deutsche lebt in {wohnort}.")
