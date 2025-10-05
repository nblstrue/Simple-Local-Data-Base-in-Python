Voici un **README complet bilingue (anglais/français)** pour ton projet de gestion de contacts, prêt à être utilisé sur GitHub :

---

# 📇 Contact Manager / Gestionnaire de Contacts

A simple console-based contact manager in Python. This program allows users to enter and store contact information (name, job, age, phone, email) in a text file and read it back later.

Un gestionnaire de contacts simple en ligne de commande écrit en Python. Ce programme permet à l'utilisateur d'ajouter et sauvegarder des informations personnelles (nom, métier, âge, téléphone, email) dans un fichier texte, puis de les lire.

---

## 📁 Features / Fonctionnalités

* Add a new contact
* Save contact info to a text file
* Read all saved contacts
* Simple and lightweight CLI interface

---

## 🧠 How it works / Comment ça fonctionne

### 1. `class Person`

**EN:** A class to represent a contact with attributes: fullname, status (job), age, phone number, and email.
**FR:** Une classe qui représente un contact avec les attributs : nom complet, métier, âge, numéro de téléphone et email.

---

### 2. `infos_recup(a: Person)`

**EN:** Prompts the user to input their personal information and assigns it to the given `Person` object.
**FR:** Demande à l'utilisateur de saisir ses informations personnelles et les stocke dans l'objet `Person` donné.

---

### 3. `read_info(file)`

**EN:** Reads all the lines from the specified file and prints each contact.
**FR:** Lit toutes les lignes du fichier spécifié et affiche chaque contact.

---

### 4. `write_info(file, a: Person)`

**EN:** Appends the contact details of a `Person` object to the specified file.
**FR:** Ajoute les informations d’un objet `Person` à la fin du fichier spécifié.

---

### 5. `main()`

**EN:** The main function that controls the program flow. It displays the menu and responds to user input (`a` to add, `l` to read, `q` to quit).
**FR:** La fonction principale qui contrôle l’exécution du programme. Elle affiche le menu et répond aux choix de l'utilisateur (`a` pour ajouter, `l` pour lire, `q` pour quitter).

---

## 📝 File Used / Fichier utilisé

* `saveInfos.txt`: Stores all contact information entered by the user.
* `saveInfos.txt` : Contient toutes les informations des contacts ajoutés par l'utilisateur.

---

## ▶️ How to Run / Comment exécuter

```bash
python3 test1.py
```

---

## ✅ Requirements / Pré-requis

* Python 3.x
  (No external libraries needed / Pas de bibliothèques externes nécessaires)

---

## ✨ Example / Exemple

```txt
--> Welcome to the contact manager <--

What would you like to do? (a/l/q)
a. Add a person
l. Read the file
q. Quit
```

## 📃 License

MIT License (or specify your own)
