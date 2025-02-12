import os, sys
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from backup import get_home_directory, get_backup_filename, create_backup


# from src.backup import get_home_directory, get_backup_filename, create_backup

def test_get_home_directory():
    """Vérifie que la fonction retourne bien le chemin du home."""
    assert os.path.isdir(get_home_directory())

def test_get_backup_filename():
    """Vérifie que le nom de fichier généré contient une date."""
    filename = get_backup_filename()
    assert filename.startswith("backup_") and filename.endswith(".zip")

def test_create_backup():
    """Teste si la sauvegarde est bien créée."""
    filename = create_backup()
    assert os.path.isfile(filename)
    os.remove(filename)  # Nettoyage après test
