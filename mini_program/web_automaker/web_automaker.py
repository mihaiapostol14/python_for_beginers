import os
import shutil
import struct
import zlib


class WebAutoMaker:
    def __init__(self, image_name: str, image_width: int, image_height: int, pixels: bytes, files_dict: dict):
        self.files_dict: dict = files_dict
        self.image_name: str = image_name
        self.image_width: int = image_width
        self.image_height: int = image_height
        self.pixels: bytes = pixels

    @staticmethod
    def create_file(directory: str, filename: str, content: str):
        if not os.path.exists(directory):
            os.mkdir(directory)

        file_path = os.path.join(directory, filename)
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)

    def run(self):
        """
        files_dict format:
        {
            "css": {"filename": "style.css", "content": "/* CSS file */"},
            "html": {"filename": "index.html", "content": "<!DOCTYPE html>"},
            "js": {"filename": "script.js", "content": "// JavaScript file"}
        }
        """
        for directory, file_info in self.files_dict.items():
            self.create_file(
                directory=directory,
                filename=file_info.get("filename", "default.txt"),
                content=file_info.get("content", "")
            )
        self.create_png(
            filename=self.image_name,
            width=self.image_width,
            height=self.image_height,
            pixels=self.pixels
        )

        self.check_exist_directory()

    def check_exist_directory(self, directory='assets'):
        try:
            if not os.path.exists(directory):
                os.mkdir(directory)
                shutil.move(self.image_name, directory)
        except OSError:
            print('directory not exist or not created')

    def png_chunk(self, chunk_type, data):
        length = struct.pack(">I", len(data))
        chunk_type = chunk_type.encode("ascii")
        crc = struct.pack(">I", zlib.crc32(chunk_type + data) & 0xffffffff)
        return length + chunk_type + data + crc

    def create_png(self, filename: str, width: int, height: int, pixels: bytes):
        # PNG file signature
        png_signature = b'\x89PNG\r\n\x1a\n'

        # IHDR chunk
        ihdr_data = struct.pack(
            ">IIBBBBB",
            width,
            height,
            8,  # bit depth
            2,  # color type: 2 = RGB
            0,  # compression
            0,  # filter
            0  # interlace
        )
        ihdr = self.png_chunk("IHDR", ihdr_data)

        # Image data (each row starts with filter byte 0)
        raw_data = b""
        row_bytes = width * 3  # RGB = 3 bytes per pixel

        for y in range(height):
            raw_data += b'\x00' + pixels[y * row_bytes:(y + 1) * row_bytes]

        compressed_data = zlib.compress(raw_data)
        idat = self.png_chunk("IDAT", compressed_data)

        # IEND chunk
        iend = self.png_chunk("IEND", b"")

        # Write file
        with open(filename, "wb") as f:
            f.write(png_signature)
            f.write(ihdr)
            f.write(idat)
            f.write(iend)


def main():
    files_to_create = {
        "html": {"filename": "index.html", "content": ""},
        "css": {"filename": "style.css", "content": ""},
        "js": {"filename": "script.js", "content": "// code here"},
        ".vscode": {"filename": "settings.json", "content": ""}
    }
    # ---- Create a red image ----
    image_width = 800
    image_height = 200

    # RGB pixels: red
    pixels = b'\x00\xff\x00' * (image_width * image_height)

    maker = WebAutoMaker(
        files_dict=files_to_create,
        image_name='preview.png',
        image_width=image_width,
        image_height=image_height,
        pixels=pixels
    )
    maker.run()


if __name__ == "__main__":
    main()
