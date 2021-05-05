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
    try:
        eingabe = input("Geben Sie einen Begriff ein den Sie übersetzen wollen: ")
        print(woerterbuch_deutsch[eingabe],"[ENG]")
        break
             
    except KeyError:
        try:
            print(woerterbuch_englisch[eingabe],"[DE]")
            break
        
        except KeyError:
            print("Wort nicht gefunden! Versuchen Sie es nochmal")
       



         

