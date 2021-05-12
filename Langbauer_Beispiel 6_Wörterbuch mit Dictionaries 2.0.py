woerterbuch_deutsch = {"Apfel": "apple",
                       "Birne": "pear",
                       "Kirsche": "cherry",
                       "Melone": "melon",
                       "Marille": "apricot",
                       "Pfirsich": "peach",
                       }

woerterbuch_englisch = {"apple":"Apfel",
                       "pear": "Birne",
                       "cherry":"Kirsche",
                       "melon":"Melone",
                       "apricot":"Marille",
                       "peach": "Pfirsich",
                       }
while True:
    eingabe = input("[E]infügen, [A]bfragen,[L]öschen, [W]örterbuch abfragen, [B]eenden: ")
    while True:
        try:           
            #Abfragen
            if eingabe == "A" or eingabe == "a":
                Wort = input("Welches Wort wollen Sie übersetzten?([z]urück): ")
                if Wort =="z" or Wort == "Z":
                    break
                else:
                    print(woerterbuch_deutsch[Wort],"[ENG]")
                    break
                
            #Einfügen
            elif eingabe == "E" or eingabe == "e":
                deutsches_Wort = input("Neues Deutschen Wort[([z]urück)]: ")
                if deutsches_Wort == "z" or deutsches_Wort == "Z":
                    break
                else:
                    englisches_Wort = input("Neues Englisches Wort: ")
                    woerterbuch_deutsch[deutsches_Wort] = englisches_Wort
                    woerterbuch_englisch[englisches_Wort] = deutsches_Wort
                    print("Wort wurde hinzugefügt!")
                    break
            
            
            #Löschen
            elif eingabe =="L" or eingabe == "l":
                try:
                    löschen = input("Welchen Begriff wollen Sie löschen?([z]urück): ")
                    if löschen == "Z" or löschen == "z":
                        break
                    else:                        
                        woerterbuch_englisch.pop(woerterbuch_deutsch[löschen])
                        woerterbuch_deutsch.pop(löschen)
                        print("Wort wurde entfernt")
                        break
             
                except KeyError:
                    try:                      
                        woerterbuch_deutsch.pop(woerterbuch_englisch[löschen])                        
                        woerterbuch_englisch.pop(löschen)                   
                        print("Wort wurde entfernt")
                        break
        
                    except NameError:
                        print("Wort nicht gefunden! Versuchen Sie es nochmal")                      
        #Beenden
            elif eingabe == "B" or eingabe == "b":
                exit()
                
            elif eingabe == "W" or eingabe == "w":
                print(woerterbuch_deutsch)
                break
            else:
                print("Fehlerhafte Eingabe")
                break
        except KeyError:
            try:
                print(woerterbuch_englisch[Wort],"[DE]")
                break
        
            except KeyError:
                print("Wort nicht gefunden! Versuchen Sie es nochmal")
                
       


