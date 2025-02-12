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

def create_backup():
    """Crée une archive ZIP du répertoire personnel."""
    home_dir = get_home_directory()
    backup_name = get_backup_filename()
    
    shutil.make_archive(backup_name.replace(".zip", ""), 'zip', home_dir)
    return backup_name

if __name__ == "__main__":
    os_name = platform.system()
    print(f"OS détecté : {os_name}")
    
    archive = create_backup()
    print(f"Archive créée : {archive}")
