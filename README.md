# Projet E-commerce — Application Web Django

Application web Django permettant d'analyser automatiquement
un fichier de ventes CSV et de visualiser les résultats.

---

## 1. Titre & Description
Ce projet est une application web développée avec **Django**.
L'utilisateur uploade un fichier `ventes.csv`, et l'application :
- Calcule automatiquement le CA Brut, CA Net et la TVA
- Affiche un tableau complet des résultats
- Génère des graphiques avec Matplotlib
- Identifie le produit avec le plus gros bénéfice
- Affiche le CA Total de l'entreprise

---

## 2. Prérequis
- Python 3.x

---

## 3. Installation
```bash
# Cloner le projet
git clone https://github.com/Khalildotcom/Projet_E-commerce_DJANGO.git
cd Projet_E-commerce_DJANGO/automatisation

# Créer l'environnement virtuel
python -m venv venv

# Activer l'environnement virtuel
# Windows :
venv\Scripts\activate
# Mac/Linux :
source venv/bin/activate

# Installer les dépendances
pip install -r requirements.txt

```

---

## 4. Utilisation
```bash
# Appliquer les migrations (crée la base de données interne de Django)
python manage.py migrate

# Lancer le serveur
python manage.py runserver
```
Ouvrir dans le navigateur : http://127.0.0.1:8000/

Uploader un fichier `ventes.csv` avec ce format :

ID,Prix,Quantite,Remise

1,150.50,3,10

2,200.00,2,5

---

## 5. Auteurs
- Eya Ben Rebah
- Ahmed Fourat Laajimi
- Adem Aroud
- Khalil Mohamed Chihaoui

**Encadrante : Imene Amira**
