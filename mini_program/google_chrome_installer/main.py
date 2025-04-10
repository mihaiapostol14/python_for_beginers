import webbrowser as wb

# Class to handle the installation process of Google Chrome
class GgoogleChromeInstaller:
    def __init__(self, url):
        """
        Constructor method to initialize the class with a URL.
        It also calls the `install` method automatically when an instance is created.
        :param url: The URL of the Google Chrome official website.
        """
        self.url = url

        # Automatically call the install method upon initialization
        self.install()

    def install(self):
        """
        This method opens the Google Chrome official website in the default web browser.
        """
        wb.open(self.url)  # Opens the provided URL in the default web browser.

# Main function to execute the program
def main():
    """
    The main function creates an instance of the GgoogleChromeInstaller class
    with the URL of the Google Chrome official website.
    """
    return GgoogleChromeInstaller(url='https://www.google.com/intl/ru_ru/chrome/')
    

if __name__ == "__main__":
    # Entry point of the script. It calls the main function.
    main()