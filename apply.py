#formulaire et ate de naissance
name = input("Quel est votre nom ? ")
date = input("Quelle est votre annee de naissance ? ")
age = 2023 - int(date)
sport_favorit = input("Quel est votre sport favorit? ")
montant_rouble = input("montant en rouble ")
dollar = 1*int(montant_rouble)/73.41
print("Bonjour " + name, "vous avez", age, "ans, vous aimer le", sport_favorit,"et vous avez", (montant_rouble), "roubles","ce qui vaut", dollar,"$")
print("maintenat nous faisons les choses bien a", int(age), "ans")