"""---------------------------------------------------------VERSION FRANCAISE---------------------------------------------------------------"""

#Programme de gestions de contact avec interface

#class pour organiser les informations d'un client en une variable
class Person:
    def __init__(self, fullname="", status="", age=0, phone="", mail="", gender=""):
        self.fullname = fullname
        self.status = status
        self.age = age
        self.phone = phone
        self.mail = mail

#Fonction pour recuperer les informations du client    
def infos_recup(a: Person):
    print("Nous allons recuperer vos informations personnelles.")
    a.fullname = input("\nEntrez votre nom complet (PrenomNOM): ")
    a.status = input("\nEntrez votre metier: ")
    a.age = int(input("\nEntrez votre age: "))
    a.phone = input("\nEntrez votre numero de telephone: ")
    a.mail = input("\nEntrez votre mail: ")

#Fonction pour lire dans un fichier
def read_info(file):
    if open(file, 'r') == FileExistsError:
        print("Le fichier n'existe pas")
    else:
        with open(file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                print(line)

#Fonction pour ecrire dans un fichier
def write_info(file, a: Person):
    with open(file, 'a') as f:
        f.write(f"Nom complet: {a.fullname}")
        f.write(f"\nMetier: {a.status}")
        f.write(f"\nAge: {a.age}")
        f.write(f"\nNumero de telephone: {a.phone}")
        f.write(f"\nMail: {a.mail}\n\n")

#Fonction principale
def main():
    nameFile = "saveInfos.txt"
    person = Person()
    #on définit la variable type qui sera utilisée pour stocker les infos de tous les clients dans le programme
    print("--> Bienvenue dans le gestionnaire de contacts <--\n\n")
    
    while True:
        print("Que voulez-vous faire ? (a/l/q)")
        print("\na. Ajouter une personne")
        print("l. Lire le fichier")
        print("q. Quitter")
        choice = input().lower()
        #input permet de récupérer la valeur de choice écrite par l'utilisateur, lower permet d'assurer que les lettres sont en minuscules
        
        if choice == 'a':
            infos_recup(person)
            write_info(nameFile, person)
        elif choice == 'l':
            read_info(nameFile)
        elif choice == 'q':
            break
        else:
            print("Choix invalide. Veuillez réessayer.")
    return 0

#Fonction primaire permettant d'executer le programme
if __name__ == "__main__":
    main()
    
"""---------------------------------------------------------ENGLISH VERSION---------------------------------------------------------------"""
""""
#Contact management program with interface

#Class to organize client information into a variable
class Person:
    def __init__(self, fullname="", status="", age=0, phone="", mail="", gender=""):
        self.fullname = fullname
        self.status = status
        self.age = age
        self.phone = phone
        self.mail = mail

#Function to collect client information    
def infos_recup(a: Person):
    print("We will collect your personal information.")
    a.fullname = input("\nEnter your full name (FirstNameLASTNAME): ")
    a.status = input("\nEnter your occupation: ")
    a.age = int(input("\nEnter your age: "))
    a.phone = input("\nEnter your phone number: ")
    a.mail = input("\nEnter your email: ")

#Function to read from a file
def read_info(file):
    if open(file, 'r') == FileExistsError:
        print("The file does not exist")
    else:
        with open(file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                print(line)

#Function to write to a file
def write_info(file, a: Person):
    with open(file, 'a') as f:
        f.write(f"Full name: {a.fullname}")
        f.write(f"\nOccupation: {a.status}")
        f.write(f"\nAge: {a.age}")
        f.write(f"\nPhone number: {a.phone}")
        f.write(f"\nEmail: {a.mail}\n\n")

#Main function
def main():
    nameFile = "saveInfos.txt"
    person = Person()
    #We define the variable type that will be used to store all client info in the program
    print("--> Welcome to the contact manager <--\n\n")
    
    while True:
        print("What would you like to do? (a/l/q)")
        print("\na. Add a person\n")
        print("l. Read the file")
        print("q. Quit")
        choice = input().lower()
        #input is used to get the value of choice entered by the user, lower ensures letters are lowercase
        
        if choice == 'a':
            infos_recup(person)
            write_info(nameFile, person)
        elif choice == 'l':
            read_info(nameFile)
        elif choice == 'q':
            break
        else:
            print("Invalid choice. Please try again.")
    return 0

#Primary function to run the program
if __name__ == "__main__":
    main()"""
