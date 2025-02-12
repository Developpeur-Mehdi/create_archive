import os
import shutil
import platform
from datetime import datetime

def get_home_directory():
    """Récupère le chemin du répertoire personnel de l'utilisateur."""
    return os.path.expanduser("~")

def get_backup_filename():
    """Génère un nom de fichier pour la sauvegarde."""
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    return f"backup_{timestamp}.zip"

def create_backup(home_dir, backup_name):
    """Crée une archive ZIP du répertoire personnel dans le dossier 'backup_zip' à la racine du projet."""
    # Aller dans le dossier racine du projet, peu importe où le script est exécuté
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    backup_dir = os.path.join(project_root, 'backup_zip')  # Dossier 'backup_zip' à la racine du projet

    # Vérification si le dossier 'backup_zip' existe, sinon création
    if not os.path.exists(backup_dir):
        try:
            os.makedirs(backup_dir)
            print(f"Dossier {backup_dir} créé.")
        except OSError as e:
            print(f"Erreur lors de la création du dossier {backup_dir}: {e}")
            return None

    # Créer l'archive dans le dossier 'backup_zip'
    backup_path = os.path.join(backup_dir, backup_name.replace(".zip", ""))
    try:
        shutil.make_archive(backup_path, 'zip', home_dir)
        print(f"Archive créée : {backup_path}.zip")
    except Exception as e:
        print(f"Erreur lors de la création de l'archive : {e}")
        return None

    return os.path.join(backup_dir, backup_name)

def create_backup_based_on_os():
    """Crée une archive du répertoire personnel en fonction du système d'exploitation."""
    os_name = platform.system()
    print(f"OS détecté : {os_name}")
    
    home_dir = get_home_directory()
    backup_name = get_backup_filename()

    # Traitement spécifique en fonction du système d'exploitation
    if os_name == "Windows":
        print("Création d'une archive pour Windows...")
        # Traitement spécifique à Windows si nécessaire

    elif os_name == "Linux" or os_name == "Darwin":  # Darwin est pour macOS
        print("Création d'une archive pour Linux/macOS...")
        archive = create_backup(home_dir, backup_name)

    else:
        print(f"Système d'exploitation {os_name} non pris en charge pour cette tâche.")
        return None

    return archive


if __name__ == "__main__":
    archive = create_backup_based_on_os()
    
    if archive:
        print(f"Archive créée : {archive}")
    else:
        print("La création de l'archive a échoué.")
