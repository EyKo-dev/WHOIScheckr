import whois
from past.builtins import raw_input

v = raw_input("Renseignez le nom de domaine à analyser :\n")  #Demande à l'utilisateur d'insérer le nom de domaine

w = whois.whois(v)
print(w)

with open("Whois.txt", "w+") as file:
    file.write("Nom de domaine : " + v + "\n" + "\n")
    file.write(str(w))
    file.close()