import os
import sys
import pytest

# Assurez-vous d'ajouter le bon chemin vers le dossier src
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from backup import get_home_directory, get_backup_filename, create_backup


def test_get_home_directory():
    """Vérifie que la fonction retourne bien le chemin du home."""
    assert os.path.isdir(get_home_directory())


def test_get_backup_filename():
    """Vérifie que le nom de fichier généré contient une date."""
    filename = get_backup_filename()
    assert filename.startswith("backup_") and filename.endswith(".zip")


def test_create_backup():
    """Teste si la sauvegarde est bien créée."""
    home_dir = get_home_directory()
    backup_name = get_backup_filename()
    
    # Appel de la fonction avec les bons arguments
    filename = create_backup(home_dir, backup_name)
    
    assert os.path.isfile(filename)  # Vérifie que le fichier existe
    os.remove(filename)  # Nettoyage après test
