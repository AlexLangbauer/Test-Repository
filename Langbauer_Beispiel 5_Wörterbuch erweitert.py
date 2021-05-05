#Erweitern Sie das Wörterbuch-Beispiel um die Möglichkeit, Einträge zu ergänzen bzw. zu löschen


woertebuch_deutsch = ["Apfel", "Birne", "Kirsche", "Melone", "Marille","Pfirsich"]
woertebuch_englisch = ["apple", "pear", "cherry", "melon", "apricot","peach"]

Abfrage = input ("Befehl? [E]infügen, [L]öschen, [A]bfragen: ")


    #Einfügen
if Abfrage == "E" or Abfrage == "e":
    Deutscher_Begriff = input ("Neuer Deutscher Begriff:")
    woertebuch_deutsch.append(Deutscher_Begriff)
    Englischer_Begriff = input ("Übersetzung ins Englische:")
    woertebuch_englisch.append(Englischer_Begriff)
    print(woertebuch_deutsch)
    print(woertebuch_englisch)
    
    #Löschen
elif Abfrage == "L" or Abfrage == "l":
    print(woertebuch_deutsch)
    print(woertebuch_englisch)
    gelöschter_Begriff = input ("Welchen?: ")
    K = 0
    while K < len(woertebuch_deutsch):
        if gelöschter_Begriff == woertebuch_deutsch[K]:
            woertebuch_englisch.remove(woertebuch_englisch[K])
            #print(woertebuch_englisch[K])
            woertebuch_deutsch.remove(gelöschter_Begriff)
            break
        if gelöschter_Begriff == woertebuch_englisch[K]:
            woertebuch_deutsch.remove(woertebuch_deutsch[K])
            woertebuch_englisch.remove(gelöschter_Begriff)
            #print(woertebuch_englisch[K])
            break
        
        K += 1
   # woertebuch_deutsch.remove(gelöschter_Begriff)
    
    print(woertebuch_deutsch)
    print(woertebuch_englisch)
    
#print("neue Listen:")
#print(woertebuch_deutsch)
#print(woertebuch_englisch)
    
    #Abfrage
elif Abfrage != "A" or Abfrage != "a":
    Begriff = input("Geben Sie einen Begriff ein den Sie übersetzen wollen: ")
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
    exit()
    
else:
    print("Fehlerhafte Eingabe")
    
Nachfrage = input("Wollen Sie noch einen Begriff übersetzen?[yes],[no]: ")

if Nachfrage == "yes":
    
    Begriff = input("Geben Sie einen Begriff ein den Sie übersetzen wollen: ")
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
elif Nachfrage == "no":
    print("Ok! Schönen Tag noch")
    
else:
    print("Fehlerhafte Eingabe")
        

    