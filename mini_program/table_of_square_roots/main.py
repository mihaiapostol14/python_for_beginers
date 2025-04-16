import matplotlib.pyplot as plt

class SquareTablet:
    def __init__(self, size, width=6, height=6):
        """
        Initializes the SquareTablet object.

        Args:
            size (int): Number of rows and columns in the square tablet.
            width (float): Width of the figure in inches. Default is 6.
            height (float): Height of the figure in inches. Default is 6.
        """
        self.size = size
        self.width = width
        self.height = height
        self.data = self._generate_data()

    def _generate_data(self):
        """Generates the 2D number data for the tablet."""
        return [[i * self.size + j + 1 for j in range(self.size)] for i in range(self.size)]

    def show(self):
        """Displays the tablet as a matplotlib figure."""
        fig, ax = plt.subplots(figsize=(self.width, self.height))
        table = ax.table(cellText=self.data, loc='center')
        table.set_fontsize(12)
        table.scale(1, 2)
        ax.axis('off')
        plt.show()


def main():
    tablet = SquareTablet(size=12, width=10, height=10)
    tablet.show()


if __name__ == '__main__':
    main()
