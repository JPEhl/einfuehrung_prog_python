# Eingabe von Name und Geburtsjahr und Speicherung in Variablen
name = input("Wie heißt du?")
geburtsjahr = int(input("In welchem Jahr bist du geboren?"))

# Berechnung des ungefähren Alters (je nach Geburtsdatum ungenau)
alter = 2023 - geburtsjahr

# Ausgabe
print(f"Hallo {name}. Du bist um die {alter} Jahre alt.")
