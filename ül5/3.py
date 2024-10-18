# 18.10.24 Tammes
# Ülesanne 5
import random

# 3. Matemaatika test (randint)
a, b = random.randint(1,10), random.randint(1,10)
vastus = int(input(f"Lisa vastus {a}*{b}="))
if vastus == a*b:
    print("Ma lollim kui sina!")
else:
    print("Kui taun sa olla saad?")