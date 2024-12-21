import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PATH_DATA = os.path.join(ROOT_DIR, 'data')
PATH_DATA_INPUT = os.path.join(PATH_DATA, 'input')
PATH_DATA_OUTPUT = os.path.join(PATH_DATA, 'output')
PATH_FIGURES = os.path.join(PATH_DATA_OUTPUT, 'figures')
PATH_TEMP = os.path.join(PATH_DATA_OUTPUT, 'temp')

PATH_SRC = os.path.join(ROOT_DIR, 'src')
