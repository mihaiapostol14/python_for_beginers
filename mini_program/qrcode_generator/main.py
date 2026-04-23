import os
from time import sleep

import qrcode


class QRCodeGenerator:
    def __init__(self, content, filename="qrcode.png", box_size=10, border=4, fill_color="black", back_color="white"):
        self.content = content
        self.filename = filename
        self.box_size = box_size
        self.border = border
        self.fill_color = fill_color
        self.back_color = back_color

        # Generate and save the QR code
        self.generate()
        sleep(5)
        # Optionally, display the QR code
        self.show()

    def generate(self):
        # Create QR code instance
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=self.box_size,
            border=self.border,
        )

        # Add data to QR code
        qr.add_data(self.content)
        qr.make(fit=True)

        # Create image
        img = qr.make_image(fill_color=self.fill_color, back_color=self.back_color)

        # Save image
        img.save(self.filename)
        print(f"QR code successfully saved as '{self.filename}'")

    def show(self):
        # Display QR code
        os.startfile(self.filename)

def main():
    # Create an instance of QRCodeGenerator
    return QRCodeGenerator(
        content='https://discord.com/users/999642555216035942',
        filename="discord_qrcode.png",
        box_size=5,
        back_color='#313338',
        fill_color='#5865F2'
    )

if __name__ == '__main__':
    main()