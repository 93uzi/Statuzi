#!/usr/bin/env python3

# BANNIÈRE
print("""
========================================
     TRIAGE D'URL PAR CODE DE STATUT
          Script par [93noushi]
========================================
""")

import sys

# Fonction pour lire le fichier et trier les URLs par code de statut
def trier_urls_par_statut(fichier):
    urls_par_statut = {}

    with open(fichier, 'r') as file:
        for ligne in file:
            ligne = ligne.strip()
            url, code_statut = ligne.split(' ')
            code_statut = code_statut.strip('[]')

            if code_statut not in urls_par_statut:
                urls_par_statut[code_statut] = []
            urls_par_statut[code_statut].append(url)

    return urls_par_statut

# Fonction pour écrire les résultats dans des fichiers séparés
def ecrire_resultats_dans_fichiers(urls_par_statut):
    for code_statut, urls in urls_par_statut.items():
        nom_fichier = f"status-{code_statut}.txt"
        with open(nom_fichier, 'w') as file:
            file.write(f"")
            for url in urls:
                file.write(f"{url}\n")
        print(f"Résultats pour le statut {code_statut} enregistrés dans {nom_fichier}")

if len(sys.argv) != 2:
    print("Usage: trier_urls <nom_du_fichier>")
    sys.exit(1)

fichier = sys.argv[1]
urls_triees = trier_urls_par_statut(fichier)
ecrire_resultats_dans_fichiers(urls_triees)
