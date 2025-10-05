# Act 20 :
adresses_ip = ["192.168.0.1", "10.0.0.1", "172.16.0.1", "200.100.50.1", "169.254.0.1"]

# Qst 1 :
print(f"1. La première adresse dans la liste est : {adresses_ip[0]}")

# Qst 2 :
print(f"2. La dernière adresse dans la liste est : {adresses_ip[-1]}")

# Qst 3 :
print(f"3. La troisième adresse dans la liste est : {adresses_ip[2]}")

# Qst 4 :
adresses_ip.append("172.31.0.1")

# Qst 5 :
adresses_ip.pop(3)

# Qst 6 :
print(f"6. Il reste {len(adresses_ip)} adresses dans la liste après modification,", end=" "); print(f"avec : adresses_ip = {adresses_ip}")

# Qst 7 :
verification = "192.168.0.1" in adresses_ip
if verification == True :
    print(f"7. Oui, l'adresse \"192.168.0.1\" est dans la liste.")
else :
    print(f"7. Non, Cette adresse n'est pas présente dans la liste.")

# Liste -> Dictionnaire
adresses_ip = {
    "192.168.0.1" : "Classe C",
    "10.0.0.1" : "Classe A",
    "172.16.0.1" : "Classe B",
    "169.254.0.1" : "APIPA",
    "172.31.0.1" : "Classe B"
}

# Qst 8 : 
print(f"8. La classe de l'adresse IP de \"10.0.0.1\" est : {adresses_ip['10.0.0.1']}")

# Qst 9 :
adresses_triees = sorted(adresses_ip)
print(f"9. La liste triée par ordre croissant est : {adresses_triees}")

# Qst 10 :
if all(value == "Classe C" for value in adresses_ip.values()) :
    print("10. Toutes les adresses sont de classe C.")
else:
    print("10. Non, toutes les adresses ne sont pas de classe C.")


# Qst 11 :
publiques = []

for key, value in adresses_ip.items() :
    if "Publique" in value :
        publiques.append(key)

print(f"11. Il y a {len(publiques)} adresse(s) IP publique(s).")

# Nom Complet : WAEL BOUHAYA
# Filière : IAGI-1 
