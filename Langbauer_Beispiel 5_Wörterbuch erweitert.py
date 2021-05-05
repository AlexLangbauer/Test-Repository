#Erweitern Sie das Wörterbuch-Beispiel um die Möglichkeit, Einträge zu ergänzen bzw. zu löschen


woertebuch_deutsch = ["Apfel", "Birne", "Kirsche", "Melone", "Marille","Pfirsich"]
woertebuch_englisch = ["apple", "pear", "cherry", "melon", "apricot","peach"]

while True:
    print("")# Absatz
    Abfrage = input ("Befehl? [E]infügen, [L]öschen, [A]bfragen, [W]örterbuch Anzeigen, [B]eenden: ")


    #Einfügen
    if Abfrage == "E" or Abfrage == "e":
        Deutscher_Begriff = input ("Neuer Deutscher Begriff:")
        woertebuch_deutsch.append(Deutscher_Begriff)
        Englischer_Begriff = input ("Übersetzung ins Englische:")
        woertebuch_englisch.append(Englischer_Begriff)
        
    
    #Löschen
    elif Abfrage == "L" or Abfrage == "l":
        
        gelöschter_Begriff = input ("Welchen Begriff möchten Sie Löschen?: ")
        K = 0
        while K < len(woertebuch_deutsch):
            if gelöschter_Begriff == woertebuch_deutsch[K]:
                woertebuch_englisch.remove(woertebuch_englisch[K])          
                woertebuch_deutsch.remove(gelöschter_Begriff)
                break
            
            if gelöschter_Begriff.lower() == woertebuch_englisch[K]:
                woertebuch_deutsch.remove(woertebuch_deutsch[K])
                woertebuch_englisch.remove(gelöschter_Begriff)
                break
            #print(K)
            K += 1
            
        if K == len(woertebuch_deutsch) + 1:
            print("nicht gefunden!")
    #Abfrage
    elif Abfrage == "A" or Abfrage == "a":
        Begriff = input("Geben Sie einen Begriff ein den Sie übersetzen wollen: ")
        Index = 0
        while Index < len(woertebuch_deutsch):
            if Begriff.lower() == woertebuch_deutsch[Index].lower():
                print("Übersetzung vom Deutschen ins Englische:",woertebuch_englisch[Index])
                break
            if Begriff.lower() == woertebuch_englisch[Index].lower():
                print("Übersetzung vom Englischen ins Deutsche: ",woertebuch_deutsch[Index])
                break
            Index += 1      
        if Index == len(woertebuch_deutsch):
            print("nicht gefunden")
        
    elif Abfrage == "W" or Abfrage == "w":
        print("Wörterbücher:")
        print(woertebuch_deutsch)
        print(woertebuch_englisch)
    
    
    elif Abfrage == "B" or Abfrage == "b":
        print("Auf Wiedersehen!")
        exit()
    
    else:
        print("Fehlerhafte Eingabe")
    
   

    
        
