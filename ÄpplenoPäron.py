
def input_int(text):
    while True:
        try:
            return int(input(text))
        except:
            print("Felaktig inmatning, skriv ett heltal.")

print("Äpplen kostar 7kr")
print("Päron kostar 13kr")
Äpplen_antal = input("Hur många äpplen vill du köpa?:")
Päron_antal = input("Hur många Päron vill du köpa?:")

Ä = int(Äpplen_antal)
P = int(Päron_antal)

Äpplen_kostnad = 7 * (Ä)
Päron_kostnad = 7 * (P)

print(f"Du spenderade {Äpplen_kostnad}kr på Äpplen")
print(f"Du spenderade {Päron_kostnad}kr på Päron")