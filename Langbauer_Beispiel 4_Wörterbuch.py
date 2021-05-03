#Ändern bzw. erweitern Sie das Wörterbuch Beispiel aus der LÜ vom 03.05,
#dass Sie Wahlweise englisch oder deutsch Begriff eingeben könenn und das Programm
#selbstständig das jeweils korrespondierende Vokabel findet und,
#versehen mit einem Hinweis auf dieSprache, ausgibt


woertebuch_deutsch = ["Apfel", "Birne", "Kirsche", "Melone", "Marille","Pfirsich"]
woertebuch_englisch = ["apple", "pear", "cherry", "melon", "apricot","peach"]

Begriff = input("Geben Sie einen Begriff ein: ")

Index = 0
while Index < len(woertebuch_deutsch):
    if Begriff.lower() == woertebuch_deutsch[Index].lower():
        print("Übersetzung vom Deutschen ins Englische:",woertebuch_englisch[Index])
        break
    if Begriff.lower() == woertebuch_englisch[Index].lower():
        print("Übersetzung vom Englischen ins Deutsche: ",woertebuch_deutsch[Index])
        break
    #print(Index, woertebuch_deutsch[Index], Begriff)
    Index += 1      
if Index == len(woertebuch_deutsch):
        print("nicht gefunden")