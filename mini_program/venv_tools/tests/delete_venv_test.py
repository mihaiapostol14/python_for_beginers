import unittest
from unittest.mock import patch, MagicMock
import os
import shutil

# Import your function
from your_script import find_and_remove_venvs


class TestFindAndRemoveVenvs(unittest.TestCase):

    @patch("shutil.rmtree")
    @patch("os.walk")
    def test_remove_existing_venv(self, mock_walk, mock_rmtree):
        # Simulate a project with a venv folder
        mock_walk.return_value = [
            ("/root/project1", ["venv"], [])
        ]

        find_and_remove_venvs("/root", "venv")

        mock_rmtree.assert_called_once_with("/root/project1/venv")

    @patch("shutil.rmtree")
    @patch("os.walk")
    def test_no_venv_found(self, mock_walk, mock_rmtree):
        # Simulate a project with no venv
        mock_walk.return_value = [
            ("/root/project1", ["src"], [])
        ]

        find_and_remove_venvs("/root", "venv")

        mock_rmtree.assert_not_called()

    @patch("shutil.rmtree", side_effect=Exception("Permission denied"))
    @patch("os.walk")
    def test_error_handling(self, mock_walk, mock_rmtree):
        # Simulate a venv folder but raise an error when deleting
        mock_walk.return_value = [
            ("/root/project1", ["venv"], [])
        ]

        find_and_remove_venvs("/root", "venv")

        mock_rmtree.assert_called_once_with("/root/project1/venv")


if __name__ == "__main__":
    unittest.main()
