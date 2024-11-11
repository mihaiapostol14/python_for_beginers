import os


def create_directory_with_file(name_directory:str='', filename:str='', sone_data:str=''):
    if not os.path.exists(name_directory):
        os.mkdir(name_directory)
        
        with open(file=f'{name_directory}/{filename}', mode='w') as file:
            file.write(sone_data)

def main():
    # used examples
    create_directory_with_file(
        name_directory='css',
        filename='style.css'
    )

    create_directory_with_file(
        name_directory='html',
        filename='index.html'
    )

    create_directory_with_file(
        name_directory='js',
        filename='script.js'
    )

if __name__ == '__main__':
    main()