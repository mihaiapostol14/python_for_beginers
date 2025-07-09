# Create Directory with File

This Python script provides a simple utility to create a new directory and a file within it. If the directory does not already exist, it is created, and then a file with the specified name is placed inside. Optionally, you can provide text content to be written into the file.

## Features

- Creates a directory if it does not exist.
- Creates a specified file inside the new directory.
- Optionally writes data to the file.

## Usage

The main function demonstrates how to use the `create_directory_with_file` function by creating several directories (`css`, `html`, `js`) and corresponding files (`style.css`, `index.html`, `script.js`).

### Example

```python
create_directory_with_file(
    name_directory='css',
    filename='style.css',
    sone_data='body { background: #fff; }'
)
```

This will:
- Create a folder named `css` if it does not exist.
- Create a file named `style.css` inside the `css` folder.
- Write the string `body { background: #fff; }` to the file.

## Function Reference

```python
def create_directory_with_file(name_directory: str = '', filename: str = '', sone_data: str = ''):
    ...
```

- `name_directory`: Name of the directory to create.
- `filename`: Name of the file to create inside the directory.
- `sone_data`: (Optional) Text to write into the file.

## How to Run

1. Ensure you have Python installed.
2. Save the script as `main.py`.
3. Run the script:

```bash
python main.py
```

## Notes

- The function only creates the directory and file if the directory does not already exist.
- If you need to always create/overwrite the file, you can modify the logic accordingly.