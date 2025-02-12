# Backup Script

Ce projet permet de créer une sauvegarde de ton répertoire personnel dans une archive ZIP. Le script est compatible avec **Windows**, **macOS** et **Linux**.

## Fonctionnalités

- **Création d'une archive ZIP** du répertoire personnel de l'utilisateur.
- La sauvegarde est placée dans le dossier `backup_zip` à la racine du projet.
- Compatible avec **Windows**, **macOS** (Darwin) et **Linux**.

## Prérequis

Avant de pouvoir utiliser ce script, assurez-vous d'avoir Python installé sur votre machine.

1. **Python 3.10+** : Vous pouvez télécharger Python depuis le site officiel [ici](https://www.python.org/downloads/).

2. **Installer les dépendances** :
    - Ouvrez un terminal ou une invite de commande.
    - Créez votre environnement virtuel : ***python3 -m venv venv***
    - Activez le : ***source venv/bin/activate*** sous Linux et sous Windows : ***venv\Scripts\activate***
    - Si vous n'avez pas encore installé les dépendances, vous pouvez les installer avec `pip` :
    ```bash
    pip install -r requirements.txt
    ```

## Installation et Utilisation

### 1. Cloner le projet
Clonez ce dépôt sur votre machine locale.

```bash
git clone https://github.com/Developpeur-Mehdi/create_archive.git
cd create_backup
