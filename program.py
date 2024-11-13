
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
    print("Du skriker i smärta i respons av den rena antallet ohelig info du tar upp i hjärnan. Sedan så plockar du upp boken och stoppar den i din magiska ficka")
    inventory.append("Magisk bok")
else:
    print("Du skrev fel, du ba fortsätter med ditt sork liv.")

print("Om du har föremål i dit inventory kan du öppna det när du ska välja något.")
print("Du fortsätter över åkern, sedan kommer du till en väg med mycket trafick")

Puzzle_status = True
while Puzzle_status == True:
    print("Hur ska du ta dig över vägen? Gå eller vänta tills traficken är borta?")
    choice = input("Vad blir det?: ")
    available_choices = ["gå", "vänta", "inventory"]
    
    if "gå" in choice:
        print("Du springer över vägen. Du klarar dig en bit men blir påkörd.")
        print("Som tur så drar en mystisk kraft dig tillbaka till där du började.")
    
    if "vänta" in choice:
        print("Du väntar på att traficken ska lungna sig, den gör det inte.")

    if "inventory" in choice:
        print("Du kollar din magiska ficka, det finns:")
        for item in inventory:
            print(item)