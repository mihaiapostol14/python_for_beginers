import unittest
from unittest.mock import patch, MagicMock
import os
import subprocess

# Import your function
from your_script import find_and_create_venvs


class TestFindAndCreateVenvs(unittest.TestCase):

    @patch("os.path.isdir")
    @patch("subprocess.check_call")
    @patch("os.walk")
    def test_create_new_venv(self, mock_walk, mock_check_call, mock_isdir):
        # Setup: pretend we have 2 projects in root
        mock_walk.return_value = [
            ("/root", ["project1", "project2"], [])
        ]
        # No venvs exist yet
        mock_isdir.return_value = False

        find_and_create_venvs("/root", "venv")

        # Should try to create venv twice
        self.assertEqual(mock_check_call.call_count, 2)
        mock_check_call.assert_any_call(["python", "-m", "venv", "/root/project1/venv"])
        mock_check_call.assert_any_call(["python", "-m", "venv", "/root/project2/venv"])

    @patch("os.path.isdir")
    @patch("subprocess.check_call")
    @patch("os.walk")
    def test_skip_existing_venv(self, mock_walk, mock_check_call, mock_isdir):
        mock_walk.return_value = [
            ("/root", ["project1"], [])
        ]
        # Pretend venv already exists
        mock_isdir.return_value = True

        find_and_create_venvs("/root", "venv")

        # Should not call subprocess
        mock_check_call.assert_not_called()

    @patch("os.path.isdir")
    @patch("subprocess.check_call")
    @patch("os.walk")
    def test_error_handling(self, mock_walk, mock_check_call, mock_isdir):
        mock_walk.return_value = [
            ("/root", ["project1"], [])
        ]
        mock_isdir.return_value = False

        # Force subprocess to fail
        mock_check_call.side_effect = subprocess.CalledProcessError(1, "python")

        find_and_create_venvs("/root", "venv")

        # Even though it failed, it should have tried once
        mock_check_call.assert_called_once_with(["python", "-m", "venv", "/root/project1/venv"])


if __name__ == "__main__":
    unittest.main()
