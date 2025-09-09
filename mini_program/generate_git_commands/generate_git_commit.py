import os
import re


class GitCommitGenerator:
    def __init__(self, include_files=None):
        if include_files is None:
            include_files = ['.ico', '.png', '.svg', '.webp', '.jpg', '.jpeg', '.gif', '.webmanifest', '.avif', '.bmp', 'html', 'css', 'js', 'gif', 'png']
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

    def read_html_file(self, filepath):
        """
        Read and return HTML file content as string.
        """
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                return file.read()
        except Exception as e:
            print(f"Failed to read HTML file: {e}")
            return ""

    def generate_git_commands(self, string=''):
        # Find all file paths inside href/src attributes
        paths = re.findall(r'(?:href|src)="([^"]+)"', string)

        # Keep only paths that end with desired extensions
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
    
generator = GitCommitGenerator()

html_content = generator.read_html_file('./html/index.html')
commands = generator.generate_git_commands(html_content)

generator.generate_initial_commit('initial_commit.sh')
generator.create_file_from_list('commit.sh', commands)

print(commands)
