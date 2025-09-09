import os
import re


class GitCommitGenerator:
    def __init__(self, include_files=None):
        if include_files is None:
            include_files = ['html', 'css', 'js', 'gif', 'png']
        self.include_files = include_files

    def generate_initial_commit(self, filename):
        try:
            with open(file=filename, mode='w', newline='') as file:
                file.write('')
            print(f"File '{filename}' created successfully.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def create_file_from_list(self, filename, data_list):
        """
        Create a file from a list of strings.
        """
        try:
            with open(file=filename, mode='w', newline='') as file:
                for item in data_list:
                    file.write(f"{item}\n")
            print(f"File '{filename}' created successfully.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def generate_git_commands(self, string=''):
        # Find all file paths inside href/src attributes
        paths = re.findall(r'(?:href|src)="([^"]+)"', string)

        # Keep only paths that end with the desired extensions
        result = [
            path for path in paths
            if any(path.endswith(ext) for ext in self.include_files)
        ]

        commands = []
        for path in result:
            clean_path = path.replace('../', '')
            filename = os.path.basename(clean_path)
            commands.append(
                f'git add {clean_path}\n'
                f'git commit -m "added {filename}"'
            )

        return commands

st = """
<link rel="stylesheet" href="../css/main.css">
<link rel="stylesheet" href="../css/blue_btn.css">
<link rel="stylesheet" href="../css/yellow_btn.css">
<link rel="stylesheet" href="../css/green_btn.css">
<link rel="stylesheet" href="../css/red_btn.css">
<script type="text/javascript" src="../js/script.js"></script>
"""

generator = GitCommitGenerator()

commands = generator.generate_git_commands(st)
print(commands)

generator.generate_initial_commit('initial_commit.sh')
generator.create_file_from_list('commit.sh', commands)
