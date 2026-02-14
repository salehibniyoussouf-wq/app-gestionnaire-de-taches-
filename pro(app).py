import tkinter as tk
import json


# fenetre principale
root = tk.Tk()
root.title("Gestionnaire de tâches")
root.geometry("500x500")
liste_taches = tk.Listbox(root)
liste_taches.pack()


taches = []

# Entry
entrer_taches = tk.Entry(root)
entrer_taches.pack()


def marquer_taches(event):
    print("Un clic detecté")
    if not event.widget.curselection():
        return
    index = event.widget.curselection()[0]
    taches[index]["fait"]= not taches[index]["fait"]
    mettre_a_jour_liste()
    sauvegarder_taches()
    print("index:", index)
    print("texte:", taches[index])

liste_taches.bind("<Double-Button-1>", marquer_taches)


def mettre_a_jour_liste():
    liste_taches.delete(0, tk.END)
    for texte in taches:
        symbole = "✔" if texte["fait"] else "✘"
        liste_taches.insert(tk.END, f'{texte["nom"]} {symbole}')


def ajouter_taches():
    nom_tache = entrer_taches.get().strip()# la tache entrer
    if nom_tache != "" :
        texte= {"nom": nom_tache, "fait": False}
        taches.append(texte) # ajouter dans la liste
        mettre_a_jour_liste()
        sauvegarder_taches()
        entrer_taches.delete(0, tk.END)


def sauvegarder_taches():
    with open("taches.json", "w") as fichier:
        json.dump(taches, fichier, indent=4)



def charger_taches():
    global taches
    try:
        with open("taches.json", "r") as fichier:
            taches = json.load(fichier)
    except FileNotFoundError:
        taches = []
    mettre_a_jour_liste()




def supprimer_taches():
    selection= liste_taches.curselection()
    if not selection:
        print("Aucune tache selectionné")
        return
    index = selection[0]
    taches.pop(index)
    mettre_a_jour_liste()
    sauvegarder_taches()


# Bouton ajouter
tk.Button(root, text="Ajouter", command=ajouter_taches).pack()
tk.Button(root, text="Supprimer", command=supprimer_taches).pack()

charger_taches()
root.mainloop()





