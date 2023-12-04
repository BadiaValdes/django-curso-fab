# Templates
BASE_TEMPLATE_DIR = '../templates/'

# Template for st_mvc
ST_MVC_TEMPLATE_DIR = f'{BASE_TEMPLATE_DIR}st_mvc/'
INDEX_TEMPLATE = f'{ST_MVC_TEMPLATE_DIR}index.html'

# Templates for obj 3
FORM_TEMPLATE_DIR = f'{BASE_TEMPLATE_DIR}form_obj3/'
INDEX_TEMPLATE_FORM = f'{FORM_TEMPLATE_DIR}index_form.html'
STATIC_TEMPLATE_FORM = f'{FORM_TEMPLATE_DIR}forms/form_static.html'
PARAM_TEMPLATE_FORM = f'{FORM_TEMPLATE_DIR}forms/form_by_param.html'
MODEL_TEMPLATE_FORM = f'{FORM_TEMPLATE_DIR}forms/form_by_model.html'


# Text
## Variables


## Methods
def length_error(field,length, max: bool = False):
    return f'El campo {field} debe tener como {"máximo" if max else "mínimo"} {length} caracteres'


# Field
NAME_MAX_LENGTH = 6
NAME_MIN_LENGTH = 4

# Methods
METHODS = {
    "GET": "GET",
    "POST": "POST",
    "DELETE": "DELETE"
}

# Error Messages
START_UPPER_CASE = 'El mensaje debe comenzar con mayuscula'
