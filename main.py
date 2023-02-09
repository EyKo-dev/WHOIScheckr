import whois

v = input("Renseignez le nom de domaine à analyser :\n")
w = whois.whois(v)
print(w)

with open("Whois.txt", "w+") as file:
    file.write("Nom de domaine : " + v + "\n" + "\n")
    file.write(str(w))
    file.close()