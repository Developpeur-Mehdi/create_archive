import os
import sys
import pytest
from unittest.mock import patch
import zipfile

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

    # Mock de l'appel à zipfile.ZipFile pour éviter la création réelle de l'archive
    with patch('zipfile.ZipFile') as mock_zipfile:
        # Nous faisons simplement une simulation de la méthode .write
        mock_zipfile.return_value.__enter__.return_value.write = lambda *args, **kwargs: None

        # Appel de la fonction avec les bons arguments
        filename = create_backup(home_dir, backup_name)

        # Vérifie que le nom de fichier retourné contient bien le nom attendu
        expected_filename = os.path.basename(filename)  # On prend juste le nom de fichier, pas le chemin complet
        assert expected_filename == backup_name  # Compare seulement le nom du fichier

        # Vérifie que zipfile.ZipFile a bien été appelé avec le bon chemin
        # Le répertoire backup_zip est un répertoire au niveau du projet, pas dans 'tests'
        expected_path = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')), 'backup_zip', backup_name.replace(".zip", "")) + '.zip'

        # Le chemin réel est également basé sur le répertoire actuel (tests), mais sans '..' dans le chemin attendu
        actual_path = os.path.join(os.path.dirname(__file__), 'backup_zip', backup_name.replace(".zip", "")) + '.zip'

        # Vérifie que zipfile.ZipFile a bien été appelé avec le bon chemin
        # Comparons les chemins absolus
        mock_zipfile.assert_called_once_with(expected_path, 'w', zipfile.ZIP_DEFLATED)
