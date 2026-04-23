# QRCode Generator

[![Top language](https://img.shields.io/github/languages/top/mihaiapostol14/qrcode_generator?style=flat-square)](https://github.com/mihaiapostol14/qrcode_generator)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue?style=flat-square)](#tech-stack)

A small, focused Python utility to generate QR codes as image files. The repository contains a simple, reusable `QRCodeGenerator` class (in `main.py`) which creates and saves a QR code image and attempts to open it for preview.


## Table of Contents
- [QRCode Generator](#qrcode-generator)
  - [Table of Contents](#table-of-contents)
  - [About](#about)
  - [Features](#features)
  - [Tech Stack](#tech-stack)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Project Structure](#project-structure)
  - [Notes \& Recommendations](#notes--recommendations)
  - [Contributing](#contributing)
  - [License](#license)
  - [Author](#author)

## About
QRCode Generator is a minimal Python project that demonstrates how to programmatically create QR codes (PNG images) using the `qrcode` and `Pillow` libraries. The code is intentionally small and easy to read, making it suitable as a learning example or a starting point for integration into larger projects.

## Features
- Generate QR code images from arbitrary text/URLs.
- Customizable filename, box size, border, foreground and background colors.
- Simple preview/open behavior (Windows `os.startfile()` used by default).

## Tech Stack
- Python: 3.8+
- Key libraries (from `requirements.txt`):
  - colorama==0.4.6
  - pillow==11.1.0 (PIL)
  - qrcode==8.0

These versions are what the repository currently lists in `requirements.txt`. The code is compatible with modern CPython 3.8+ runtimes; use the latest patch release available for your interpreter series when possible.

## Installation

1. Create and activate a virtual environment
```bash
# Create a virtual environment
python -m venv venv  

# Activate the virtual environment
source venv/bin/activate  # Linux/MacOS  
venv\Scripts\activate     # Windows
```


2. Install dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## Usage

Run the included example script (creates `discord_qrcode.png` by default):
```bash
python main.py
```



## Project Structure
```
qrcode_generator/
├── main.py           # Core QRCodeGenerator class and example usage
├── requirements.txt  # Project dependencies
└── README.md         # Project documentation (this file)
```

## Notes & Recommendations
- Add a small CLI interface (argparse / click) so users can pass content, filename, colors, and options from the terminal.
- Consider adding a cross-platform preview implementation (see usage notes).
- Add unit tests for generation behavior and CI (GitHub Actions) if you plan to extend functionality.
- Add a LICENSE file to clarify reuse terms.

## Contributing
Contributions are welcome. Please open an issue or submit a pull request with proposed changes. For substantial changes, please include tests and update this README with usage examples.

## License
No license file is included in the repository currently. If you intend to publish this project, add a LICENSE (for example MIT, Apache-2.0) to make reuse terms explicit.

---

If you'd like, I can:
- Add a small CLI wrapper and a cross-platform preview change,
- Add a GitHub Actions workflow to run simple checks,
- Or update this README further to include examples/screenshots once you provide a demo link or sample images.

## Author

[Mihai Apostol](https://github.com/mihaiapostol14)