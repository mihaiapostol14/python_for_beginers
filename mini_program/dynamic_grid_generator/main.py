from PIL import (
    Image,
    ImageDraw,
    ImageFont
)


class A4GridNumberTemplate:
    """
    Professional A4 Grid Number Template Generator
    """

    def __init__(
            self,
            width=2480,
            height=3508,
            background_color="#222831",
            grid_color="#393E46",
            text_color="white",
            cell_size=200,
            font_size=80,
            start_number=1,
            filename="grid_number_template.png"
    ):

        # Image settings
        self.width = width
        self.height = height
        self.background_color = background_color

        # Grid settings
        self.grid_color = grid_color
        self.cell_size = cell_size

        # Text settings
        self.text_color = text_color
        self.font_size = font_size

        # Number settings
        self.start_number = start_number

        # Filename
        self.filename = filename

        # Initialize
        self.image = self.create_image()

        self.draw = self.create_draw()

        self.font = self.load_font()

        # Auto start
        self.start()

    def create_image(self):
        """
        Create blank image.
        """

        return Image.new(
            "RGB",
            (self.width, self.height),
            self.background_color
        )

    def create_draw(self):
        """
        Create drawing object.
        """

        return ImageDraw.Draw(self.image)

    def load_font(self):
        """
        Load font.
        """

        try:
            return ImageFont.truetype(
                "arial.ttf",
                self.font_size
            )

        except IOError:

            print("Arial font not found. Using default font.")

            return ImageFont.load_default()

    def draw_grid_with_numbers(self):
        """
        Draw full grid with numbers.
        """

        number = self.start_number

        # Loop rows
        for y in range(0, self.height, self.cell_size):

            # Loop columns
            for x in range(0, self.width, self.cell_size):

                # Cell coordinates
                x2 = x + self.cell_size
                y2 = y + self.cell_size

                # Draw grid cell
                self.draw.rectangle(
                    [x, y, x2, y2],
                    outline=self.grid_color,
                    width=2
                )

                # Text
                text = str(number)

                # Text size
                bbox = self.font.getbbox(text)

                text_width = bbox[2] - bbox[0]
                text_height = bbox[3] - bbox[1]

                # Center text
                text_x = x + (self.cell_size - text_width) / 2
                text_y = y + (self.cell_size - text_height) / 2

                # Draw number
                self.draw.text(
                    (text_x, text_y),
                    text,
                    fill=self.text_color,
                    font=self.font
                )

                # Next number
                number += 1

    def save_template(self):
        """
        Save image.
        """

        self.image.save(self.filename)

        print(f"Template saved as '{self.filename}'")

    def start(self):
        """
        Start generation.
        """

        self.draw_grid_with_numbers()

        self.save_template()

        print("Grid template completed successfully.")


# ---------------------------------------------------
# Run Project
# ---------------------------------------------------

def main():

    return A4GridNumberTemplate(

        background_color="#222831",

        grid_color="#00ADB5",

        text_color="white",

        cell_size=200,

        font_size=70,

        start_number=1,

        filename="professional_grid_numbers.png"
    )


if __name__ == '__main__':
    main()