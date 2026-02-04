import os
from PIL import Image, ImageDraw, ImageFont

class CardGenerator:
    """
    Handles the generation of high-resolution printable cards.
    """
    # Standard A4 dimensions at 300 DPI
    A4_WIDTH = 2480
    A4_HEIGHT = 3508

    @staticmethod
    def generate_set(start, end, font_path="arial.ttf", bg_hex="#2B2B2B", text_color="white", font_size=1200):
        """
        Static method to generate a batch of A4-sized cards for high-quality printing.
        
        :param start: Starting integer for the sequence.
        :param end: Ending integer for the sequence.
        :param font_path: Path to the TrueType/OpenType font file.
        :param bg_hex: Background color in hexadecimal format.
        :param text_color: Text color (name or RGB).
        :param font_size: Font size in pixels.
        """
        output_dir = "cards_for_print"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Parse HEX color string to RGB tuple
        bg_rgb = tuple(int(bg_hex.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))

        try:
            font = ImageFont.truetype(font_path, font_size)
        except OSError:
            print(f"[-] Error: Failed to load font at {font_path}")
            return

        print(f"[*] Initializing generation: Range {start} to {end}")

        for i in range(start, end + 1):
            # Initialize A4 canvas with the specified background color
            img = Image.new("RGB", (CardGenerator.A4_WIDTH, CardGenerator.A4_HEIGHT), bg_rgb)
            draw = ImageDraw.Draw(img)
            
            text = str(i)
            
            # Calculate text bounding box for precise centering
            bbox = draw.textbbox((0, 0), text, font=font)
            tw = bbox[2] - bbox[0]
            th = bbox[3] - bbox[1]
            
            # Center coordinates adjusted for glyph offsets
            x = (CardGenerator.A4_WIDTH - tw) / 2 - bbox[0]
            y = (CardGenerator.A4_HEIGHT - th) / 2 - bbox[1]
            
            draw.text((x, y), text, font=font, fill=text_color)
            
            # Export with 300 DPI metadata for print accuracy
            filename = os.path.join(output_dir, f"A4_card_{i:02d}.png")
            img.save(filename, "PNG", dpi=(300, 300))
            print(f"[+] Exported: {filename}")

# --- ENTRY POINT ---
if __name__ == "__main__":
    # Static method call: Invoked directly from the class without instantiation
    CardGenerator.generate_set(
        start=1, 
        end=11, 
        font_path="verdina.ttf",  # Ensure this path is valid for your OS
        bg_hex="#FFD700",        # Gold theme
        font_size=1300
    )