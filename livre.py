#gestion simple d'une bibliotheque
titre=input("Titre du livre :")
exemplaires=int(input("Nombre d'exemplaires:"))

print("Livre :" ,titre)
print("Exemplaires disponibles :",exemplaires)

#emprunt d'un livre
exemplaires=exemplaires-1
print("Apres emprunt :",exemplaires,"exemplaire(s) disponible(s)")