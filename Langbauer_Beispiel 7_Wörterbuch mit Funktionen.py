#Beispiel 7 mit Funktionen
woertebuch_deutsch = ["Apfel", "Birne", "Kirsche", "Melone", "Marille", "Pfirsich"]
woertebuch_englisch = ["apple", "pear", "cerry", "melon", "apricot", "peach"]

#Funktionen
def Wort_hinzufügen(Deutscher_Begriff, Englischer_Begriff):   
    woertebuch_deutsch.append(Deutscher_Begriff)
    woertebuch_englisch.append(Englischer_Begriff)
    print("Der Begriff wurde hinzugefügt")
        
def Wort_löschen():
    gelöschter_Begriff = input ("Welchen Begriff möchten Sie Löschen?: ")
    K = 0
    while K < len(woertebuch_deutsch):
        if gelöschter_Begriff == woertebuch_deutsch[K]:
            woertebuch_englisch.remove(woertebuch_englisch[K])          
            woertebuch_deutsch.remove(gelöschter_Begriff)
            print("Der Begriff wurde gelöscht")
            break
            
        if gelöschter_Begriff.lower() == woertebuch_englisch[K]:
            woertebuch_deutsch.remove(woertebuch_deutsch[K])
            woertebuch_englisch.remove(gelöschter_Begriff)
            print("Der Begriff wurde gelöscht")
            break
            #print(K)
        K += 1
            
        if K == len(woertebuch_deutsch):
            print("nicht gefunden!")
def Wort_abfragen(Begriff):
    
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
            
def Eingabe():
    while True:
        Abfrage = input("Befehl? [E]infügen, [L]öschen, [A]bfragen, [B]eenden: ")
        if Abfrage.lower() == "e" or  Abfrage.lower() =="l" or Abfrage.lower() =="a" or Abfrage.lower() =="q":
            return Abfrage.lower()
        else:
            print("Versuche es nochmal!")
    
    
while True:
    Abfrage = Eingabe()
    if Abfrage == "e":
        Deutscher_Begriff = input ("Neuer Deutscher Begriff:")
        Englischer_Begriff = input ("Übersetzung ins Englische:")
        Wort_hinzufügen(Deutscher_Begriff, Englischer_Begriff)
        
    elif Abfrage == "a":
        Begriff = input("Geben Sie einen Begriff ein den Sie übersetzen wollen: ")
        Wort_abfragen(Begriff)
    elif Abfrage == "l":
        Wort_löschen()
    elif Abfrage == "b":
        break 
            
            
            
            