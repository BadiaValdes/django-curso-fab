# URL
BASE_TEMPLATE_DIR = '../templates/st_mvc/'
INDEX_TEMPLATE = f'{BASE_TEMPLATE_DIR}index.html'


# Text
## Variables


## Methods
def length_error(field,length, max: bool = False):
    return f'El campo {field} debe tener como {"máximo" if max else "mínimo"} {length} caracteres'


# Field
NAME_MAX_LENGTH = 6
NAME_MIN_LENGTH = 4
