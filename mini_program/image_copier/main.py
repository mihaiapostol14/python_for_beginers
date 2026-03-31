import os

from PIL import Image


class ImageCopier:
    def __init__(self, image_path, count=1, output_dir='copied_image'):
        """Initializes the copier with file, count, and target directory."""
        self.image_path = image_path
        self.count = count
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

        self.duplicate_image()

    def align_pillow_extension(self, filename):
        """Standardizes extensions for Pillow's save format."""
        extension = self.get_extension(filename=filename)
        match extension:
            case 'JPG' | 'JPEG':
                return 'JPEG'
            case 'PNG':
                return 'PNG'
            case _:
                return extension

    def get_extension(self, filename):
        """Helper to extract file extension."""
        return filename.rsplit('.', 1)[1] if '.' in filename else ''

    def get_basename(self, filename):
        """Helper to extract filename without extension."""
        return filename.rsplit('.', 1)[0]

    def duplicate_image(self):
        """Creates copies based on the count and path defined in __init__."""
        if not os.path.exists(self.image_path):
            print(f"Error: {self.image_path} not found.")
            return

        ext = self.get_extension(self.image_path)
        base = self.get_basename(self.image_path)

        with Image.open(self.image_path) as img:
            # Loop using the count stored in the class instance
            for n in range(1, self.count + 1):
                new_name = f"copy_{base}_{n}.{ext}"
                save_path = os.path.join(self.output_dir, new_name)

                # Save the image using the aligned format
                img.save(save_path, format=self.align_pillow_extension(filename=ext.upper()))
                print(f"Saved: {save_path}")


# --- Usage ---
def main():
    # All configuration happens here
    return ImageCopier(
        image_path='image.jpg', # For Example
        output_dir='my_copies',
        count=100
    )


if __name__ == "__main__":
    main()
