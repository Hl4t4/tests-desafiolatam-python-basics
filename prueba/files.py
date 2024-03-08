import os

#Se crean los directorios en caso de que no existan
os.makedirs('html/assets/img', exist_ok=True)
os.makedirs('html/assets/css', exist_ok=True)

def make_files(path, string):
    """Esta funcion recibe datos y un path para crear un archivo
    Parameters
    ----------
    path: [str]
        String del path a donde se guardara el archivo
    string: [str]
        String que contiene los datos a guardar dentro del archivo
    Returns
    ----------
    """
    with open(path, 'w', encoding='utf-8') as f:
        f.write(string)

