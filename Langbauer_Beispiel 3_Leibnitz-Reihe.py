# Benutzer gibt eine Anzahl der gewünschten Interationen an
Interation = int (input("Geben Sie die gewünschte Anzahl der Interationen ein (1-\u221E): "))

#Abfrage ob die Zwischenergebnisse angezeigt werden sollen
Zwischenergebnisse = str (input("Wollen Sie die Zwischenergebnisse angezeigt bekommen?(yes/no):"))

if Zwischenergebnisse == "yes":
    print("Zwischenergebnisse")
elif Zwischenergebnisse == "no":
    print("")
else:
    print("Falsche Eingabe. Aber Sie bekommem trotzdem ein Ergebnis für die Annäherung an Pi :)")
    
# Leibnitz-Reihe mit while Schleife
Ergebnis = 4
k = 1
while k < Interation:
    Ergebnis += (((-1)**k)/(2*k+1))*4
    if Zwischenergebnisse == "yes":
        print(round(Ergebnis,4),"k=",k)
    k += 1

# Ausgabe des Wertes mit Anzahl der Interationen grammatikalisch angepasst
if Interation == 1:
    print("Der Näherungswert für Pi mit einer Interation beträgt:",round(Ergebnis,10))
else:
    print("Der Näherungswert für Pi mit",Interation,"Interationen beträgt:",round(Ergebnis,10)) 





print("--------------------------------------------------------") # Absatz
#Differenz zum Originalwert
import math
x= math.pi

if x>=Ergebnis:
    Differenz = ((x-Ergebnis)/Ergebnis)*100
else:
    Differenz = ((Ergebnis-x)/x)*100

print("Die Differenz zum Originalwert beträgt:",round(Differenz,4),"%")
if Differenz < 0.1:
    print("Also schon echt nah dran!")
elif Differenz > 2:
    print("Das ist schon noch ein ganzes Stück weit weg!")

