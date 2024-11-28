from PIL import Image, ImageDraw, ImageFont

# A4 size in pixels at 300 DPI
A4_WIDTH = 2480
A4_HEIGHT = 3508

# Create a blank A4 image with a blue background
image = Image.new("RGB", (A4_WIDTH, A4_HEIGHT), "#1CC88F")
draw = ImageDraw.Draw(image)

# Box size and color
box_size = 500
box_color = "green"
text_color = "white"

# Font settings - Replace with a valid TrueType font path
font_size = 200  # Adjusted font size
try:
    font = ImageFont.truetype("arial.ttf", font_size)  # Use a TrueType font with specified size
except IOError:
    print("TrueType font not found. Using default font.")
    font = ImageFont.load_default()  # Fallback to default font

# Starting position for the boxes
start_x = 100
start_y = 100
spacing = 555  # Space between boxes

# Draw 5 green boxes with numbers
for i in range(5):
    box_x1 = start_x
    box_y1 = start_y + i * spacing
    box_x2 = box_x1 + box_size
    box_y2 = box_y1 + box_size
    draw.rectangle([box_x1, box_y1, box_x2, box_y2], fill=box_color)

    # Add the number inside the box
    number = str(i + 1)
    text_width, text_height = font.getbbox(number)[2:4]  # Get text width and height
    text_x = box_x1 + (box_size - text_width) / 2
    text_y = box_y1 + (box_size - text_height) / 2
    draw.text((text_x, text_y), number, fill=text_color, font=font)

# Save the image
image.save("a4_template_with_boxes.png")
print("Template saved as 'a4_template_with_boxes.png'")
