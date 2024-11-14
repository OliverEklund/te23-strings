
from random import randint
inventory = []

name = input("Hej, vad är ditt namn?: ")

print("du vaknar upp efter en lång natts sömn......")
print("Mystiskt nog finner du dig i en marsvins kropp finner du dig i en sorks kropp, då du springer runt på en äng, du ser ett torn i horizonten, allt du vet är att du måste dit.")
print("Du stannar till när du ser en magisk [bok], tittar du på boken eller din magiska-[marsvin]-form")

choice = input("Vad väljer du?: ")
available_choices = ["bok", "sork"]
if "sork" in choice:
    print("I drömlik slowmotion så ser du en full 360 video av marsvin, ganska söt")
elif "bok" in choice:
    print("Du plockar upp den magiska boken. Sedan stoppar du den i din magiska ficka")
    inventory.append("Magisk bok")
else:
    print("Du skrev fel, du ba fortsätter med ditt sork liv.")

print("Om du har föremål i dit inventory kan du öppna det när du ska välja något genom att skriva [i].")
print("Du fortsätter över åkern, sedan kommer du till en väg med mycket trafick")

Puzzle_status = True


while Puzzle_status == True:
    print("/")
    print("Hur ska du ta dig över vägen? Gå eller vänta tills traficken är borta?")
    choice = input("Vad blir det?: ")
    available_choices = ["gå", "vänta", "inventory"]
    
    if "gå" in choice:
        chance = randint (1,6)
        if chance <6:
            print("Du springer över vägen. Du klarar dig en bit men blir påkörd.")
            print("Som tur så drar en mystisk kraft dig tillbaka till där du började, bättre lycka nästa gång!")
        if chance ==6:
            print("Du knappast klarar dig över vägen.")
            Puzzle_status == False
            break
    
    if "vänta" in choice:
        print("Du väntar på att traficken ska lungna sig, den gör det inte.")

    if "i" in choice:
        print("Du kollar din magiska ficka, det finns:")
        for item in inventory:
            print(item)
        print("Vill du gå [ut]? Om du vill att använda ett föremål skriv bara föremålets namn.")
        inventory_choice = input("")

        if inventory_choice == "ut":
            print("Du slutar att kolla i fickan")
        
        if "Magisk bok" in inventory and inventory_choice == "Magisk bok":
            print("Du använder bokens magi för att teleportera dig över till andra sidan vägen")
            Puzzle_status == False
            break

print("/")
print("DU HAR TAGIT DIG ÖVER VÄGEN! nu kan ditt äventyr äntligen fortsätta mot det där tornet!")
print("Du springer över fina ängar och igenom stora skogar. plöstligt så kommer du till.")