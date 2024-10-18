# 16.10.24 Tammes
# Ülesanded 04


# 4. Kingituste pakkimine
try:
    kingitused = int(input("Lisade kinkide arv: "))
    maht = 5
    pakid = kingitused // maht
    yle = kingitused % maht
    print(f"Saad teha {pakid} täis kinkekasti. Üle jääb {yle} kingitust.")
except:
    print("Tegid sisetamisel vea!")