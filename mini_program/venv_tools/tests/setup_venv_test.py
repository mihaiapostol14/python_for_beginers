import unittest
from unittest.mock import patch, MagicMock
import subprocess

# Import your function
from your_script import setup_project_envs


class TestSetupProjectEnvs(unittest.TestCase):

    @patch("os.path.isfile")
    @patch("os.path.isdir")
    @patch("subprocess.check_call")
    @patch("os.walk")
    def test_create_venv_and_install_requirements(self, mock_walk, mock_check_call, mock_isdir, mock_isfile):
        # Simulate one project folder with requirements.txt
        mock_walk.return_value = [
            ("/root", ["project1"], [])
        ]
        mock_isdir.return_value = False   # venv doesn't exist
        mock_isfile.return_value = True   # requirements.txt exists

        setup_project_envs("/root", "venv")

        # Should create venv
        mock_check_call.assert_any_call(["python", "-m", "venv", "/root/project1/venv"])
        # Should install requirements
        pip_path = "/root/project1/venv/Scripts/pip.exe"
        mock_check_call.assert_any_call([pip_path, "install", "-r", "/root/project1/requirements.txt"])

    @patch("os.path.isfile")
    @patch("os.path.isdir")
    @patch("subprocess.check_call")
    @patch("os.walk")
    def test_skip_existing_venv(self, mock_walk, mock_check_call, mock_isdir, mock_isfile):
        mock_walk.return_value = [
            ("/root", ["project1"], [])
        ]
        mock_isdir.return_value = True   # venv already exists
        mock_isfile.return_value = False # no requirements.txt

        setup_project_envs("/root", "venv")

        # Should not call python -m venv
        self.assertNotIn(
            (("python", "-m", "venv", "/root/project1/venv"),),
            [c[0] for c in mock_check_call.call_args_list]
        )
        # Should not install anything
        self.assertEqual(mock_check_call.call_count, 0)

    @patch("os.path.isfile")
    @patch("os.path.isdir")
    @patch("subprocess.check_call", side_effect=subprocess.CalledProcessError(1, "python"))
    @patch("os.walk")
    def test_error_creating_venv(self, mock_walk, mock_check_call, mock_isdir, mock_isfile):
        mock_walk.return_value = [
            ("/root", ["project1"], [])
        ]
        mock_isdir.return_value = False  # no venv
        mock_isfile.return_value = True  # has requirements.txt

        setup_project_envs("/root", "venv")

        # It tried to create but failed
        mock_check_call.assert_called_once_with(["python", "-m", "venv", "/root/project1/venv"])


if __name__ == "__main__":
    unittest.main()
