# Aufgabe 1
# Schreiben Sie ein Phyton-Programm, das
#1) Benutzer begrüßt
#2) 1. Zahl entgeben nimmt
#3) 2. Zahl entgeben nimmt
#4) Summe ausgibt
#5) Differez der kleineren von der größeren berechnen
#6) Produkt ausgibt
#7) Quotient kleinere durch größere zahl(inkl. Nachklommerstellen) ausgibt


# Begrüßung
print("Hallo!")

# Eingabe der Zahlen 1 und 2
zahl1 = float (input("Eingabe Ihrer ersten Zahl: "))
zahl2 = float (input("Eingabe Ihrer zweiten Zahl: "))

# Berechnungen und Ausgabe

#Summe
print("Summe: ", zahl1+zahl2)

# Differenz
if zahl1>=zahl2:
 print("Differenz: ",zahl1-zahl2)
else:
 print("Differenz: ",zahl2-zahl1)
 
#Produkt
print("Produkt: ", zahl1*zahl2)

#Quotient
if zahl1>=zahl2:
 print("Quotient: ",zahl2/zahl1)
else:
 print("Quotient: ",zahl1/zahl2)


