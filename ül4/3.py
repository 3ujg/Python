# 16.10.24 Tammes
# Ülesanded 04


#3. Faili allalaadimine
try:
    failsuurus = int(input("Sistesta faili suurus (MB): "))
    downkiirus = int(input("Sisesta allalaadimis kiirus (MB/s): "))
    aeg = failsuurus / downkiirus
    print(f"Allalaadimiseks kulub {aeg:0.2f} sekundit")
except:
    print("Tegid sisestamisel vea!")