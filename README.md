# Statuzi

## Trier les URLs par Code de Statut HTTP
Ce projet contient un script Python qui trie des URLs par leur code de statut HTTP et enregistre les résultats dans des fichiers distincts. 
C'est un outil simple mais efficace pour organiser les URLs selon leur statut de réponse, ce qui peut être utile pour l'analyse, le débogage ou la gestion de grands ensembles d'URLs.
J'ai ecris ce script pour trier la sortie de httpx.

### Fonctionnalités
Tri par code de statut HTTP : Le script lit un fichier contenant des URLs et leurs codes de statut, puis les trie selon le code de statut.
Enregistrement dans des fichiers distincts : Les URLs triées sont enregistrées dans des fichiers séparés, nommés en fonction du code de statut (par exemple, status-200.txt, status-404.txt).
Utilisation simple en ligne de commande : Le script peut être exécuté comme une commande en fournissant simplement le fichier d'URLs à traiter.
Prérequis
Python 3.x : Assurez-vous que Python 3 est installé sur votre machine. Vous pouvez vérifier cela en exécutant python3 --version dans votre terminal.
### ***Installation***
```
Clonez le dépôt
git clone https://github.com/93uzi/Statuzi.git
cd statuzi

Rendez le script exécutable (si nécessaire) :
chmod +x statuzi.py

Déplacez le script dans un répertoire inclus dans votre PATH (optionnel) :
sudo mv statuzi.py /usr/local/bin/statuzi
```

### Utilisation
supposons cette liste :
```
https://secure.netflix.com [200]
https://nintendo.nccp.us-west-2.prodaa.netflix.com [403]
https://push.prod.eu-west-1.netflix.com [404]
```

Exécutez le script en fournissant le fichier d'URLs en argument :

statuzi subdomainstatus.txt
Le script lira le fichier, triera les URLs par code de statut et enregistrera les résultats dans des fichiers séparés (par exemple, status-200.txt, status-403.txt, etc.).
