import tkinter as tk
from tkinter import messagebox
import random

def repartir_groupes():
    noms = entree_noms.get("1.0", tk.END).strip().split("\n")
    try:
        if option_var.get() == "groupes":
            nombre_groupes = int(entree_groupes.get())
            if nombre_groupes <= 0:
                raise ValueError("Le nombre de groupes doit être supérieur à 0.")
        else:
            nombres_par_groupe = int(entree_groupes.get())
            if nombres_par_groupe <= 0:
                raise ValueError("Le nombre de personnes par groupe doit être supérieur à 0.")
            nombre_groupes = (len(noms) + nombres_par_groupe - 1) // nombres_par_groupe
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer un nombre valide.")
        return

    if not noms or noms == [""]:
        messagebox.showerror("Erreur", "Veuillez entrer au moins un nom.")
        return

    random.shuffle(noms)
    groupes = [[] for _ in range(nombre_groupes)]
    for i, nom in enumerate(noms):
        groupes[i % nombre_groupes].append(nom)

    resultat = ""
    for i, groupe in enumerate(groupes, start=1):
        resultat += f"Groupe {i} : {', '.join(groupe) if groupe else 'Vide'}\n"

    text_resultat.delete("1.0", tk.END)
    text_resultat.insert(tk.END, resultat)

# Fenêtre principale
fenetre = tk.Tk()
fenetre.title("Répartition aléatoire en groupes")
fenetre.attributes('-fullscreen', True)  # Plein écran
fenetre.configure(bg="white")

# Styles
style_bouton = {"bg": "blue", "fg": "white", "font": ("Arial", 16, "bold")}
style_label = {"bg": "white", "fg": "black", "font": ("Arial", 16)}

# Widgets
label_noms = tk.Label(fenetre, text="Entrez les noms (un par ligne) :", **style_label)
label_noms.pack(pady=10)

entree_noms = tk.Text(fenetre, height=15, width=70, bd=2, relief="groove", font=("Arial", 14))
entree_noms.pack(pady=10)

option_var = tk.StringVar(value="groupes")
frame_options = tk.Frame(fenetre, bg="white")
frame_options.pack(pady=10)

rb_groupes = tk.Radiobutton(frame_options, text="Nombre de groupes", variable=option_var, value="groupes",
                            bg="white", fg="black", font=("Arial", 14), anchor="w")
rb_groupes.pack(side="left", padx=20)
rb_personnes = tk.Radiobutton(frame_options, text="Nombre de personnes par groupe", variable=option_var, value="personnes",
                               bg="white", fg="black", font=("Arial", 14), anchor="w")
rb_personnes.pack(side="left", padx=20)

label_groupes = tk.Label(fenetre, text="Valeur :", **style_label)
label_groupes.pack(pady=10)

entree_groupes = tk.Entry(fenetre, width=20, bd=2, relief="groove", font=("Arial", 14))
entree_groupes.pack(pady=10)

bouton_repartir = tk.Button(fenetre, text="Répartir", command=repartir_groupes, **style_bouton)
bouton_repartir.pack(pady=20)

text_resultat = tk.Text(fenetre, height=15, width=70, bd=2, relief="groove", font=("Arial", 14), bg="#f5f5f5")
text_resultat.pack(pady=20)

bouton_quitter = tk.Button(fenetre, text="Quitter", command=fenetre.destroy, **style_bouton)
bouton_quitter.pack(pady=10)

fenetre.mainloop()
