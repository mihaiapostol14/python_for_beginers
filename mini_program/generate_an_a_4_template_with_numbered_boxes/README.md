# A4 Template with Numbered Boxes  

This project generates an A4-sized image (at 300 DPI) with a blue background and five evenly spaced green boxes, each containing a centered white number. The image is created programmatically using the **Pillow** library in Python.

---

## Features  
- **A4 Dimensions**: The image adheres to the standard A4 size (2480x3508 pixels) with 300 DPI resolution.  
- **Customizable Design**: Easily modify box size, colors, font size, and spacing as per your requirements.  
- **Text Centering**: Numbers in the boxes are automatically centered.

---

## Prerequisites  
- Python 3.x installed on your system.  
- The **Pillow** library installed to handle image processing.

---

### 1. Create and Activate a Virtual Environment  

```bash
# Create a virtual environment
python -m venv venv  

# Activate the virtual environment
source venv/bin/activate  # Linux/MacOS  
venv\Scripts\activate     # Windows  
```

### 2. Install the required libraries:  

```bash
pip install -r requirements.txt
```